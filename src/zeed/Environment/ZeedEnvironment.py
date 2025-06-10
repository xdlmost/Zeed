import json
from zeed.Environment import ExecuteEnvironment, PrepareEnvironment
from zeed.Environment.Base import Base
from zeed.Environment.ENVReader import ENVReader
from zeed.Environment.Zeed import ZeedPackageDesc
from zeed.Utils import Hash, PackageMaker


class ZeedEnvironment(Base):
    """ZeedEnvironment, inherits from Base"""

    def __init__(self, absolute_zeed_file_path: str):
        super().__init__()
        self._prepareEnvironment = PrepareEnvironment(absolute_zeed_file_path)
        self._executeEnvironment = ExecuteEnvironment(absolute_zeed_file_path)

    def _environment(self) -> ExecuteEnvironment:
        return  self._executeEnvironment
    
    def _zeed(self, **kwargs) -> ZeedPackageDesc:
        zeed = ZeedPackageDesc(**kwargs)
        self._prepareEnvironment.zeed_des_list.append(zeed)
        return zeed

    def _get_environment_globals(self) -> dict:
        globals = { 
            "GetDict": self.get_dict,
            "EnsurePythonVersion": self._prepareEnvironment._ensure_python_version,
            "EnsureZeedVersion": self._prepareEnvironment._ensure_zeed_version,
            "Environment": self._environment,
            "Zeed": self._zeed
        }
        globals.update(self._prepareEnvironment._get_prepare_environment_globals())
        globals.update(self._executeEnvironment._get_execute_environment_globals())
        print(globals)
        return globals
    
    def prepare(self):
        zeed_file_content = self._prepareEnvironment.get_zeed_file_content()
        compile_code = compile(zeed_file_content, '<string>', 'exec')
        gVars = self._get_environment_globals()
        try:
            exec(compile_code, gVars)
        except Exception as e:
            print(e)
            raise e
        


    def execute(self):
        self._executeEnvironment.execute()   

    def get_dict(self) -> dict:
        return {
            "prepareEnvironment": self._prepareEnvironment.get_dict(),
            "executeEnvironment": self._executeEnvironment.get_dict()
        }
    
    def get_json(self) -> str:
        return json.dumps(self.get_dict(), indent=4, ensure_ascii=False)
    