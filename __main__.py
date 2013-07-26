#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""corplist.py: generate character list from corp name"""

from sys import argv
import operator

import eveapi_simple as api
import evewho


corpname = 'EVE University' if len(argv) <= 1 else argv[1]

result_object = api.query('/eve/CharacterID', {'names': corpname})
corpid = result_object.result.rowset.row.attrib['characterID']

characters = evewho.corpmembers(corpid)

print('<table>')

for item in sorted(characters.iteritems(), key=operator.itemgetter(1)):
    charid, charname = item

    print('\t<tr>')
    print('\t\t<td>%s</td>' % charname)
    print('\t\t<td><a href="http://evewho.com/pilot/%s">evewho</a></td>' %
          charname)
    print('\t\t<td class="igblink" onclick="CCPEVE.showInfo(1377, ''%s)">'
          'showinfo</td>' % charid)
    print('\t\t<td class="igblink" onclick="CCPEVE.addContact(''%s)">'
          'watchlist</a></td>' % charid)
    print('\t</tr>')

print('</table>')