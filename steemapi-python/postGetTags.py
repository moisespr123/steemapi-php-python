#!/usr/bin/env python
# -*- coding: utf-8 -*-
from piston import Steem
import sys

ENCODING = sys.stdout.encoding if sys.stdout.encoding else 'utf-8'
steem = Steem(node="wss://node.steem.place")
post = steem.get_post(sys.argv[1])
tagstring = ""
for tag in post["tags"]:
	if not tag == tagstring[:-1]:
		tagstring += tag + ","
print(tagstring[:-1])
