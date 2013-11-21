#!/bin/bash

set -e

DEST=$1


[ "$DEST" ] || exit 1


GWL=`batctl gwl -n`

SELF=`echo "$GWL" | head -n 1 | sed -r -e 's@^.*MainIF/MAC: [^/]+/([0-9a-f:]+).*$@\1@'`
GWS=`(echo "$GWL" | tail -n +2 | grep -v '^No' | sed 's/=>//' | awk '{ print $1 }') | while read a; do echo -n "-g $a "; done`

if [ `cat /sys/class/net/bat0/mesh/gw_mode` = server ]; then
    GWS="$GWS -g $SELF"
fi

"$(dirname "$0")"/ffhlwiki.py http://freifunk.metameute.de/wiki/Knoten > "$(dirname "$0")"/aliases_hl.json
"$(dirname "$0")"/ffhlwiki.py http://freifunk.metameute.de/wiki/Moelln:Knoten > "$(dirname "$0")"/aliases_moelln.json

batctl vd json -n | "$(dirname "$0")"/bat2nodes.py -a "$(dirname "$0")"/aliases.json -a aliases_hl.json -a aliases_moelln.json -d $DEST $GWS -

mv $DEST/nodes.json.new $DEST/nodes.json

