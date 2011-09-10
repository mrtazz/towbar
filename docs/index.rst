.. simplenote.py documentation master file, created by
   sphinx-quickstart on Sat Jun 25 17:40:25 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

towbar: python API wrapper for boxcar.io
=========================================================

Contents:

.. toctree::
   :maxdepth: 2

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


Quickstart
-----------
towbar is a python library for the boxcar.io_ web service.
It can be imported into any python module::

    from towbar import Towbar
    tow_bar = Towbar(user, password)

The object then provides the following API methods::

    tow_bar.notify_myself(message, sender)

There is also an exported API function which can be used directly::

    import towbar
    towbar.send_notification(user, password, text)

API Reference
-------------

If you are looking for information on a specific function, class or
method, you can most likely find it here.

.. toctree::
   :maxdepth: 2

   api


.. _boxcar.io: http://boxcar.io

