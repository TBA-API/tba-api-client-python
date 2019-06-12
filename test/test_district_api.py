# coding: utf-8

"""
    The Blue Alliance API v3

    # Overview    Information and statistics about FIRST Robotics Competition teams and events.   # Authentication   All endpoints require an Auth Key to be passed in the header `X-TBA-Auth-Key`. If you do not have an auth key yet, you can obtain one from your [Account Page](/account).    A `User-Agent` header may need to be set to prevent a 403 Unauthorized error.  # noqa: E501

    The version of the OpenAPI document: 3.04.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import tbaapiv3client
from tbaapiv3client.api.district_api import DistrictApi  # noqa: E501
from tbaapiv3client.rest import ApiException


class TestDistrictApi(unittest.TestCase):
    """DistrictApi unit test stubs"""

    def setUp(self):
        self.api = tbaapiv3client.api.district_api.DistrictApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_district_events(self):
        """Test case for get_district_events

        """
        pass

    def test_get_district_events_keys(self):
        """Test case for get_district_events_keys

        """
        pass

    def test_get_district_events_simple(self):
        """Test case for get_district_events_simple

        """
        pass

    def test_get_district_rankings(self):
        """Test case for get_district_rankings

        """
        pass

    def test_get_district_teams(self):
        """Test case for get_district_teams

        """
        pass

    def test_get_district_teams_keys(self):
        """Test case for get_district_teams_keys

        """
        pass

    def test_get_district_teams_simple(self):
        """Test case for get_district_teams_simple

        """
        pass

    def test_get_districts_by_year(self):
        """Test case for get_districts_by_year

        """
        pass

    def test_get_event_district_points(self):
        """Test case for get_event_district_points

        """
        pass

    def test_get_team_districts(self):
        """Test case for get_team_districts

        """
        pass


if __name__ == '__main__':
    unittest.main()
