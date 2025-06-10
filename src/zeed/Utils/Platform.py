import platform

class Platform:
    """平台配置相关的工具类"""

    @staticmethod
    def get_os_name() -> str:
        """
        获取当前平台名称
        
        Returns:
            str: 平台名称,如 'Windows', 'Linux', 'Darwin' 等
        """
        return platform.system()
    
    @staticmethod
    def get_arch() -> str:
        """
        获取当前系统架构
        
        Returns:
            str: 系统架构名称,如'x86_64', 'arm64'等
        """
        return platform.machine()

    @staticmethod
    def get_platform() -> str:
        """
        获取当前平台标识字符串
        
        Returns:
            str: 平台标识字符串,格式为 'os.arch',如 'windows.x86_64', 'linux.arm64' 等
        """
        return f"{Platform.get_os_name().lower()}.{Platform.get_arch().lower()}"