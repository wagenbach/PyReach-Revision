"""
Migration script to convert Django model groups to TypeClass groups.

Run this script to migrate from the old Django model system to the new TypeClass system.
This should be run from the Evennia Python shell (@py command).

Usage in Evennia shell:
exec(open('world/groups/migrate_to_typeclass.py').read())
"""

from evennia import logger
from typeclasses.groups import create_group, get_group_by_name

def migrate_groups_to_typeclass():
    """
    Migrate all existing Django model groups to TypeClass groups.
    """
    try:
        from world.cofd.models import Group as DjangoGroup, GroupMembership
    except ImportError:
        print("Django Group models not found - migration not needed.")
        return
    
    # Get all existing Django groups
    django_groups = DjangoGroup.objects.all()
    
    if not django_groups.exists():
        print("No Django groups found to migrate.")
        return
    
    print(f"Found {django_groups.count()} Django groups to migrate...")
    
    migrated_count = 0
    error_count = 0
    
    for django_group in django_groups:
        try:
            print(f"Migrating group: {django_group.name}")
            
            # Check if TypeClass group already exists
            existing_typeclass = get_group_by_name(django_group.name)
            if existing_typeclass:
                print(f"  TypeClass group '{django_group.name}' already exists, skipping...")
                continue
            
            # Create new TypeClass group
            typeclass_group = create_group(
                name=django_group.name,
                group_type=django_group.group_type,
                description=django_group.description or ''
            )
            
            # Set additional properties
            typeclass_group.notes = django_group.notes or ''
            typeclass_group.is_public = django_group.is_public
            
            # Set leader if exists
            if django_group.leader:
                typeclass_group.leader = django_group.leader
                print(f"  Set leader: {django_group.leader.name}")
            
            # Migrate all memberships
            memberships = GroupMembership.objects.filter(group=django_group)
            member_count = 0
            
            for membership in memberships:
                character = membership.character
                
                # Add member to TypeClass group
                if typeclass_group.add_member(character):
                    member_count += 1
                    
                    # Set title if exists
                    if membership.title:
                        typeclass_group.set_member_title(character, membership.title)
                    
                    # Set role if exists
                    if membership.role:
                        typeclass_group.set_member_role(character, membership.role.name)
            
            print(f"  Migrated {member_count} members")
            migrated_count += 1
            
        except Exception as e:
            print(f"  ERROR migrating {django_group.name}: {str(e)}")
            error_count += 1
            logger.log_err(f"Error migrating group {django_group.name}: {str(e)}")
    
    print(f"\nMigration complete!")
    print(f"Successfully migrated: {migrated_count} groups")
    print(f"Errors: {error_count} groups")
    
    if migrated_count > 0:
        print("\nMigration successful! You should now:")
        print("1. Test the new TypeClass groups to ensure they work correctly")
        print("2. Update any custom code that references Django Group models")
        print("3. Consider removing the old Django Group models from your database")
        print("   (after ensuring everything works)")


def cleanup_old_django_groups():
    """
    Remove old Django groups after successful migration.
    
    WARNING: This will permanently delete all Django Group and GroupMembership records!
    Only run this after verifying the TypeClass migration was successful.
    """
    try:
        from world.cofd.models import Group as DjangoGroup, GroupMembership
    except ImportError:
        print("Django Group models not found - cleanup not needed.")
        return
    
    # Count records
    group_count = DjangoGroup.objects.count()
    membership_count = GroupMembership.objects.count()
    
    if group_count == 0:
        print("No Django groups found to clean up.")
        return
    
    print(f"WARNING: This will delete {group_count} Django groups and {membership_count} memberships!")
    print("Make sure you have successfully migrated to TypeClass groups first!")
    
    confirm = input("Type 'DELETE' to confirm deletion: ")
    if confirm != 'DELETE':
        print("Cleanup cancelled.")
        return
    
    # Delete all memberships first
    GroupMembership.objects.all().delete()
    print(f"Deleted {membership_count} group memberships")
    
    # Delete all groups
    DjangoGroup.objects.all().delete()
    print(f"Deleted {group_count} groups")
    
    print("Django group cleanup complete!")


def verify_migration():
    """
    Verify that the migration was successful by comparing counts and data.
    """
    try:
        from world.cofd.models import Group as DjangoGroup, GroupMembership
        django_available = True
    except ImportError:
        django_available = False
    
    from typeclasses.groups import get_all_groups
    
    typeclass_groups = get_all_groups()
    typeclass_count = len(typeclass_groups)
    
    print(f"TypeClass groups found: {typeclass_count}")
    
    if django_available:
        django_count = DjangoGroup.objects.count()
        print(f"Django groups found: {django_count}")
        
        if django_count > 0 and typeclass_count > 0:
            print("Both Django and TypeClass groups exist.")
            print("Verify TypeClass groups work correctly before running cleanup_old_django_groups()")
        elif django_count > 0:
            print("Only Django groups found - run migrate_groups_to_typeclass()")
        elif typeclass_count > 0:
            print("Only TypeClass groups found - migration appears complete!")
    else:
        if typeclass_count > 0:
            print("TypeClass groups found, Django models not available.")
        else:
            print("No groups found in either system.")
    
    # Show some sample data
    if typeclass_count > 0:
        print("\nSample TypeClass groups:")
        for i, group in enumerate(typeclass_groups[:5]):
            member_count = group.get_member_count()
            print(f"  {group.name} (#{group.group_id}) - {member_count} members")
            if i >= 4:  # Show max 5
                break


if __name__ == "__main__":
    print("Group Migration Script")
    print("=" * 40)
    print("Available functions:")
    print("- migrate_groups_to_typeclass() - Convert Django groups to TypeClass")
    print("- verify_migration() - Check migration status")
    print("- cleanup_old_django_groups() - Remove old Django groups (DANGEROUS)")
    print("")
    print("Start with: migrate_groups_to_typeclass()") 