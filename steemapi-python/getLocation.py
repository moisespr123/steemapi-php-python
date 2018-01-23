#!/usr/bin/env python
# -*- coding: utf-8 -*-
from steem import Steem
import sys
import json

ENCODING = sys.stdout.encoding if sys.stdout.encoding else 'utf-8'
s = Steem(nodes=["https://api.steemit.com"])
followers = s.get_account(sys.argv[1])
location = json.loads(followers["json_metadata"])
print(location["profile"]["location"])