# -*- coding: utf-8 -*-
"""
    towbar
    ~~~~~~~~~~~~~~

    Python library for accessing the boxcar API

    :copyright: (c) 2011 by Daniel Schauenberg
    :license: MIT, see LICENSE for more details.
"""

import requests
import time

class Towbar(object):
    """ Class for interacting with the boxcar web service """

    def __init__(self, username, password):
        """ object constructor """
        self.auth = (username, password)
        self.url = "https://boxcar.io/notifications"

    def notify_myself(self, message='', sender='towbar', source_url=None,
                      icon_url=None, sound=None, callback=None):
        """ method to send a notification to yourself

        Arguments:
            - sender (string): sender of the message
            - message (string): message to send
            - sender: sender of this message
            - source_url: the source URL for the notification
            - icon_url: URL for the icon to use
            - sound: name of the sound to use
            - callback: JSONP callback

        Returns:
            - response (requests response): response from the requests call

        """
        # build up data
        data = {"notification[from_screen_name]": sender,
                "notification[message]": message,
                "notification[from_remote_service_id]": int(time.time())}
        if source_url:
            data["notification[source_url]"] = source_url
        if icon_url:
            data["notification[icon_url]"] = icon_url
        if sound:
            data["notification[sound]"] = sound
        if callback:
            data["callback"] = callback

        return requests.post(self.url, auth=self.auth, data=data)

