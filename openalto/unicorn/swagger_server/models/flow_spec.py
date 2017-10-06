# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.ipv4_addr import Ipv4Addr
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class FlowSpec(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, src_ip: Ipv4Addr=None, dst_ip: Ipv4Addr=None):
        """
        FlowSpec - a model defined in Swagger

        :param src_ip: The src_ip of this FlowSpec.
        :type src_ip: Ipv4Addr
        :param dst_ip: The dst_ip of this FlowSpec.
        :type dst_ip: Ipv4Addr
        """
        self.swagger_types = {
            'src_ip': Ipv4Addr,
            'dst_ip': Ipv4Addr
        }

        self.attribute_map = {
            'src_ip': 'srcIP',
            'dst_ip': 'dstIP'
        }

        self._src_ip = src_ip
        self._dst_ip = dst_ip

    @classmethod
    def from_dict(cls, dikt) -> 'FlowSpec':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FlowSpec of this FlowSpec.
        :rtype: FlowSpec
        """
        return deserialize_model(dikt, cls)

    @property
    def src_ip(self) -> Ipv4Addr:
        """
        Gets the src_ip of this FlowSpec.

        :return: The src_ip of this FlowSpec.
        :rtype: Ipv4Addr
        """
        return self._src_ip

    @src_ip.setter
    def src_ip(self, src_ip: Ipv4Addr):
        """
        Sets the src_ip of this FlowSpec.

        :param src_ip: The src_ip of this FlowSpec.
        :type src_ip: Ipv4Addr
        """
        if src_ip is None:
            raise ValueError("Invalid value for `src_ip`, must not be `None`")

        self._src_ip = src_ip

    @property
    def dst_ip(self) -> Ipv4Addr:
        """
        Gets the dst_ip of this FlowSpec.

        :return: The dst_ip of this FlowSpec.
        :rtype: Ipv4Addr
        """
        return self._dst_ip

    @dst_ip.setter
    def dst_ip(self, dst_ip: Ipv4Addr):
        """
        Sets the dst_ip of this FlowSpec.

        :param dst_ip: The dst_ip of this FlowSpec.
        :type dst_ip: Ipv4Addr
        """
        if dst_ip is None:
            raise ValueError("Invalid value for `dst_ip`, must not be `None`")

        self._dst_ip = dst_ip
