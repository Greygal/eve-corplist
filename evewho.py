# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""evewho.py: query evewho"""

import time
import json
from httplib import HTTPConnection


class APIError(Exception):
    pass


def corpmembers(corpid):
    members = {}
    curpage = 0
    while True:
        page = _corp_page(corpid, curpage)
        if len(page['characters']) == 0:
            break
        for c in page['characters']:
            members[int(c['character_id'])] = str(c['name'])

        # delay a bit every few pages for large corps to
        # save evewho some load
        if curpage % 3 == 0:
            time.sleep(20)
        curpage += 1
    return members

def _corp_page(corpid, pageid):
    con = HTTPConnection('evewho.com')
    con.request('GET', 'http://evewho.com/api.php?type=corplist&id=%s&page=%s'
                       % (corpid, pageid))
    response = con.getresponse()
    if response.status != 200:
        raise APIError("HTTP GET failed")
    content = response.read()
    try:
        result_object = json.loads(content)
    except ValueError:
        # try again in 20s
        time.sleep(20)
        return _corp_page(corpid, pageid)
    return result_object