from typing import Optional
import json
from pathlib import Path
from .ZeedPackageBlob import ZeedPackageBlobRule, ZeedPackageBlob
from zeed.Utils.FileSystem import FS

class ZeedPackageDir:
    """Zeed包的目录实例类"""
    
    def __init__(self, path: str):
        self.path = path
        self.type = "dir"
        self.dirs = {}
        self.blobs = {}

    def add_dir(self, path: str) : # type: ignore
        pass

    
    def add_blob(self, path: str, content: str) -> 'ZeedPackageBlob': # type: ignore
        blob = ZeedPackageBlob(path=path, content=content)

class ZeedPackageDirRule:
    """Zeed包的目录数据维护类"""
    
    def __init__(self, path: str):
        self.path = path
        self.type = "dir"
        self.blob_rules = []

    def add_blob_rule(self, from_dir: str, files_filter: str) -> ZeedPackageBlobRule:
        rule = ZeedPackageBlobRule(from_dir=from_dir, files_filter=files_filter)
        self.blob_rules.append(rule)
        return rule
    
    def add_dir(self, path: str) -> 'ZeedPackageDirRule': # type: ignore
        dir = ZeedPackageDirRule(path=str(Path(self.path) / path))
        self.blob_rules.append(dir)
        return dir

    def expand(self, from_fs: FS, zeed_package_root_dir: ZeedPackageDir):
        for blob_rule in self.blob_rules:
            if blob_rule.type == "dir":
                zeed_package_root_dir.add_dir(blob_rule.path)


    def get_dict(self) -> dict:
        return {
            "path": self.path,  
            "type": self.type,
            "blob_rules": [rule.get_dict() for rule in self.blob_rules]
        }

    def get_json(self) -> str:
        return json.dumps(self.get_dict(), indent=4)

