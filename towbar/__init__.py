# -*- coding: utf-8 -*-

from towbar import Towbar

__author__ = "Daniel Schauenberg"
__version__ = "0.1.1"
__license__ = "MIT"

def notify_myself(user, password, message='', sender='towbar', source_url=None,
                      icon_url=None, sound=None, callback=None):
    """ exported API function to send notifications

    Arguments (all exptected as strings):
        - user: boxcar username
        - password: boxcar password
        - message: the message to send
        - sender: sender of this message
        - source_url: the source URL for the notification
        - icon_url: URL for the icon to use
        - sound: name of the sound to use
        - callback: JSONP callback

    Returns:
        the requests response object

    """
    return Towbar(user, password).notify_myself(message, sender, source_url,
                                                icon_url, sound, callback)

