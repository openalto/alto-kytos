# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class ErrorResponseMeta(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, code: str=None, message: str=None):
        """
        ErrorResponseMeta - a model defined in Swagger

        :param code: The code of this ErrorResponseMeta.
        :type code: str
        :param message: The message of this ErrorResponseMeta.
        :type message: str
        """
        self.swagger_types = {
            'code': str,
            'message': str
        }

        self.attribute_map = {
            'code': 'code',
            'message': 'message'
        }

        self._code = code
        self._message = message

    @classmethod
    def from_dict(cls, dikt) -> 'ErrorResponseMeta':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ErrorResponse_meta of this ErrorResponseMeta.
        :rtype: ErrorResponseMeta
        """
        return deserialize_model(dikt, cls)

    @property
    def code(self) -> str:
        """
        Gets the code of this ErrorResponseMeta.

        :return: The code of this ErrorResponseMeta.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code: str):
        """
        Sets the code of this ErrorResponseMeta.

        :param code: The code of this ErrorResponseMeta.
        :type code: str
        """
        allowed_values = ["E_SYNTAX", "E_MISSING_FIELD", "E_INVALID_FIELD_TYPE", "E_INVALID_FIELD_VALUE"]
        if code not in allowed_values:
            raise ValueError(
                "Invalid value for `code` ({0}), must be one of {1}"
                .format(code, allowed_values)
            )

        self._code = code

    @property
    def message(self) -> str:
        """
        Gets the message of this ErrorResponseMeta.
        Provides the details of the error

        :return: The message of this ErrorResponseMeta.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """
        Sets the message of this ErrorResponseMeta.
        Provides the details of the error

        :param message: The message of this ErrorResponseMeta.
        :type message: str
        """

        self._message = message
