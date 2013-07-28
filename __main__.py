#!/usr/bin/env python2

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""corplist.py: generate character list from corp name"""

from sys import argv

import eveapi_simple as api
import evewho


if len(argv) <= 1:
    print("please supply corp name as argument")
    exit(1)

corpname = argv[1]

# corp name -> id
result_object = api.query('/eve/CharacterID', {'names': corpname})
corpid = result_object.result.rowset.row.attrib['characterID']

# get character list and sort the result
characters = evewho.corpmembers(corpid)
characters.sort(key=lambda x: (x[0].upper(), x[0].islower()))

# create html output
print('<!DOCTYPE html>')
print('<html>')
print('<head>')
print('<title>%s member list</title>' % corpname)
print('<link rel="stylesheet" type="text/css" href="style.css" />')
print('</head>')
print('<body>')
print('<h1>%s member list</h1>' % corpname)
print('<table>')

for character_info in characters:
    charname, charid = character_info

    print('<tr>')
    print('<td>%s</td>' % charname)
    print('<td><a href="http://evewho.com/pilot/%s">evewho</a></td>' %
          charname)
    print('<td class="igblink" onclick="CCPEVE.showInfo(1377, %s)">'
          'showinfo</td>' % charid)
    print('<td class="igblink" onclick="CCPEVE.addContact(%s)">'
          'watchlist</td>' % charid)
    print('</tr>')

print('</table>')
print('</body>')
print('</html>')
