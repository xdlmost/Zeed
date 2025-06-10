import json
from pathlib import Path
from zeed.Environment.Base import Base
from zeed.Environment.ENVReader import ENVReader
from zeed.Environment.Zeed import ZeedPackageDesc
from zeed.Utils import Hash, PackageMaker
from zeed.Utils.FileSystem import FileSystem, FS

class ExecuteEnvironment(Base):
    """准备环境的类,继承自Base"""
    
    def __init__(self, absolute_zeed_file_path: str):
        super().__init__()
        self.zeeds = []
        self.INSTALL_CACHE_DIR = ENVReader.get_env(ENVReader.ENV_ZEED_INSTALL_CACHE_DIR, ENVReader.ENV_ZEED_INSTALL_CACHE_DIR_DEFAULT)
        self.INSTALL_DIR = ENVReader.get_env(ENVReader.ENV_ZEED_INSTALL_DIR, ENVReader.ENV_ZEED_INSTALL_DIR_DEFAULT)
        tmp = ENVReader.get_env(ENVReader.ENV_ZEED_PACKAGE_OUTPUT_DIR, ENVReader.ENV_ZEED_PACKAGE_OUTPUT_DIR_DEFAULT)
        if FileSystem.is_absolute_path(tmp):
            self.PACKAGE_OUTPUT_DIR = tmp
        else:
            self.PACKAGE_OUTPUT_DIR = Path(FileSystem.get_path_dir(absolute_zeed_file_path)) / tmp
        self.fs = FS(self.PACKAGE_OUTPUT_DIR)

        self._hash_func = Hash.sha256
        self._package_make_func = PackageMaker.make_tar_gz


    def _get_execute_environment_globals(self) -> dict:
        return {}
    
    def get_dict(self) -> dict:
        return {
            "zeeds": [zeed.get_dict() for zeed in self.zeeds],
            "INSTALL_CACHE_DIR": self.INSTALL_CACHE_DIR,
            "INSTALL_DIR": self.INSTALL_DIR,
            "PACKAGE_OUTPUT_DIR": self.PACKAGE_OUTPUT_DIR,
            "hash_func": self._hash_func,
            "package_make_func": self._package_make_func
        }
    
    def get_json(self) -> str:
        return json.dumps(self.get_dict(), indent=4, ensure_ascii=False)
    