#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pistonapi.steemnoderpc import SteemNodeRPC
import sys
import json

ENCODING = sys.stdout.encoding if sys.stdout.encoding else 'utf-8'
ws = SteemNodeRPC("wss://steemd.steemit.com", "", "")
followers = ws.get_account(sys.argv[1])
location = json.loads(followers["json_metadata"])
print(location["profile"]["location"])