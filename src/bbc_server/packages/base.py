from abc import ABC, abstractmethod, ABCMeta
from typing import ClassVar
import json


class EnsurePackageType(ABCMeta):
    def __init__(cls, name, bases, namespace):
        super().__init__(name, bases, namespace)
        if cls.__name__ != 'BasePackage' and 'PACKAGE_TYPE' not in cls.__dict__:
            raise NotImplementedError("Packages must set PACKAGE_TYPE class var")


class BasePackage(metaclass=EnsurePackageType):

    @abstractmethod
    def _generate_body_dict(self) -> dict:
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


