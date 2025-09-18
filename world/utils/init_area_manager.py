"""
Utility script to initialize the area manager system.
This should be run once when setting up the game.
"""

from world.area_manager import get_area_manager
from evennia import logger


def init_area_manager():
    """Initialize the area manager system."""
    try:
        area_manager = get_area_manager()
        logger.log_info("Area manager initialized successfully")
        
        # Log the available areas
        areas = area_manager.get_areas()
        logger.log_info(f"Available areas: {', '.join(areas.keys())}")
        
        return True
    except Exception as e:
        logger.log_err(f"Failed to initialize area manager: {e}")
        return False


# Call this function when the server starts
if __name__ == "__main__":
    init_area_manager()
