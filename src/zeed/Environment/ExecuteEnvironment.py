from zeed.Environment.Base import Base

class ExecuteEnvironment(Base):
    """准备环境的类,继承自Base"""
    
    def __init__(self):
        super().__init__()
        self.zeeds = []

    def _environment(self) -> 'ExecuteEnvironment' : # type: ignore
        return self
    
    def _zeed(self, zeed: str) -> str:
        self.zeeds.append(zeed)
        return zeed

    def _get_execute_environment_globals(self) -> dict:
        return {
            "Environment": self._environment,
            "Zeed": self._zeed
        }
    
