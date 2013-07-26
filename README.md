eve-corplist
============

This is a simple script to generate an HTML memberlist of an EVE Online corporation. To get the member list it queries the evewho.com API.

To generate a member list, just execute the script with the corp name as parameter like so:

    python __main__.py "CORPNAME"

or
    
    python eve-corplist "CORPNAME"

from one directory above the one you checked out.

For larger corporations this can take a while since the script has some delays to take load off evewho.com.


Requirements
============

lxml module

Tested on Python 2.7
