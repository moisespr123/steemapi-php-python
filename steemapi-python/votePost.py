from steem.blockchain import Blockchain
from steem import Steem
import sys
pk = [sys.argv[4]]
steem = Steem(keys=pk[0], nodes=["https://api.steemit.com"])
percent = float(sys.argv[2])
steem.vote(sys.argv[1], percent, account=sys.argv[3])
print("ok")
