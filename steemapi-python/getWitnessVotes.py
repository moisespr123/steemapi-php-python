#!/usr/bin/env python
# -*- coding: utf-8 -*-
from steem import Steem
import sys

ENCODING = sys.stdout.encoding if sys.stdout.encoding else 'utf-8'
s = Steem(nodes=["https://api.steemit.com"])
account = s.get_account(sys.argv[1])
votes = account["witness_votes"]
votelist = ""
for vote in votes:
	votelist += vote + ","
print(votelist)
