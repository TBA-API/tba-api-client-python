# coding: utf-8

"""
    The Blue Alliance API v3

    # Overview    Information and statistics about FIRST Robotics Competition teams and events.   # Authentication   All endpoints require an Auth Key to be passed in the header `X-TBA-Auth-Key`. If you do not have an auth key yet, you can obtain one from your [Account Page](/account).    A `User-Agent` header may need to be set to prevent a 403 Unauthorized error.  # noqa: E501

    The version of the OpenAPI document: 3.5
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class EventDistrictPointsTiebreakers(object):
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
        'highest_qual_scores': 'list[int]',
        'qual_wins': 'int'
    }

    attribute_map = {
        'highest_qual_scores': 'highest_qual_scores',
        'qual_wins': 'qual_wins'
    }

    def __init__(self, highest_qual_scores=None, qual_wins=None):  # noqa: E501
        """EventDistrictPointsTiebreakers - a model defined in OpenAPI"""  # noqa: E501

        self._highest_qual_scores = None
        self._qual_wins = None
        self.discriminator = None

        if highest_qual_scores is not None:
            self.highest_qual_scores = highest_qual_scores
        if qual_wins is not None:
            self.qual_wins = qual_wins

    @property
    def highest_qual_scores(self):
        """Gets the highest_qual_scores of this EventDistrictPointsTiebreakers.  # noqa: E501


        :return: The highest_qual_scores of this EventDistrictPointsTiebreakers.  # noqa: E501
        :rtype: list[int]
        """
        return self._highest_qual_scores

    @highest_qual_scores.setter
    def highest_qual_scores(self, highest_qual_scores):
        """Sets the highest_qual_scores of this EventDistrictPointsTiebreakers.


        :param highest_qual_scores: The highest_qual_scores of this EventDistrictPointsTiebreakers.  # noqa: E501
        :type: list[int]
        """

        self._highest_qual_scores = highest_qual_scores

    @property
    def qual_wins(self):
        """Gets the qual_wins of this EventDistrictPointsTiebreakers.  # noqa: E501


        :return: The qual_wins of this EventDistrictPointsTiebreakers.  # noqa: E501
        :rtype: int
        """
        return self._qual_wins

    @qual_wins.setter
    def qual_wins(self, qual_wins):
        """Sets the qual_wins of this EventDistrictPointsTiebreakers.


        :param qual_wins: The qual_wins of this EventDistrictPointsTiebreakers.  # noqa: E501
        :type: int
        """

        self._qual_wins = qual_wins

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
        if not isinstance(other, EventDistrictPointsTiebreakers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
