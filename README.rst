Django Google Contact Importer
==============================

This application wraps Google Contact API, using AuthSub, and provides easy
access to contacts of a Google user. Its primary usage is for writing
"Invite Your Friends" like functionality.

Installation:

* Install gdata.py_ 
* Install ElementTree_
* Put dgci folder somewhere in PYTHONPATH
* Add dgci to settings.py under INSTALLED_APPS
* (r'^dgci/', include('dgci.urls')), into urls.py

Usage:

* Point user to /dgci/start/?next=YourURL

It will store the addressbook into requset.session["dgci_contact_feed"] and
then redirect users to YourURL once addressbook has been imported.

Some examples of how to work with dgci_contact_feed_ object.

Enjoy!

.. _gdata.py: http://code.google.com/p/gdata-python-client/downloads/list
.. _ElementTree: http://pypi.python.org/pypi/elementtree/
.. _dgci_contact_feed: http://code.google.com/apis/contacts/docs/1.0/developers_guide_python.html#Retrieving
