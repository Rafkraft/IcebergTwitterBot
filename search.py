import json
import tweepy

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


ckey ='EgLx9a2h748H0r5zH1zSshdRY'
csecret ='C06Xesjs1S23X8ClP1Q9BiCNIAXCRBAEia139uSXyymCmvjZiA'
atoken ='136394046-GmTHewzpiWVh42IkUebTQ7rOSrQt1V4P8aJxsyaH'
asecret ='MSsI3f2mLmepyK1qMZ7utzP0nFGBOnUQ9JaGbcEjGWg7d'

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth_handler=auth, parser=tweepy.parsers.JSONParser())

for status in tweepy.Cursor(api.search, q=['tweepy']).items():
    print status

