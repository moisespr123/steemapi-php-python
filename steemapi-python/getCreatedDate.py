#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pistonapi.steemnoderpc import SteemNodeRPC
from piston import Steem
import sys

ENCODING = sys.stdout.encoding if sys.stdout.encoding else 'utf-8'
ws = SteemNodeRPC("wss://node.steem.place", "", "")
createddate = ws.get_account(sys.argv[1])
print(createddate["created"])
