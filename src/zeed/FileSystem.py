from pathlib import Path

class FileSystem:
    """File system class for Zeed"""
    
    def __init__(self, file_path: str):
        # 将文件路径分解为工作路径和文件名
        self._work_dir = Path(file_path).parent
        self._main_zeedfile_name = Path(file_path).name
        
    def get_work_dir(self) -> Path:
        return self._work_dir
    
    def get_main_zeedfile_name(self) -> str:
        return self._main_zeedfile_name
    
    def get_main_zeedfile_path(self) -> Path:
        return self._work_dir / self._main_zeedfile_name  
    
    def get_zeedfile_path(self, zeedfile_name: str) -> Path:
        return self._work_dir / zeedfile_name
    
    def get_zeedfile_content(self, zeedfile_name: str) -> str:
        with open(self.get_zeedfile_path(zeedfile_name), 'r') as f:
            return f.read()
    
    def get_main_zeedfile_content(self) -> str:
        return self.get_zeedfile_content(self._main_zeedfile_name)