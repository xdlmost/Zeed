
from zeed.Environment import ZeedEnvironment
from .Utils.FileSystem import FileSystem

class Node:
    """Base class for Zeed nodes"""
    
    def __init__(self, zeed_file_path: str):
        absolute_zeed_file_path = FileSystem.get_absolute_path(zeed_file_path)
        if not FileSystem.exists(absolute_zeed_file_path):
            raise FileNotFoundError(f"Zeed file not found: {absolute_zeed_file_path}")  
          
        self.zeed_environment = ZeedEnvironment(absolute_zeed_file_path)

    def prepare(self):
        return self.zeed_environment.prepare()
    
    def execute(self):
        return self.zeed_environment.execute()
    
        # main_zeedfile_content = self.fs.get_main_zeedfile_content()
        # compile_code = compile(main_zeedfile_content, '<string>', 'exec')
        # gVars = self.zeed_environment._get_environment_globals()
        # exec(compile_code, gVars)

        # print(FileSystem.exists(self.zeed_environment.ExecuteEnvironment.INSTALL_CACHE_DIR))
        # print(FileSystem.exists(self.fs.to_absolute_path(self.zeed_environment.ExecuteEnvironment.PACKAGE_OUTPUT_DIR)))
