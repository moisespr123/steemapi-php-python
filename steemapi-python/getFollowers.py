#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pistonapi.steemnoderpc import SteemNodeRPC
from piston import Steem
import sys

ENCODING = sys.stdout.encoding if sys.stdout.encoding else 'utf-8'
ws = SteemNodeRPC("wss://steemd.steemit.com", "", "", apis=["follow"])
followers = ws.get_follow_count(sys.argv[1], '', 'blog', 1000, api='follow')
print(followers['follower_count'])
