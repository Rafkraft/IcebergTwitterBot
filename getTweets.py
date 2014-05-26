import json

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


ckey ='EgLx9a2h748H0r5zH1zSshdRY'
csecret ='C06Xesjs1S23X8ClP1Q9BiCNIAXCRBAEia139uSXyymCmvjZiA'
atoken ='136394046-GmTHewzpiWVh42IkUebTQ7rOSrQt1V4P8aJxsyaH'
asecret ='MSsI3f2mLmepyK1qMZ7utzP0nFGBOnUQ9JaGbcEjGWg7d'

looking_for = 'TousUnisContreLeFN'


class listener(StreamListener):
    def on_data(self, data):
        jsonData = json.loads(data)

        #print jsonData

        hashtags = jsonData['entities']['hashtags']

        has_hashtag = False

        for hashtag in hashtags:
            if looking_for in hashtag['text']:
                has_hashtag = True

        if has_hashtag:
            print "GOOOOD"
        else:
            print "BADDD"

        return True

    def on_error(self,status):
        print status

auth=OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)


def getTweet():
    twitterStream = Stream(auth, listener())
    twitterStream.filter(track=[looking_for])

if __name__ == '__main__':
    getTweet()

