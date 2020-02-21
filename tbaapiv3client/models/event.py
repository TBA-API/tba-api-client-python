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


class Event(object):
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
        'key': 'str',
        'name': 'str',
        'event_code': 'str',
        'event_type': 'int',
        'district': 'DistrictList',
        'city': 'str',
        'state_prov': 'str',
        'country': 'str',
        'start_date': 'date',
        'end_date': 'date',
        'year': 'int',
        'short_name': 'str',
        'event_type_string': 'str',
        'week': 'int',
        'address': 'str',
        'postal_code': 'str',
        'gmaps_place_id': 'str',
        'gmaps_url': 'str',
        'lat': 'float',
        'lng': 'float',
        'location_name': 'str',
        'timezone': 'str',
        'website': 'str',
        'first_event_id': 'str',
        'first_event_code': 'str',
        'webcasts': 'list[Webcast]',
        'division_keys': 'list[str]',
        'parent_event_key': 'str',
        'playoff_type': 'int',
        'playoff_type_string': 'str'
    }

    attribute_map = {
        'key': 'key',
        'name': 'name',
        'event_code': 'event_code',
        'event_type': 'event_type',
        'district': 'district',
        'city': 'city',
        'state_prov': 'state_prov',
        'country': 'country',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'year': 'year',
        'short_name': 'short_name',
        'event_type_string': 'event_type_string',
        'week': 'week',
        'address': 'address',
        'postal_code': 'postal_code',
        'gmaps_place_id': 'gmaps_place_id',
        'gmaps_url': 'gmaps_url',
        'lat': 'lat',
        'lng': 'lng',
        'location_name': 'location_name',
        'timezone': 'timezone',
        'website': 'website',
        'first_event_id': 'first_event_id',
        'first_event_code': 'first_event_code',
        'webcasts': 'webcasts',
        'division_keys': 'division_keys',
        'parent_event_key': 'parent_event_key',
        'playoff_type': 'playoff_type',
        'playoff_type_string': 'playoff_type_string'
    }

    def __init__(self, key=None, name=None, event_code=None, event_type=None, district=None, city=None, state_prov=None, country=None, start_date=None, end_date=None, year=None, short_name=None, event_type_string=None, week=None, address=None, postal_code=None, gmaps_place_id=None, gmaps_url=None, lat=None, lng=None, location_name=None, timezone=None, website=None, first_event_id=None, first_event_code=None, webcasts=None, division_keys=None, parent_event_key=None, playoff_type=None, playoff_type_string=None, local_vars_configuration=None):  # noqa: E501
        """Event - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._key = None
        self._name = None
        self._event_code = None
        self._event_type = None
        self._district = None
        self._city = None
        self._state_prov = None
        self._country = None
        self._start_date = None
        self._end_date = None
        self._year = None
        self._short_name = None
        self._event_type_string = None
        self._week = None
        self._address = None
        self._postal_code = None
        self._gmaps_place_id = None
        self._gmaps_url = None
        self._lat = None
        self._lng = None
        self._location_name = None
        self._timezone = None
        self._website = None
        self._first_event_id = None
        self._first_event_code = None
        self._webcasts = None
        self._division_keys = None
        self._parent_event_key = None
        self._playoff_type = None
        self._playoff_type_string = None
        self.discriminator = None

        self.key = key
        self.name = name
        self.event_code = event_code
        self.event_type = event_type
        if district is not None:
            self.district = district
        if city is not None:
            self.city = city
        if state_prov is not None:
            self.state_prov = state_prov
        if country is not None:
            self.country = country
        self.start_date = start_date
        self.end_date = end_date
        self.year = year
        if short_name is not None:
            self.short_name = short_name
        self.event_type_string = event_type_string
        if week is not None:
            self.week = week
        if address is not None:
            self.address = address
        if postal_code is not None:
            self.postal_code = postal_code
        if gmaps_place_id is not None:
            self.gmaps_place_id = gmaps_place_id
        if gmaps_url is not None:
            self.gmaps_url = gmaps_url
        if lat is not None:
            self.lat = lat
        if lng is not None:
            self.lng = lng
        if location_name is not None:
            self.location_name = location_name
        if timezone is not None:
            self.timezone = timezone
        if website is not None:
            self.website = website
        if first_event_id is not None:
            self.first_event_id = first_event_id
        if first_event_code is not None:
            self.first_event_code = first_event_code
        if webcasts is not None:
            self.webcasts = webcasts
        if division_keys is not None:
            self.division_keys = division_keys
        if parent_event_key is not None:
            self.parent_event_key = parent_event_key
        if playoff_type is not None:
            self.playoff_type = playoff_type
        if playoff_type_string is not None:
            self.playoff_type_string = playoff_type_string

    @property
    def key(self):
        """Gets the key of this Event.  # noqa: E501

        TBA event key with the format yyyy[EVENT_CODE], where yyyy is the year, and EVENT_CODE is the event code of the event.  # noqa: E501

        :return: The key of this Event.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this Event.

        TBA event key with the format yyyy[EVENT_CODE], where yyyy is the year, and EVENT_CODE is the event code of the event.  # noqa: E501

        :param key: The key of this Event.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and key is None:  # noqa: E501
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def name(self):
        """Gets the name of this Event.  # noqa: E501

        Official name of event on record either provided by FIRST or organizers of offseason event.  # noqa: E501

        :return: The name of this Event.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Event.

        Official name of event on record either provided by FIRST or organizers of offseason event.  # noqa: E501

        :param name: The name of this Event.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def event_code(self):
        """Gets the event_code of this Event.  # noqa: E501

        Event short code, as provided by FIRST.  # noqa: E501

        :return: The event_code of this Event.  # noqa: E501
        :rtype: str
        """
        return self._event_code

    @event_code.setter
    def event_code(self, event_code):
        """Sets the event_code of this Event.

        Event short code, as provided by FIRST.  # noqa: E501

        :param event_code: The event_code of this Event.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and event_code is None:  # noqa: E501
            raise ValueError("Invalid value for `event_code`, must not be `None`")  # noqa: E501

        self._event_code = event_code

    @property
    def event_type(self):
        """Gets the event_type of this Event.  # noqa: E501

        Event Type, as defined here: https://github.com/the-blue-alliance/the-blue-alliance/blob/master/consts/event_type.py#L2  # noqa: E501

        :return: The event_type of this Event.  # noqa: E501
        :rtype: int
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this Event.

        Event Type, as defined here: https://github.com/the-blue-alliance/the-blue-alliance/blob/master/consts/event_type.py#L2  # noqa: E501

        :param event_type: The event_type of this Event.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and event_type is None:  # noqa: E501
            raise ValueError("Invalid value for `event_type`, must not be `None`")  # noqa: E501

        self._event_type = event_type

    @property
    def district(self):
        """Gets the district of this Event.  # noqa: E501


        :return: The district of this Event.  # noqa: E501
        :rtype: DistrictList
        """
        return self._district

    @district.setter
    def district(self, district):
        """Sets the district of this Event.


        :param district: The district of this Event.  # noqa: E501
        :type: DistrictList
        """

        self._district = district

    @property
    def city(self):
        """Gets the city of this Event.  # noqa: E501

        City, town, village, etc. the event is located in.  # noqa: E501

        :return: The city of this Event.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Event.

        City, town, village, etc. the event is located in.  # noqa: E501

        :param city: The city of this Event.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def state_prov(self):
        """Gets the state_prov of this Event.  # noqa: E501

        State or Province the event is located in.  # noqa: E501

        :return: The state_prov of this Event.  # noqa: E501
        :rtype: str
        """
        return self._state_prov

    @state_prov.setter
    def state_prov(self, state_prov):
        """Sets the state_prov of this Event.

        State or Province the event is located in.  # noqa: E501

        :param state_prov: The state_prov of this Event.  # noqa: E501
        :type: str
        """

        self._state_prov = state_prov

    @property
    def country(self):
        """Gets the country of this Event.  # noqa: E501

        Country the event is located in.  # noqa: E501

        :return: The country of this Event.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Event.

        Country the event is located in.  # noqa: E501

        :param country: The country of this Event.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def start_date(self):
        """Gets the start_date of this Event.  # noqa: E501

        Event start date in `yyyy-mm-dd` format.  # noqa: E501

        :return: The start_date of this Event.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this Event.

        Event start date in `yyyy-mm-dd` format.  # noqa: E501

        :param start_date: The start_date of this Event.  # noqa: E501
        :type: date
        """
        if self.local_vars_configuration.client_side_validation and start_date is None:  # noqa: E501
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this Event.  # noqa: E501

        Event end date in `yyyy-mm-dd` format.  # noqa: E501

        :return: The end_date of this Event.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this Event.

        Event end date in `yyyy-mm-dd` format.  # noqa: E501

        :param end_date: The end_date of this Event.  # noqa: E501
        :type: date
        """
        if self.local_vars_configuration.client_side_validation and end_date is None:  # noqa: E501
            raise ValueError("Invalid value for `end_date`, must not be `None`")  # noqa: E501

        self._end_date = end_date

    @property
    def year(self):
        """Gets the year of this Event.  # noqa: E501

        Year the event data is for.  # noqa: E501

        :return: The year of this Event.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this Event.

        Year the event data is for.  # noqa: E501

        :param year: The year of this Event.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and year is None:  # noqa: E501
            raise ValueError("Invalid value for `year`, must not be `None`")  # noqa: E501

        self._year = year

    @property
    def short_name(self):
        """Gets the short_name of this Event.  # noqa: E501

        Same as `name` but doesn't include event specifiers, such as 'Regional' or 'District'. May be null.  # noqa: E501

        :return: The short_name of this Event.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this Event.

        Same as `name` but doesn't include event specifiers, such as 'Regional' or 'District'. May be null.  # noqa: E501

        :param short_name: The short_name of this Event.  # noqa: E501
        :type: str
        """

        self._short_name = short_name

    @property
    def event_type_string(self):
        """Gets the event_type_string of this Event.  # noqa: E501

        Event Type, eg Regional, District, or Offseason.  # noqa: E501

        :return: The event_type_string of this Event.  # noqa: E501
        :rtype: str
        """
        return self._event_type_string

    @event_type_string.setter
    def event_type_string(self, event_type_string):
        """Sets the event_type_string of this Event.

        Event Type, eg Regional, District, or Offseason.  # noqa: E501

        :param event_type_string: The event_type_string of this Event.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and event_type_string is None:  # noqa: E501
            raise ValueError("Invalid value for `event_type_string`, must not be `None`")  # noqa: E501

        self._event_type_string = event_type_string

    @property
    def week(self):
        """Gets the week of this Event.  # noqa: E501

        Week of the event relative to the first official season event, zero-indexed. Only valid for Regionals, Districts, and District Championships. Null otherwise. (Eg. A season with a week 0 'preseason' event does not count, and week 1 events will show 0 here. Seasons with a week 0.5 regional event will show week 0 for those event(s) and week 1 for week 1 events and so on.)  # noqa: E501

        :return: The week of this Event.  # noqa: E501
        :rtype: int
        """
        return self._week

    @week.setter
    def week(self, week):
        """Sets the week of this Event.

        Week of the event relative to the first official season event, zero-indexed. Only valid for Regionals, Districts, and District Championships. Null otherwise. (Eg. A season with a week 0 'preseason' event does not count, and week 1 events will show 0 here. Seasons with a week 0.5 regional event will show week 0 for those event(s) and week 1 for week 1 events and so on.)  # noqa: E501

        :param week: The week of this Event.  # noqa: E501
        :type: int
        """

        self._week = week

    @property
    def address(self):
        """Gets the address of this Event.  # noqa: E501

        Address of the event's venue, if available.  # noqa: E501

        :return: The address of this Event.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Event.

        Address of the event's venue, if available.  # noqa: E501

        :param address: The address of this Event.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def postal_code(self):
        """Gets the postal_code of this Event.  # noqa: E501

        Postal code from the event address.  # noqa: E501

        :return: The postal_code of this Event.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this Event.

        Postal code from the event address.  # noqa: E501

        :param postal_code: The postal_code of this Event.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def gmaps_place_id(self):
        """Gets the gmaps_place_id of this Event.  # noqa: E501

        Google Maps Place ID for the event address.  # noqa: E501

        :return: The gmaps_place_id of this Event.  # noqa: E501
        :rtype: str
        """
        return self._gmaps_place_id

    @gmaps_place_id.setter
    def gmaps_place_id(self, gmaps_place_id):
        """Sets the gmaps_place_id of this Event.

        Google Maps Place ID for the event address.  # noqa: E501

        :param gmaps_place_id: The gmaps_place_id of this Event.  # noqa: E501
        :type: str
        """

        self._gmaps_place_id = gmaps_place_id

    @property
    def gmaps_url(self):
        """Gets the gmaps_url of this Event.  # noqa: E501

        Link to address location on Google Maps.  # noqa: E501

        :return: The gmaps_url of this Event.  # noqa: E501
        :rtype: str
        """
        return self._gmaps_url

    @gmaps_url.setter
    def gmaps_url(self, gmaps_url):
        """Sets the gmaps_url of this Event.

        Link to address location on Google Maps.  # noqa: E501

        :param gmaps_url: The gmaps_url of this Event.  # noqa: E501
        :type: str
        """

        self._gmaps_url = gmaps_url

    @property
    def lat(self):
        """Gets the lat of this Event.  # noqa: E501

        Latitude for the event address.  # noqa: E501

        :return: The lat of this Event.  # noqa: E501
        :rtype: float
        """
        return self._lat

    @lat.setter
    def lat(self, lat):
        """Sets the lat of this Event.

        Latitude for the event address.  # noqa: E501

        :param lat: The lat of this Event.  # noqa: E501
        :type: float
        """

        self._lat = lat

    @property
    def lng(self):
        """Gets the lng of this Event.  # noqa: E501

        Longitude for the event address.  # noqa: E501

        :return: The lng of this Event.  # noqa: E501
        :rtype: float
        """
        return self._lng

    @lng.setter
    def lng(self, lng):
        """Sets the lng of this Event.

        Longitude for the event address.  # noqa: E501

        :param lng: The lng of this Event.  # noqa: E501
        :type: float
        """

        self._lng = lng

    @property
    def location_name(self):
        """Gets the location_name of this Event.  # noqa: E501

        Name of the location at the address for the event, eg. Blue Alliance High School.  # noqa: E501

        :return: The location_name of this Event.  # noqa: E501
        :rtype: str
        """
        return self._location_name

    @location_name.setter
    def location_name(self, location_name):
        """Sets the location_name of this Event.

        Name of the location at the address for the event, eg. Blue Alliance High School.  # noqa: E501

        :param location_name: The location_name of this Event.  # noqa: E501
        :type: str
        """

        self._location_name = location_name

    @property
    def timezone(self):
        """Gets the timezone of this Event.  # noqa: E501

        Timezone name.  # noqa: E501

        :return: The timezone of this Event.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this Event.

        Timezone name.  # noqa: E501

        :param timezone: The timezone of this Event.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def website(self):
        """Gets the website of this Event.  # noqa: E501

        The event's website, if any.  # noqa: E501

        :return: The website of this Event.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this Event.

        The event's website, if any.  # noqa: E501

        :param website: The website of this Event.  # noqa: E501
        :type: str
        """

        self._website = website

    @property
    def first_event_id(self):
        """Gets the first_event_id of this Event.  # noqa: E501

        The FIRST internal Event ID, used to link to the event on the FRC webpage.  # noqa: E501

        :return: The first_event_id of this Event.  # noqa: E501
        :rtype: str
        """
        return self._first_event_id

    @first_event_id.setter
    def first_event_id(self, first_event_id):
        """Sets the first_event_id of this Event.

        The FIRST internal Event ID, used to link to the event on the FRC webpage.  # noqa: E501

        :param first_event_id: The first_event_id of this Event.  # noqa: E501
        :type: str
        """

        self._first_event_id = first_event_id

    @property
    def first_event_code(self):
        """Gets the first_event_code of this Event.  # noqa: E501

        Public facing event code used by FIRST (on frc-events.firstinspires.org, for example)  # noqa: E501

        :return: The first_event_code of this Event.  # noqa: E501
        :rtype: str
        """
        return self._first_event_code

    @first_event_code.setter
    def first_event_code(self, first_event_code):
        """Sets the first_event_code of this Event.

        Public facing event code used by FIRST (on frc-events.firstinspires.org, for example)  # noqa: E501

        :param first_event_code: The first_event_code of this Event.  # noqa: E501
        :type: str
        """

        self._first_event_code = first_event_code

    @property
    def webcasts(self):
        """Gets the webcasts of this Event.  # noqa: E501


        :return: The webcasts of this Event.  # noqa: E501
        :rtype: list[Webcast]
        """
        return self._webcasts

    @webcasts.setter
    def webcasts(self, webcasts):
        """Sets the webcasts of this Event.


        :param webcasts: The webcasts of this Event.  # noqa: E501
        :type: list[Webcast]
        """

        self._webcasts = webcasts

    @property
    def division_keys(self):
        """Gets the division_keys of this Event.  # noqa: E501

        An array of event keys for the divisions at this event.  # noqa: E501

        :return: The division_keys of this Event.  # noqa: E501
        :rtype: list[str]
        """
        return self._division_keys

    @division_keys.setter
    def division_keys(self, division_keys):
        """Sets the division_keys of this Event.

        An array of event keys for the divisions at this event.  # noqa: E501

        :param division_keys: The division_keys of this Event.  # noqa: E501
        :type: list[str]
        """

        self._division_keys = division_keys

    @property
    def parent_event_key(self):
        """Gets the parent_event_key of this Event.  # noqa: E501

        The TBA Event key that represents the event's parent. Used to link back to the event from a division event. It is also the inverse relation of `divison_keys`.  # noqa: E501

        :return: The parent_event_key of this Event.  # noqa: E501
        :rtype: str
        """
        return self._parent_event_key

    @parent_event_key.setter
    def parent_event_key(self, parent_event_key):
        """Sets the parent_event_key of this Event.

        The TBA Event key that represents the event's parent. Used to link back to the event from a division event. It is also the inverse relation of `divison_keys`.  # noqa: E501

        :param parent_event_key: The parent_event_key of this Event.  # noqa: E501
        :type: str
        """

        self._parent_event_key = parent_event_key

    @property
    def playoff_type(self):
        """Gets the playoff_type of this Event.  # noqa: E501

        Playoff Type, as defined here: https://github.com/the-blue-alliance/the-blue-alliance/blob/master/consts/playoff_type.py#L4, or null.  # noqa: E501

        :return: The playoff_type of this Event.  # noqa: E501
        :rtype: int
        """
        return self._playoff_type

    @playoff_type.setter
    def playoff_type(self, playoff_type):
        """Sets the playoff_type of this Event.

        Playoff Type, as defined here: https://github.com/the-blue-alliance/the-blue-alliance/blob/master/consts/playoff_type.py#L4, or null.  # noqa: E501

        :param playoff_type: The playoff_type of this Event.  # noqa: E501
        :type: int
        """

        self._playoff_type = playoff_type

    @property
    def playoff_type_string(self):
        """Gets the playoff_type_string of this Event.  # noqa: E501

        String representation of the `playoff_type`, or null.  # noqa: E501

        :return: The playoff_type_string of this Event.  # noqa: E501
        :rtype: str
        """
        return self._playoff_type_string

    @playoff_type_string.setter
    def playoff_type_string(self, playoff_type_string):
        """Sets the playoff_type_string of this Event.

        String representation of the `playoff_type`, or null.  # noqa: E501

        :param playoff_type_string: The playoff_type_string of this Event.  # noqa: E501
        :type: str
        """

        self._playoff_type_string = playoff_type_string

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
        if not isinstance(other, Event):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Event):
            return True

        return self.to_dict() != other.to_dict()
