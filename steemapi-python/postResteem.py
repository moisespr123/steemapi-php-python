#!/usr/bin/env python
# -*- coding: utf-8 -*-
from piston.post import Post
from piston import Steem
import sys

ENCODING = sys.stdout.encoding if sys.stdout.encoding else 'utf-8'
pk = [sys.argv[3]]
steem = Steem(keys=pk[0], node="wss://node.steem.place")
steem.resteem(sys.argv[1], account=sys.argv[2])
print("ok")