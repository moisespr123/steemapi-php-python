from piston import Steem
import sys

pk = [sys.argv[6]]
steem = Steem(keys=pk[0], node="wss://node.steem.place")
tagsarray = sys.argv[5].split(',')
steem.post(sys.argv[1], sys.argv[2], author=sys.argv[3], permlink=sys.argv[4], meta={"app":"steemplace/0.1","tags":tagsarray}, reply_identifier=None, category=None, tags=tagsarray)
print("ok")
