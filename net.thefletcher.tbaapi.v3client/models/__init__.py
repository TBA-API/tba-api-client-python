# coding: utf-8

# flake8: noqa
"""
    The Blue Alliance API v3

    # Overview    Information and statistics about FIRST Robotics Competition teams and events.   # Authentication   All endpoints require an Auth Key to be passed in the header `X-TBA-Auth-Key`. If you do not have an auth key yet, you can obtain one from your [Account Page](/account).    A `User-Agent` header may need to be set to prevent a 403 Unauthorized error.  # noqa: E501

    OpenAPI spec version: 3.03.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from net.thefletcher.tbaapi.v3client.models.api_status import APIStatus
from net.thefletcher.tbaapi.v3client.models.api_status_app_version import APIStatusAppVersion
from net.thefletcher.tbaapi.v3client.models.award import Award
from net.thefletcher.tbaapi.v3client.models.award_recipient import AwardRecipient
from net.thefletcher.tbaapi.v3client.models.district_list import DistrictList
from net.thefletcher.tbaapi.v3client.models.district_ranking import DistrictRanking
from net.thefletcher.tbaapi.v3client.models.district_ranking_event_points import DistrictRankingEventPoints
from net.thefletcher.tbaapi.v3client.models.elimination_alliance import EliminationAlliance
from net.thefletcher.tbaapi.v3client.models.elimination_alliance_backup import EliminationAllianceBackup
from net.thefletcher.tbaapi.v3client.models.elimination_alliance_status import EliminationAllianceStatus
from net.thefletcher.tbaapi.v3client.models.event import Event
from net.thefletcher.tbaapi.v3client.models.event_district_points import EventDistrictPoints
from net.thefletcher.tbaapi.v3client.models.event_district_points_points import EventDistrictPointsPoints
from net.thefletcher.tbaapi.v3client.models.event_district_points_tiebreakers import EventDistrictPointsTiebreakers
from net.thefletcher.tbaapi.v3client.models.event_insights import EventInsights
from net.thefletcher.tbaapi.v3client.models.event_insights_2016 import EventInsights2016
from net.thefletcher.tbaapi.v3client.models.event_insights_2017 import EventInsights2017
from net.thefletcher.tbaapi.v3client.models.event_insights_2018 import EventInsights2018
from net.thefletcher.tbaapi.v3client.models.event_op_rs import EventOPRs
from net.thefletcher.tbaapi.v3client.models.event_predictions import EventPredictions
from net.thefletcher.tbaapi.v3client.models.event_ranking import EventRanking
from net.thefletcher.tbaapi.v3client.models.event_ranking_extra_stats_info import EventRankingExtraStatsInfo
from net.thefletcher.tbaapi.v3client.models.event_ranking_rankings import EventRankingRankings
from net.thefletcher.tbaapi.v3client.models.event_ranking_sort_order_info import EventRankingSortOrderInfo
from net.thefletcher.tbaapi.v3client.models.event_simple import EventSimple
from net.thefletcher.tbaapi.v3client.models.match import Match
from net.thefletcher.tbaapi.v3client.models.match_alliance import MatchAlliance
from net.thefletcher.tbaapi.v3client.models.match_score_breakdown_2015 import MatchScoreBreakdown2015
from net.thefletcher.tbaapi.v3client.models.match_score_breakdown_2015_alliance import MatchScoreBreakdown2015Alliance
from net.thefletcher.tbaapi.v3client.models.match_score_breakdown_2016 import MatchScoreBreakdown2016
from net.thefletcher.tbaapi.v3client.models.match_score_breakdown_2016_alliance import MatchScoreBreakdown2016Alliance
from net.thefletcher.tbaapi.v3client.models.match_score_breakdown_2017 import MatchScoreBreakdown2017
from net.thefletcher.tbaapi.v3client.models.match_score_breakdown_2017_alliance import MatchScoreBreakdown2017Alliance
from net.thefletcher.tbaapi.v3client.models.match_score_breakdown_2018 import MatchScoreBreakdown2018
from net.thefletcher.tbaapi.v3client.models.match_score_breakdown_2018_alliance import MatchScoreBreakdown2018Alliance
from net.thefletcher.tbaapi.v3client.models.match_simple import MatchSimple
from net.thefletcher.tbaapi.v3client.models.match_simple_alliances import MatchSimpleAlliances
from net.thefletcher.tbaapi.v3client.models.match_timeseries_2018 import MatchTimeseries2018
from net.thefletcher.tbaapi.v3client.models.match_videos import MatchVideos
from net.thefletcher.tbaapi.v3client.models.media import Media
from net.thefletcher.tbaapi.v3client.models.team import Team
from net.thefletcher.tbaapi.v3client.models.team_event_status import TeamEventStatus
from net.thefletcher.tbaapi.v3client.models.team_event_status_alliance import TeamEventStatusAlliance
from net.thefletcher.tbaapi.v3client.models.team_event_status_alliance_backup import TeamEventStatusAllianceBackup
from net.thefletcher.tbaapi.v3client.models.team_event_status_playoff import TeamEventStatusPlayoff
from net.thefletcher.tbaapi.v3client.models.team_event_status_rank import TeamEventStatusRank
from net.thefletcher.tbaapi.v3client.models.team_event_status_rank_ranking import TeamEventStatusRankRanking
from net.thefletcher.tbaapi.v3client.models.team_event_status_rank_sort_order_info import TeamEventStatusRankSortOrderInfo
from net.thefletcher.tbaapi.v3client.models.team_robot import TeamRobot
from net.thefletcher.tbaapi.v3client.models.team_simple import TeamSimple
from net.thefletcher.tbaapi.v3client.models.wlt_record import WLTRecord
from net.thefletcher.tbaapi.v3client.models.webcast import Webcast