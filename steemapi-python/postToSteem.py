#!/usr/bin/env python
# -*- coding: utf-8 -*-
from steem.post import Post
from steem import Steem
import sys

ENCODING = sys.stdout.encoding if sys.stdout.encoding else 'utf-8'
pk = [sys.argv[4]]
steem = Steem(keys=pk[0], nodes=["https://api.steemit.com"])
tagsarray = sys.argv[5].split(',')
steem.post(sys.argv[1], sys.argv[2], author=sys.argv[3], permlink=sys.argv[4], json_metadata={"app":"steemplace/0.1","tags":tagsarray}, reply_identifier=None, category=None)
print("ok")
