import json
import tweepy
# import twitter

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
# from twitter import Twitter


ckey ='EgLx9a2h748H0r5zH1zSshdRY'
csecret ='C06Xesjs1S23X8ClP1Q9BiCNIAXCRBAEia139uSXyymCmvjZiA'
atoken ='136394046-GmTHewzpiWVh42IkUebTQ7rOSrQt1V4P8aJxsyaH'
asecret ='MSsI3f2mLmepyK1qMZ7utzP0nFGBOnUQ9JaGbcEjGWg7d'

auth=OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
api = tweepy.API(auth)



def analyseTweet(tweet):

    length =  len(tweet.entities['hashtags']);
    size = False
    url = False

    

    for hashtag in tweet.entities['hashtags']:
        if hashtag['text'][0] == 'T' or hashtag['text'][0] == 't':
            size =  hashtag['text'].split('_')
            size = size[1]

    print size

    if size:
        api.update_status('Votre achat a ete enregistre, taille %s'%(size),tweet.id)
    else:
        api.update_status('Votre achat a ete enregistre',tweet.id)
        print 'ok'


    parent_id = tweet.in_reply_to_status_id

    parent_status = api.get_status(str(parent_id))


    print parent_status

    product_url = False

    for url in parent_status.entities['urls']:
        link = url['expanded_url']
        if 'modizy.com' in link:
            product_url = link

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
            print jsonData['text']
            analyseTweet(jsonData)
        else:
            print "BADDD"

        return True

    def on_error(self,status):
        print status



#status = twitter.showStatus(id="112652479837110273")
#print status['text']

def getTweet(search_term, periods = 60*60*24):
    results = api.search(q=search_term, rpp=periods)
    #json_results = json.loads(results)

    for tweet in results:
        # print tweet.entities['hashtags']
        # print tweet.text
        print '1 tweet'
        analyseTweet(tweet)

    return results


def listenToTweets(search_term):
    twitterStream = Stream(auth, listener())
    twitterStream.filter(track=[search_term])

    return True


if __name__ == '__main__':
    looking_for = '#Modizy_bot'

    listenToTweets(looking_for)
    #getTweet(looking_for)








