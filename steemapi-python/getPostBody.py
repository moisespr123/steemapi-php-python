#!/usr/bin/env python
# -*- coding: utf-8 -*-
from steem import Steem
import sys

ENCODING = sys.stdout.encoding if sys.stdout.encoding else 'utf-8'
s = Steem(nodes=["https://api.steemit.com"])
author,permlink=sys.argv[1].split("/")
post = s.get_content(author,permlink)
posttext = post["body"]
print (posttext)
