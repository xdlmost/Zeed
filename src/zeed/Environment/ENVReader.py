import os
from typing import Optional



class ENVReader:
    """用于读取系统环境变量的通用类"""
    
    ENV_ZEED_INSTALL_CACHE_DIR = "ZEED_INSTALL_CACHE_DIR"
    ENV_ZEED_INSTALL_CACHE_DIR_DEFAULT = os.path.join(os.path.expanduser("~"), ".zeed", "cache")

    ENV_ZEED_INSTALL_DIR = "ZEED_INSTALL_DIR"
    ENV_ZEED_INSTALL_DIR_DEFAULT = os.path.join(os.path.expanduser("~"), ".zeed", "install")

    ENV_ZEED_PACKAGE_OUTPUT_DIR = "ZEED_PACKAGE_OUTPUT_DIR"
    ENV_ZEED_PACKAGE_OUTPUT_DIR_DEFAULT = "package_output"

    @staticmethod
    def get_env(key: str, default: Optional[str] = None) -> Optional[str]:
        """
        获取指定的环境变量值
        
        Args:
            key: 环境变量名称
            default: 默认值,当环境变量不存在时返回此值
            
        Returns:
            str | None: 环境变量的值,如果不存在且未指定默认值则返回None
        """
        return os.getenv(key, default)
    
    @staticmethod
    def set_env(key: str, value: str) -> None:
        """
        设置环境变量
        
        Args:
            key: 环境变量名称
            value: 要设置的值
        """
        os.environ[key] = value
        
    @staticmethod
    def has_env(key: str) -> bool:
        """
        检查环境变量是否存在
        
        Args:
            key: 环境变量名称
            
        Returns:
            bool: 如果环境变量存在返回True,否则返回False
        """
        return key in os.environ
    

