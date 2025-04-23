from bbc_server.packages import BasePackage

class ExceptionPackage(BasePackage):
    PACKAGE_TYPE = "exception"
    JSON_PARAM_MAP = {
        "name": "name",
        "details": "details"
    }

    def __init__(self, name: str, details: dict):
        """ExceptionPackage
        see the package documentation for more information

        Args:
            name (str): name of the exception
            details (dict): dict with more information
        """
        self.__name = name
        self.__details = details

    def _generate_body_dict(self) -> dict:
        dict_repr = {
            "name": self.__name,
            "details": self.__details
        }
        return dict_repr

    @property
    def name(self) -> str:
        return self.__name

    @property
    def details(self) -> dict:
        return self.__details


class PackageParsingExceptionPackage(ExceptionPackage):
    """Wrapper Class for Package Parsing Exceptions"""
    def __init__(self, stage: str, details: dict):
        details = {
            "stage": stage,
            **details
        }
        super().__init__("PackageParsingException", details)
