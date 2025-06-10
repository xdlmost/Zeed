from pathlib import Path
from typing import List

class FileSystem:
    """File system class for Zeed"""

    @staticmethod
    def get_absolute_path(path: str) -> str:
        return str(Path(path).absolute())

    @staticmethod
    def is_absolute_path(path: str) -> bool:
        """
        Check if the given path is absolute
        
        Args:
            path: Path string to check
            
        Returns:
            bool: True if path is absolute, False otherwise
        """
        return Path(path).is_absolute()
    
        

    @staticmethod
    def exists(path: str) -> bool:
        """
        Check if path exists
        
        Args:
            path: Path to check
            
        Returns:
            bool: True if path exists, False otherwise
        """
        return Path(path).exists()
        
    @staticmethod
    def is_file(path: str) -> bool:
        """
        Check if path is a regular file
        
        Args:
            path: Path to check
            
        Returns:
            bool: True if path is a regular file, False otherwise
        """
        return Path(path).is_file()
        
    @staticmethod
    def is_dir(path: str) -> bool:
        """
        Check if path is a directory
        
        Args:
            path: Path to check
            
        Returns:
            bool: True if path is a directory, False otherwise
        """
        return Path(path).is_dir()
        

    @staticmethod
    def is_symlink(path: str) -> bool:
        """
        Check if path is a symbolic link
        
        Args:
            path: Path to check
            
        Returns:
            bool: True if path is a symbolic link, False otherwise
        """
        return Path(path).is_symlink()
        

    @staticmethod
    def get_mode(path: str) -> int:
        """
        Get file mode (permissions)
        
        Args:
            path: Path to file
            
        Returns:
            int: File mode in octal format
        """
        return Path(path).stat().st_mode
        

    @staticmethod
    def get_owner(path: str) -> str:
        """
        Get file owner username
        
        Args:
            path: Path to file
            
        Returns:
            str: Username of file owner
        """
        import pwd
        return pwd.getpwuid(Path(path).stat().st_uid).pw_name
        

    @staticmethod
    def get_group(path: str) -> str:
        """
        Get file group name
        
        Args:
            path: Path to file
            
        Returns:
            str: Group name of file
        """
        import grp
        return grp.getgrgid(Path(path).stat().st_gid).gr_name
    
    @staticmethod
    def get_path_dir(path: str) -> str:
        return str(Path(path).parent)
    
    @staticmethod
    def get_path_file_name(path: str) -> str:
        return str(Path(path).name)
    
    @staticmethod
    def split_path(path: str) -> List[str]:
        return path.split(Path.sep)
    

class FS:
    """File system class for Zeed"""
    
    
    def __init__(self, work_dir: str):
        self._work_dir = Path(work_dir)

    def to_absolute_path(self, path: str) -> str: 
        if FileSystem.is_absolute_path(path):
            return path
        else:
            return str(self.get_work_dir() / path)
    
    def get_work_dir(self) -> Path:
        return self._work_dir
    
    
    def get_file_content_str(self, file_name: str) -> str:
        with open(self.to_absolute_path(file_name), 'r') as f:
            return f.read()

    def get_file_content_bytes(self, file_name: str) -> bytes:
        with open(self.to_absolute_path(file_name), 'rb') as f:
            return f.read()


    