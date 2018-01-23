#!/usr/bin/env python
# -*- coding: utf-8 -*-
from steem import Steem
import sys
import json
ENCODING = sys.stdout.encoding if sys.stdout.encoding else 'utf-8'
s = Steem(nodes=["https://api.steemit.com"])
author,permlink=sys.argv[1].split("/")
post = s.get_content(author,permlink)
posttext = post["active_votes"]
users = ""
for voters in posttext:
	users +=voters["voter"] + ","
print(users)