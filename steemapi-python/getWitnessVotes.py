#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pistonapi.steemnoderpc import SteemNodeRPC
from piston import Steem
import sys

ENCODING = sys.stdout.encoding if sys.stdout.encoding else 'utf-8'
from piston.account import Account
from piston import Steem
steem = Steem(node="wss://node.steem.place")
account = Account(sys.argv[1], steem_instance=steem)
votes = account["witness_votes"]
votelist = ""
for vote in votes:
	votelist += vote + ","
print(votelist)
