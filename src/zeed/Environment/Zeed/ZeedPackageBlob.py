import json

class ZeedPackageBlob:
    """Zeed包的文件数据维护类"""
    
    def __init__(self, from_blob: str, to_blob: str):
        self.type = "blob"
        self.from_blob = from_blob
        self.to_blob = to_blob

    def get_dict(self) -> dict:
        return {
            "type": self.type,
            "from_blob": self.from_blob,
            "to_blob": self.to_blob
        }

    def get_json(self) -> str:
        return json.dumps(self.get_dict(), indent=4)

import json

class ZeedPackageBlobRule:
    """Zeed包的文件数据维护类"""
    
    def __init__(self, from_dir: str, files_filter: str):
        self.type = "blob_rule"
        self.from_dir = from_dir
        self.files_filter = files_filter

    def get_from_dir(self) -> str:
        return self.from_dir

    def get_files_filter(self) -> str:
        return self.files_filter

    def get_dict(self) -> dict:
        return {
            "type": self.type,
            "from_dir": self.from_dir,
            "files_filter": self.files_filter
        }

    def get_json(self) -> str:
        return json.dumps(self.get_dict(), indent=4)
