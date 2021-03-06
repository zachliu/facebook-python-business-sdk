# Copyright 2014 Facebook, Inc.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import pprint

import six
from facebook_business.adobjects.serverside.custom_data import CustomData
from facebook_business.adobjects.serverside.user_data import UserData


class Event(object):
    param_types = {
        'event_name': 'str',
        'event_time': 'int',
        'event_source_url': 'str',
        'opt_out': 'bool',
        'event_id': 'str',
        'user_data': 'UserData',
        'custom_data': 'CustomData'
    }

    def __init__(self, event_name: str = None, event_time: int = None, event_source_url: str = None,
                 opt_out: bool = None, event_id: str = None,
                 user_data: UserData = None, custom_data: CustomData = None):
        """Server-Side Event"""
        self._event_name = None
        self._event_time = None
        self._event_source_url = None
        self._opt_out = None
        self._event_id = None
        self._user_data = None
        self._custom_data = None
        self.event_name = event_name
        self.event_time = event_time
        if event_source_url is not None:
            self.event_source_url = event_source_url
        if opt_out is not None:
            self.opt_out = opt_out
        if event_id is not None:
            self.event_id = event_id
        if user_data is not None:
            self.user_data = user_data
        if custom_data is not None:
            self.custom_data = custom_data

    @property
    def event_name(self):
        """Gets the event_name of this Event.

        A Facebook pixel Standard Event or Custom Event name.

        :return: The event_name of this Event.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name: str):
        """Sets the event_name of this Event.

        A Facebook pixel Standard Event or Custom Event name.

        :param event_name: The event_name of this Event.
        :type: str
        :return self
        """
        if event_name is None:
            raise ValueError("Invalid value for `event_name`, must not be `None`")

        self._event_name = event_name

    @property
    def event_time(self):
        """Gets the event_time of this Event.

        A Unix timestamp in seconds indicating when the actual event occurred.

        :return: The event_time of this Event.
        :rtype: int
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time: int):
        """Sets the event_time of this Event.

        A Unix timestamp in seconds indicating when the actual event occurred.

        :param event_time: The event_time of this Event.
        :type: int
        """
        if event_time is None:
            raise ValueError("Invalid value for `event_time`, must not be `None`")

        if not isinstance(event_time, int):
            raise TypeError('Event.event_time must be an int')

        self._event_time = event_time

    @property
    def event_source_url(self):
        """Gets the event_source_url of this Event.

        The browser URL where the event happened.

        :return: The event_source_url of this Event.
        :rtype: str
        """
        return self._event_source_url

    @event_source_url.setter
    def event_source_url(self, event_source_url: str):
        """Sets the event_source_url of this Event.

        The browser URL where the event happened.

        :param event_source_url: The event_source_url of this Event.
        :type: str
        """

        self._event_source_url = event_source_url

    @property
    def opt_out(self):
        """Gets the opt_out of this Event.

        A flag that indicates we should not use this event for ads delivery optimization.
        If set to true, we only use the event for attribution.

        :return: The opt_out of this Event.
        :rtype: bool
        """
        return self._opt_out

    @opt_out.setter
    def opt_out(self, opt_out: bool):
        """Sets the opt_out of this Event.

        A flag that indicates we should not use this event for ads delivery optimization.
        If set to true, we only use the event for attribution.

        :param opt_out: The opt_out of this Event.
        :type: bool
        """

        if not isinstance(opt_out, bool):
            raise TypeError('Event.opt_out must be a bool')
        self._opt_out = opt_out

    @property
    def event_id(self):
        """Gets the event_id of this Event.

        An ID used by Facebook to deduplicate the same event sent from both server and browser.
         The ID sent by server and browser for a given event should match.
         IDs cannot be reused elsewhere in your application, even with a different event_name or event_time.

        :return: The event_id of this Event.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id: str):
        """Sets the event_id of this Event.

        An ID used by Facebook to deduplicate the same event sent from both server and browser.
        The ID sent by server and browser for a given event should match.
        IDs cannot be reused elsewhere in your application, even with a different event_name or event_time.

        :param event_id: The event_id of this Event.
        :type: str
        """

        self._event_id = event_id

    @property
    def user_data(self):
        """Gets the user_data of this Event.


        :return: The user_data of this Event.
        :rtype: UserData
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data: UserData):
        """Sets the user_data of this Event.


        :param user_data: The user_data of this Event.
        :type: UserData
        """
        if user_data is None:
            raise ValueError("Invalid value for `user_data`, must not be `None`")

        if not isinstance(user_data, UserData):
            raise TypeError('Event.user_Data must be of type UserData')

        self._user_data = user_data

    @property
    def custom_data(self):
        """Gets the custom_data of this Event.


        :return: The custom_data of this Event.
        :rtype: CustomData
        """
        return self._custom_data

    @custom_data.setter
    def custom_data(self, custom_data: CustomData):
        """Sets the custom_data of this Event.


        :param custom_data: The custom_data of this Event.
        :type: CustomData
        """

        if not isinstance(custom_data, CustomData):
            raise TypeError('Event.custom_data must be of type CustomData')

        self._custom_data = custom_data

    def normalize(self):
        normalized_payload = {'event_name': self.event_name, 'event_time': self.event_time,
                              'event_source_url': self.event_source_url, 'opt_out': self.opt_out,
                              'event_id': self.event_id}

        if self.user_data is not None:
            normalized_payload['user_data'] = self.user_data.normalize()

        if self.custom_data is not None:
            normalized_payload['custom_data'] = self.custom_data.normalize()

        normalized_payload: dict = {k: v for k, v in normalized_payload.items() if v is not None}
        return normalized_payload

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.param_types):
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
        if issubclass(Event, dict):
            for key, value in self.items():
                result[key] = value

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

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
