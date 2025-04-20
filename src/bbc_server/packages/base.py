from abc import ABC, abstractmethod, ABCMeta
import json


class EnsurePackageType(ABCMeta):
    """helper class for ensuring all packages have a PACKAGE_TYPE and JSON_PARAM_MAP ClassVar

    PACKAGE_TYPE is the name of the package

    JSON_PARAM_MAP maps the JSON section name to the python parameter used for the class
    This is necessary as packet section names are not necessarily valid python argument names

    """
    def __init__(cls, name, bases, namespace):
        super().__init__(name, bases, namespace)
        if cls.__name__ != 'BasePackage' and 'PACKAGE_TYPE' not in cls.__dict__:
            raise NotImplementedError("Packages must set PACKAGE_TYPE class var")
        if cls.__name__ != 'BasePackage' and 'JSON_PARAM_MAP' not in cls.__dict__:
            raise NotImplementedError("Packages must set JSON_PARAM_MAP class var")


class BasePackage(metaclass=EnsurePackageType):
    """base class for all package classes
    """

    @abstractmethod
    def _generate_body_dict(self) -> dict:
        """method for generating the dictionairy representing the body of the package

        Returns:
            dict: the body dict
        """
        pass

    def to_json(self) -> str:
        """serialize package to JSON string

        Returns:
            str
        """
        outer_dict = {
            "type": self.PACKAGE_TYPE,
            "body": self._generate_body_dict()
        }

        return json.dumps(outer_dict)


