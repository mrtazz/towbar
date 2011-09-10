==============
towbar
==============

Introduction
=============
towbar is a python library for the boxcar.io_ web service.

Installation
=============
Install via pip::

    pip install towbar

Or if you must::

    easy_install towbar


Usage
======
towbar can be imported into any python module::

    from towbar import Towbar
    tow_bar = Towbar(user, password)

The object then provides the following API methods::

    tow_bar.notify_myself(message, sender)

There is also an exported API function which can be used directly::

    import towbar
    towbar.send_notification(user, password, text)

Dependencies
=============
* `python-requests <http://python-requests.org>`_

TODO
=====
* Full API support
* Provider support
* Integration testing

Meta
======
* `Bugs <https://github.com/mrtazz/towbar/issues>`_
* `Continuous Integration <http://ci.unwiredcouch.com/job/towbar-master>`_
* `Docs <http://readthedocs.org/docs/towbar/en/latest/api.html>`_

Contribute
===========
If you want to contribute:

* Fork the project.
* Make your feature addition or bug fix based on develop.
* Add tests for it. This is important so I don’t break it in a future version unintentionally.
* Commit, do not mess with version
* Send me a pull request. Bonus points for topic branches.

.. _boxcar.io: http://boxcar.io
