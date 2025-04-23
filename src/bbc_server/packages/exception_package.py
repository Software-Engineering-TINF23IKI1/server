from bbc_server.packages import BasePackage
from typing import Optional

class ExceptionPackage(BasePackage):
    PACKAGE_TYPE = "exception"
    JSON_PARAM_MAP = {
        "name": "name",
        "details": "details"
    }

    def __init__(self, name: str, details: Optional[dict] = None):
        """ExceptionPackage
        see the package documentation for more information

        Args:
            name (str): name of the exception
            details (dict): dict with more information
        """
        self.__name = name
        if not details:
            details = {}
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
    """Wrapper Class for Package Parsing Exceptions

    Args:
        stage (str): package Parsing stage at which exception occured
        details (Optional[dict], optional): additional details. Defaults to None.
    """
    def __init__(self, stage: str, details: Optional[dict] = None):
        if not details:
            details = {}
        details = {
            "stage": stage,
            **details
        }
        super().__init__("PackageParsingException", details)

class InvalidGameCodeExceptionPackage(ExceptionPackage):
    """Wrapper Class for Invalid GameCodes

    Args:
        code (str): the gamecode provided
        details (Optional[dict], optional): additional details. Defaults to None.
    """
    def __init__(self, code: str, details: Optional[dict] = None):
        if not details:
            details = {}
        details = {
            "code": code,
            **details
        }
        super().__init__("InvalidGameCodeException", details)
