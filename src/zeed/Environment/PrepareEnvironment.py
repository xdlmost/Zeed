from typing import Union, Tuple, List
import json
from zeed.Environment.Base import Base
from zeed.Utils.FileSystem import FileSystem, FS
from zeed.Environment.Zeed.ZeedPackage import ZeedPackageDesc

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
    @staticmethod
    def _ensure_zeed_version(required_version: Union[str, Tuple[int, int, int]]) -> None:
        """
        Static method to check if current Zeed version meets the requirement
        
        Args:
            required_version: Required Zeed version, can be string format ("major.minor.patch")
                            or tuple format (major, minor, patch)
            
        Raises:
            RuntimeError: When Zeed version requirement is not met
            ValueError: When version format is invalid
        """
        current_version = Base._get_current_zeed_version()
        required_tuple = None
        
        if isinstance(required_version, str):
            try:
                major_str, minor_str, patch_str = required_version.split(".")
                required_tuple = (int(major_str), int(minor_str), int(patch_str))
            except (ValueError, TypeError):
                raise ValueError(f"Invalid version format: {required_version}. Expected format: 'major.minor.patch' or (major, minor, patch)")
        elif isinstance(required_version, tuple) and len(required_version) == 3 and all(isinstance(x, int) for x in required_version):
            required_tuple = required_version
        else:
            raise ValueError(f"Invalid version type: {type(required_version)}. Expected tuple (major, minor, patch)")
        
        if required_tuple is None:
            raise ValueError(f"Invalid version type: {type(required_version)}. Expected tuple (major, minor, patch)")
        
        if current_version[0] < required_tuple[0] or (
            current_version[0] == required_tuple[0] and current_version[1] < required_tuple[1]
        ) or (
            current_version[0] == required_tuple[0] and 
            current_version[1] == required_tuple[1] and 
            current_version[2] < required_tuple[2]
        ):
            raise RuntimeError(
                f"Zeed version requirement not met: requires {required_tuple[0]}.{required_tuple[1]}.{required_tuple[2]} or higher, "
                f"current version is {current_version[0]}.{current_version[1]}.{current_version[2]}"
            )
        
    @classmethod
    def _get_prepare_environment_globals(cls) -> dict:
        return {}

    def __init__(self, absolute_zeed_file_path: str):
        super().__init__()
        self.zeed_file_dir = FileSystem.get_path_dir(absolute_zeed_file_path)
        self.zeed_file_name = FileSystem.get_path_file_name(absolute_zeed_file_path)
        self.fs = FS(self.zeed_file_dir)

        self.zeed_des_list = []
        
    def get_zeed_file_content(self) -> str:
        return self.fs.get_file_content_str(self.zeed_file_name)
    
    def expand_zeed_package(self) -> List[ZeedPackageDesc]:
        zeeds=[]
        for zeed_desc in self.zeed_des_list:
            zeeds.append(zeed_desc.expand(self.fs))
        return zeeds

    def get_dict(self) -> dict:
        return {
            "zeed_file_dir": self.zeed_file_dir,
            "zeed_file_name": self.zeed_file_name,
            "zeed_des_list": [zeed.get_dict() for zeed in self.zeed_des_list]
        }
    
    def get_json(self) -> str:
        return json.dumps(self.get_dict(), indent=4, ensure_ascii=False)
