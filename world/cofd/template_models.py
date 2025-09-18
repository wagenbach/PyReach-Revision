"""
Template system models for Chronicles of Darkness.
Allows for modular template installation and management.
"""

from django.db import models
from evennia.utils.idmapper.models import SharedMemoryModel


class TemplateDefinition(SharedMemoryModel):
    """
    Model for storing character template definitions.
    Templates can be installed/uninstalled dynamically.
    """
    name = models.CharField(max_length=50, unique=True, help_text="Template name (e.g., 'Vampire', 'Mage')")
    display_name = models.CharField(max_length=50, help_text="Display name for the template")
    description = models.TextField(blank=True, help_text="Description of the template")
    
    # Template configuration stored as JSON
    bio_fields = models.JSONField(default=list, help_text="Required bio fields for this template")
    integrity_name = models.CharField(max_length=50, default="Integrity", help_text="Name of integrity stat for this template")
    starting_integrity = models.IntegerField(default=7, help_text="Starting integrity value")
    
    # Field validation rules
    field_validations = models.JSONField(default=dict, help_text="Validation rules for template-specific fields")
    
    # Template status
    is_active = models.BooleanField(default=True, help_text="Whether this template is available for use")
    is_system = models.BooleanField(default=False, help_text="System template (cannot be deleted)")
    
    # Metadata
    version = models.CharField(max_length=20, default="1.0", help_text="Template version")
    author = models.CharField(max_length=100, blank=True, help_text="Template author/creator")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Installation tracking
    installed_by = models.ForeignKey('objects.ObjectDB', on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return f"{self.display_name} ({self.name})"
    
    def get_bio_fields(self):
        """Return the bio fields for this template."""
        return self.bio_fields or []
    
    def get_field_validation(self, field_name):
        """Get validation rules for a specific field."""
        return self.field_validations.get(field_name, {})
    
    def validate_field_value(self, field_name, value):
        """
        Validate a field value against template rules.
        
        Returns:
            tuple: (is_valid, error_message)
        """
        validation = self.get_field_validation(field_name)
        if not validation:
            return True, None
        
        valid_values = validation.get('valid_values', [])
        if valid_values and value.lower() not in [v.lower() for v in valid_values]:
            return False, f"Invalid {field_name}. Valid options: {', '.join(valid_values).title()}"
        
        return True, None


class TemplatePackage(SharedMemoryModel):
    """
    Model for storing template packages (collections of templates).
    Useful for game lines or themed template sets.
    """
    name = models.CharField(max_length=100, unique=True)
    display_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    # Package metadata
    version = models.CharField(max_length=20, default="1.0")
    author = models.CharField(max_length=100, blank=True)
    game_line = models.CharField(max_length=50, blank=True, help_text="Game line (e.g., 'World of Darkness')")
    
    # Package status
    is_active = models.BooleanField(default=True)
    
    # Installation tracking
    installed_at = models.DateTimeField(auto_now_add=True)
    installed_by = models.ForeignKey('objects.ObjectDB', on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.display_name
    
    def get_templates(self):
        """Get all templates in this package."""
        return TemplateDefinition.objects.filter(package=self)


class TemplateUsage(SharedMemoryModel):
    """
    Track which characters are using which templates.
    Useful for migration and dependency management.
    """
    character = models.ForeignKey('objects.ObjectDB', on_delete=models.CASCADE, related_name='template_usage')
    template = models.ForeignKey(TemplateDefinition, on_delete=models.CASCADE, related_name='character_usage')
    assigned_at = models.DateTimeField(auto_now_add=True)
    assigned_by = models.ForeignKey('objects.ObjectDB', on_delete=models.SET_NULL, null=True, blank=True, related_name='template_assignments')
    
    class Meta:
        unique_together = ('character', 'template')
    
    def __str__(self):
        return f"{self.character.name} - {self.template.display_name}" 