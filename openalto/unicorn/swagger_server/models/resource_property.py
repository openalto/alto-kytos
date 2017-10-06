# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class ResourceProperty(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, availbw: int=None):
        """
        ResourceProperty - a model defined in Swagger

        :param availbw: The availbw of this ResourceProperty.
        :type availbw: int
        """
        self.swagger_types = {
            'availbw': int
        }

        self.attribute_map = {
            'availbw': 'availbw'
        }

        self._availbw = availbw

    @classmethod
    def from_dict(cls, dikt) -> 'ResourceProperty':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResourceProperty of this ResourceProperty.
        :rtype: ResourceProperty
        """
        return deserialize_model(dikt, cls)

    @property
    def availbw(self) -> int:
        """
        Gets the availbw of this ResourceProperty.

        :return: The availbw of this ResourceProperty.
        :rtype: int
        """
        return self._availbw

    @availbw.setter
    def availbw(self, availbw: int):
        """
        Sets the availbw of this ResourceProperty.

        :param availbw: The availbw of this ResourceProperty.
        :type availbw: int
        """
        if availbw is None:
            raise ValueError("Invalid value for `availbw`, must not be `None`")

        self._availbw = availbw
