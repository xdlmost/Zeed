from typing import Optional, List
import json
from zeed.Utils.Platform import Platform
from .ZeedPackageDir import ZeedPackageDirRule, ZeedPackageDir
from .ZeedPackageBlob import ZeedPackageBlobRule, ZeedPackageBlob
from zeed.Utils.FileSystem import FS

class ZeedPackage(ZeedPackageDir):
    """Zeed包的实例类"""

    def __init__(self, name: str, version: str, platform: Optional[str] = None):
        self.name = name
        self.version = version
        self.platform = platform if platform else Platform.get_platform()



class ZeedPackageDesc:
    """Zeed包的数据维护类"""
    
    def __init__(self, name: str, version: str, platform: Optional[str] = None):
        """
        初始化ZeedPackage实例
        
        Args:
            name: 包名称
            version: 包版本
            platform: 平台标识,如果为None则使用当前平台
        """
        self.name = name
        self.version = version
        self.platform = platform if platform else Platform.get_platform()
        self.dependencies: List['ZeedPackageDesc'] = []
        self.root_dir = ZeedPackageDirRule(path = ".")

    def add_dependency(self, dependency: 'ZeedPackageDesc') -> None:
        """添加依赖包"""
        self.dependencies.append(dependency)
    
    def add_dir(self, path: str) -> ZeedPackageDirRule:
        """添加目录"""
        return self.root_dir.add_dir(path)
    
    def add_blob_rule(self, from_dir: str, files_filter: str) -> ZeedPackageBlobRule:
        """添加文件规则"""
        return self.root_dir.add_blob_rule(from_dir, files_filter)

    def get_package_id(self) -> str:
        """获取包的唯一标识"""
        return f"{self.name}-{self.version}-{self.platform}"

    def expand(self, from_fs: FS) -> ZeedPackage:
        """扩展包"""
        zeed_package = ZeedPackage(name=self.name, version=self.version, platform=self.platform)
        self.root_dir.expand(from_fs, zeed_package)
        return zeed_package

    def get_dict(self) -> dict:
        return {
            "name": self.name,
            "version": self.version,
            "platform": self.platform,
            "dependencies": self.dependencies,
            "root_dir": self.root_dir.get_dict()   
        }

    def get_json(self) -> str:
        return json.dumps(self.get_dict(), indent=4, ensure_ascii=False)
    
