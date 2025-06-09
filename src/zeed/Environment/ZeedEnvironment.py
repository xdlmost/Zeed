from zeed.Environment import ExecuteEnvironment, PrepareEnvironment
from zeed.Environment.Base import Base

class ZeedEnvironment(Base):
    """ZeedEnvironment, inherits from Base"""

    def __init__(self):
        super().__init__()
        self.PrepareEnvironment = PrepareEnvironment()
        self.ExecuteEnvironment = ExecuteEnvironment()

    def _get_environment_globals(self) -> dict:
        globals = {}
        globals.update(self.PrepareEnvironment._get_prepare_environment_globals())
        globals.update(self.ExecuteEnvironment._get_execute_environment_globals())
        print(globals)
        return globals