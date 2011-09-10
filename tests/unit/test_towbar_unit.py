# -*- coding: utf-8 -*-
import unittest
import os
import sys
import mock
sys.path.append(os.getcwd())
import towbar

class TestTowbar(unittest.TestCase):

    def setUp(self):
        self.t = towbar.Towbar("foo", "bar")

    def tearDown(self):
        pass

    @mock.patch('time.time')
    @mock.patch('requests.post')
    def test_notify_myself_simple(self, mock_requests, mock_time):
        mock_time.return_value = 1
        data = {'notification[from_screen_name]': 'me',
                'notification[message]': 'msg',
                'notification[from_remote_service_id]': 1}
        self.t.notify_myself("msg", "me")
        mock_requests.assert_called_once_with('https://boxcar.io/notifications',
                                              data=data,
                                              auth=("foo", "bar"))

    @mock.patch('time.time')
    @mock.patch('requests.post')
    def test_notify_myself_full(self, mock_requests, mock_time):
        mock_time.return_value = 1
        data = {'notification[from_screen_name]': 'me',
                'notification[message]': 'msg',
                'notification[from_remote_service_id]': 1,
                "notification[source_url]": "source_url",
                "notification[icon_url]": "icon_url",
                "notification[sound]": "sound",
                "callback": "callback"}
        self.t.notify_myself("msg", "me", "source_url", "icon_url", "sound", "callback")
        mock_requests.assert_called_once_with('https://boxcar.io/notifications',
                                              data=data,
                                              auth=("foo", "bar"))

if __name__ == '__main__':
    unittest.main()


