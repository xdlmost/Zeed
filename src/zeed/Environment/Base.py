import sys
from typing import Tuple
from zeed import __version__ as zeed_version

class Base(dict):
    """Base class for Environment, inherits from dict"""

    @staticmethod
    def _get_current_python_version() -> Tuple[int, int]:
        """
        Get current Python version as a tuple
        
        Returns:
            Tuple[int, int]: A tuple containing major and minor version numbers
        """
        return (sys.version_info.major, sys.version_info.minor)
    
    @staticmethod
    def _get_current_zeed_version() -> Tuple[int, int, int]:
        """
        Get current Zeed version as a tuple
        
        Returns:
            Tuple[int, int, int]: A tuple containing major, minor and patch version numbers
        """
        version_parts = zeed_version.split('.')
        if len(version_parts) == 3:
            return tuple(int(part) for part in version_parts)
        else:
            raise ValueError(f"Invalid Zeed version format: {zeed_version}")