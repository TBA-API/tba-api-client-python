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
from tbaapiv3client.api.match_api import MatchApi  # noqa: E501
from tbaapiv3client.rest import ApiException


class TestMatchApi(unittest.TestCase):
    """MatchApi unit test stubs"""

    def setUp(self):
        self.api = tbaapiv3client.api.match_api.MatchApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_event_match_timeseries(self):
        """Test case for get_event_match_timeseries

        """
        pass

    def test_get_event_matches(self):
        """Test case for get_event_matches

        """
        pass

    def test_get_event_matches_keys(self):
        """Test case for get_event_matches_keys

        """
        pass

    def test_get_event_matches_simple(self):
        """Test case for get_event_matches_simple

        """
        pass

    def test_get_match(self):
        """Test case for get_match

        """
        pass

    def test_get_match_simple(self):
        """Test case for get_match_simple

        """
        pass

    def test_get_match_timeseries(self):
        """Test case for get_match_timeseries

        """
        pass

    def test_get_team_event_matches(self):
        """Test case for get_team_event_matches

        """
        pass

    def test_get_team_event_matches_keys(self):
        """Test case for get_team_event_matches_keys

        """
        pass

    def test_get_team_event_matches_simple(self):
        """Test case for get_team_event_matches_simple

        """
        pass

    def test_get_team_matches_by_year(self):
        """Test case for get_team_matches_by_year

        """
        pass

    def test_get_team_matches_by_year_keys(self):
        """Test case for get_team_matches_by_year_keys

        """
        pass

    def test_get_team_matches_by_year_simple(self):
        """Test case for get_team_matches_by_year_simple

        """
        pass


if __name__ == '__main__':
    unittest.main()
