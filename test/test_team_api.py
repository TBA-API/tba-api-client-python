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
from tbaapiv3client.api.team_api import TeamApi  # noqa: E501
from tbaapiv3client.rest import ApiException


class TestTeamApi(unittest.TestCase):
    """TeamApi unit test stubs"""

    def setUp(self):
        self.api = tbaapiv3client.api.team_api.TeamApi()  # noqa: E501

    def tearDown(self):
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

    def test_get_event_teams(self):
        """Test case for get_event_teams

        """
        pass

    def test_get_event_teams_keys(self):
        """Test case for get_event_teams_keys

        """
        pass

    def test_get_event_teams_simple(self):
        """Test case for get_event_teams_simple

        """
        pass

    def test_get_event_teams_statuses(self):
        """Test case for get_event_teams_statuses

        """
        pass

    def test_get_team(self):
        """Test case for get_team

        """
        pass

    def test_get_team_awards(self):
        """Test case for get_team_awards

        """
        pass

    def test_get_team_awards_by_year(self):
        """Test case for get_team_awards_by_year

        """
        pass

    def test_get_team_districts(self):
        """Test case for get_team_districts

        """
        pass

    def test_get_team_event_awards(self):
        """Test case for get_team_event_awards

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

    def test_get_team_event_status(self):
        """Test case for get_team_event_status

        """
        pass

    def test_get_team_events(self):
        """Test case for get_team_events

        """
        pass

    def test_get_team_events_by_year(self):
        """Test case for get_team_events_by_year

        """
        pass

    def test_get_team_events_by_year_keys(self):
        """Test case for get_team_events_by_year_keys

        """
        pass

    def test_get_team_events_by_year_simple(self):
        """Test case for get_team_events_by_year_simple

        """
        pass

    def test_get_team_events_keys(self):
        """Test case for get_team_events_keys

        """
        pass

    def test_get_team_events_simple(self):
        """Test case for get_team_events_simple

        """
        pass

    def test_get_team_events_statuses_by_year(self):
        """Test case for get_team_events_statuses_by_year

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

    def test_get_team_media_by_tag(self):
        """Test case for get_team_media_by_tag

        """
        pass

    def test_get_team_media_by_tag_year(self):
        """Test case for get_team_media_by_tag_year

        """
        pass

    def test_get_team_media_by_year(self):
        """Test case for get_team_media_by_year

        """
        pass

    def test_get_team_robots(self):
        """Test case for get_team_robots

        """
        pass

    def test_get_team_simple(self):
        """Test case for get_team_simple

        """
        pass

    def test_get_team_social_media(self):
        """Test case for get_team_social_media

        """
        pass

    def test_get_team_years_participated(self):
        """Test case for get_team_years_participated

        """
        pass

    def test_get_teams(self):
        """Test case for get_teams

        """
        pass

    def test_get_teams_by_year(self):
        """Test case for get_teams_by_year

        """
        pass

    def test_get_teams_by_year_keys(self):
        """Test case for get_teams_by_year_keys

        """
        pass

    def test_get_teams_by_year_simple(self):
        """Test case for get_teams_by_year_simple

        """
        pass

    def test_get_teams_keys(self):
        """Test case for get_teams_keys

        """
        pass

    def test_get_teams_simple(self):
        """Test case for get_teams_simple

        """
        pass


if __name__ == '__main__':
    unittest.main()