 # Twitter Web Services
import tweepy

consumer_key = "Cajrzfezq48l9kA9P2xM51uBY"
consumer_secret ="Mpyjm9F6AfGDtOUkBMJrE4YyYi8OJKzHNtDhc10bzD5Q2bEqqO"
access_token = "foobar"
access_secret = "foolisha"



try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print 'Error! Failed to get request token.'

session.set('request_token', (auth.request_token.key,
auth.request_token.secret))

verifier = raw_input('Verifier:')

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
token = session.get('request_token')
session.delete('request_token')
auth.set_request_token(token[0], token[1])

try:
    auth.get_access_token(verifier)
except tweepy.TweepError:
    print 'Error! Failed to get access token.'



tweets = api.search(q='#python')

#display results
for t in tweets:
    print t.created_at, t.text, "\n"
