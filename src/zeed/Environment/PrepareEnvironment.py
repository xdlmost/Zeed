from typing import Union, Tuple
from zeed.Environment.Base import Base

class PrepareEnvironment(Base):
    """准备环境的类,继承自Base"""
    
    @staticmethod
    def _ensure_python_version(required_version: Union[str, Tuple[int, int]]) -> None:
        """
        Static method to check if current Python version meets the requirement
        
        Args:
            required_version: Required Python version, can be string format ("major.minor") 
                            or tuple format (major, minor). Defaults to "3.10"
            
        Raises:
            RuntimeError: When Python version requirement is not met
            ValueError: When version format is invalid
        """
        current_version = Base._get_current_python_version()
        required_tuple = None
        if isinstance(required_version, str):
            try:
                major_str, minor_str = required_version.split(".")
                required_tuple = (int(major_str), int(minor_str))
            except (ValueError, TypeError):
                raise ValueError(f"Invalid version format: {required_version}. Expected format: 'major.minor' or (major, minor)")
        elif isinstance(required_version, tuple) and len(required_version) == 2 and isinstance(required_version[0], int) and isinstance(required_version[1], int):
            required_tuple = required_version
        else:
            raise ValueError(f"Invalid version type: {type(required_version)}. Expected tuple (major, minor)")
        
        if required_tuple is None:
            raise ValueError(f"Invalid version type: {type(required_version)}. Expected tuple (major, minor)")
        
        if current_version[0] < required_tuple[0] or (
            current_version[0] == required_tuple[0] and current_version[1] < required_tuple[1]
        ):
            raise RuntimeError(
                f"Python version requirement not met: requires {required_tuple[0]}.{required_tuple[1]} or higher, "
                f"current version is {current_version[0]}.{current_version[1]}"
            )
        
    @classmethod
    def _get_prepare_environment_globals(cls) -> dict:
        return {
            "EnsurePythonVersion": cls._ensure_python_version
        }
