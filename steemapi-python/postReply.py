#!/usr/bin/env python
# -*- coding: utf-8 -*-
from piston.post import Post
from piston import Steem
import sys

ENCODING = sys.stdout.encoding if sys.stdout.encoding else 'utf-8'
pk = [sys.argv[4]]
steem = Steem(keys=pk[0], node="wss://node.steem.place")
postToComment = Post(sys.argv[1], steem)
texto = sys.argv[2]
cuenta = sys.argv[3]
postToComment.reply(body=texto, author=cuenta)
print("ok")