# coding: utf-8

"""
    The Blue Alliance API v3

    # Overview    Information and statistics about FIRST Robotics Competition teams and events.   # Authentication   All endpoints require an Auth Key to be passed in the header `X-TBA-Auth-Key`. If you do not have an auth key yet, you can obtain one from your [Account Page](/account).    A `User-Agent` header may need to be set to prevent a 403 Unauthorized error.  # noqa: E501

    OpenAPI spec version: 3.03.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TeamRobot(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'year': 'int',
        'robot_name': 'str',
        'key': 'str',
        'team_key': 'str'
    }

    attribute_map = {
        'year': 'year',
        'robot_name': 'robot_name',
        'key': 'key',
        'team_key': 'team_key'
    }

    def __init__(self, year=None, robot_name=None, key=None, team_key=None):  # noqa: E501
        """TeamRobot - a model defined in Swagger"""  # noqa: E501

        self._year = None
        self._robot_name = None
        self._key = None
        self._team_key = None
        self.discriminator = None

        self.year = year
        self.robot_name = robot_name
        self.key = key
        self.team_key = team_key

    @property
    def year(self):
        """Gets the year of this TeamRobot.  # noqa: E501

        Year this robot competed in.  # noqa: E501

        :return: The year of this TeamRobot.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this TeamRobot.

        Year this robot competed in.  # noqa: E501

        :param year: The year of this TeamRobot.  # noqa: E501
        :type: int
        """
        if year is None:
            raise ValueError("Invalid value for `year`, must not be `None`")  # noqa: E501

        self._year = year

    @property
    def robot_name(self):
        """Gets the robot_name of this TeamRobot.  # noqa: E501

        Name of the robot as provided by the team.  # noqa: E501

        :return: The robot_name of this TeamRobot.  # noqa: E501
        :rtype: str
        """
        return self._robot_name

    @robot_name.setter
    def robot_name(self, robot_name):
        """Sets the robot_name of this TeamRobot.

        Name of the robot as provided by the team.  # noqa: E501

        :param robot_name: The robot_name of this TeamRobot.  # noqa: E501
        :type: str
        """
        if robot_name is None:
            raise ValueError("Invalid value for `robot_name`, must not be `None`")  # noqa: E501

        self._robot_name = robot_name

    @property
    def key(self):
        """Gets the key of this TeamRobot.  # noqa: E501

        Internal TBA identifier for this robot.  # noqa: E501

        :return: The key of this TeamRobot.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this TeamRobot.

        Internal TBA identifier for this robot.  # noqa: E501

        :param key: The key of this TeamRobot.  # noqa: E501
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def team_key(self):
        """Gets the team_key of this TeamRobot.  # noqa: E501

        TBA team key for this robot.  # noqa: E501

        :return: The team_key of this TeamRobot.  # noqa: E501
        :rtype: str
        """
        return self._team_key

    @team_key.setter
    def team_key(self, team_key):
        """Sets the team_key of this TeamRobot.

        TBA team key for this robot.  # noqa: E501

        :param team_key: The team_key of this TeamRobot.  # noqa: E501
        :type: str
        """
        if team_key is None:
            raise ValueError("Invalid value for `team_key`, must not be `None`")  # noqa: E501

        self._team_key = team_key

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, TeamRobot):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other