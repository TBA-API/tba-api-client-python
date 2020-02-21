# coding: utf-8

"""
    The Blue Alliance API v3

    # Overview    Information and statistics about FIRST Robotics Competition teams and events.   # Authentication   All endpoints require an Auth Key to be passed in the header `X-TBA-Auth-Key`. If you do not have an auth key yet, you can obtain one from your [Account Page](/account).    A `User-Agent` header may need to be set to prevent a 403 Unauthorized error.  # noqa: E501

    The version of the OpenAPI document: 3.8.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from tbaapiv3client.configuration import Configuration


class EventRankingExtraStatsInfo(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'precision': 'float',
        'name': 'str'
    }

    attribute_map = {
        'precision': 'precision',
        'name': 'name'
    }

    def __init__(self, precision=None, name=None, local_vars_configuration=None):  # noqa: E501
        """EventRankingExtraStatsInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._precision = None
        self._name = None
        self.discriminator = None

        self.precision = precision
        self.name = name

    @property
    def precision(self):
        """Gets the precision of this EventRankingExtraStatsInfo.  # noqa: E501

        Integer expressing the number of digits of precision in the number provided in `sort_orders`.  # noqa: E501

        :return: The precision of this EventRankingExtraStatsInfo.  # noqa: E501
        :rtype: float
        """
        return self._precision

    @precision.setter
    def precision(self, precision):
        """Sets the precision of this EventRankingExtraStatsInfo.

        Integer expressing the number of digits of precision in the number provided in `sort_orders`.  # noqa: E501

        :param precision: The precision of this EventRankingExtraStatsInfo.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and precision is None:  # noqa: E501
            raise ValueError("Invalid value for `precision`, must not be `None`")  # noqa: E501

        self._precision = precision

    @property
    def name(self):
        """Gets the name of this EventRankingExtraStatsInfo.  # noqa: E501

        Name of the field used in the `extra_stats` array.  # noqa: E501

        :return: The name of this EventRankingExtraStatsInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EventRankingExtraStatsInfo.

        Name of the field used in the `extra_stats` array.  # noqa: E501

        :param name: The name of this EventRankingExtraStatsInfo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EventRankingExtraStatsInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EventRankingExtraStatsInfo):
            return True

        return self.to_dict() != other.to_dict()
