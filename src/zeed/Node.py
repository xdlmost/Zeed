
from zeed.Environment import ZeedEnvironment
from .FileSystem import FileSystem

class Node:
    """Base class for Zeed nodes"""
    
    def __init__(self, fs: FileSystem):
        self.fs = fs
        self.zeed_environment = ZeedEnvironment()

    def prepare(self):  
        main_zeedfile_content = self.fs.get_main_zeedfile_content()
        compile_code = compile(main_zeedfile_content, '<string>', 'exec')
        gVars = self.zeed_environment._get_environment_globals()
        exec(compile_code, gVars)
        
