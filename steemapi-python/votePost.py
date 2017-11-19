from piston import Steem
import sys

pk = [sys.argv[4]]
steem = Steem(keys=pk[0], node="wss://node.steem.place")
percent = float(sys.argv[2])
steem.vote(sys.argv[1], percent, voter=sys.argv[3])
print("ok")
