# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""eveapi_simple.py: simple eve api query helper"""

from httplib import HTTPSConnection
from urlparse import urlunsplit
from urllib import urlencode
from lxml import objectify


class APIError(Exception):
    pass


def query(query, args):
    """Query the eve online API and return a result object."""
    query = _make_query_string(query, args)
    con = HTTPSConnection('api.eveonline.com')
    con.request('GET', query)
    response = con.getresponse()
    if response.status != 200:
        raise APIError("HTTPS GET failed")
    return objectify.fromstring(response.read())


def _make_query_string(query, args):
    if not query.startswith('/'):
        query = '/' + query
    if not query.endswith(".xml.aspx"):
        query += '.xml.aspx'
    return urlunsplit(('', '', query, urlencode(args), ''))
