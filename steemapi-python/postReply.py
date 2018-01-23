#!/usr/bin/env python
# -*- coding: utf-8 -*-
from steem.post import Post
from steem import Steem
import sys

ENCODING = sys.stdout.encoding if sys.stdout.encoding else 'utf-8'
pk = [sys.argv[4]]
steem = Steem(keys=pk[0], nodes=["https://api.steemit.com"])
postToComment = Post(sys.argv[1], steem)
texto = sys.argv[2]
cuenta = sys.argv[3]
postToComment.reply(body=texto, author=cuenta)
print("ok")