from bbc_server.packages import BasePackage

class StatusUpdatePackage(BasePackage):
    PACKAGE_TYPE = "status-update"

    def __init__(self, is_ready: bool):
        self.__is_ready = is_ready

    def _generate_body_dict(self) -> dict:
        return {"is-ready": self.__is_ready}

    @property
    def is_ready(self) -> bool:
        return self.__is_ready
    
