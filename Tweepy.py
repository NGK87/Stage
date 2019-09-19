import tweepy

#my user credential in order to access TWITTER API
consumer_key = "mFBcbp8mZkZlEVAFcarY0JQEv"
consumer_secret = "hhuzxiV1EZQOc4sY9e5qhzFOxHauC8s5ydaxQER2NLqwwhtcGm"
access_token = "624059394-D881rOiRH0xTpkrP2SxOZor09jOiV6m1NFtYSMZM"
access_token_secret = "moT59pM1dNi0GxRuUNXR9O1tddU0Wd2uCTYT4T9wYtvu3"

#Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#Create API Object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True) #add wait_on_rate_limit=True, wait_on_rate_limit_notify=True

public_tweets = api.search(q="natixis AND (negatif OR frein OR violence OR plus OR teletravail OR stress OR violences \
OR insultes OR menaces OR agressions OR troubles OR anxiété OR dépression OR burnout OR boreout OR épuisement OR suicide\
OR irritabilité OR nervosité OR fatigue OR palpitations OR hostile OR risque OR déséquilibre OR harcèlement OR démuni \
OR éreinté OR mal-être OR difficultés OR répit OR frustration OR suicidaire OR panique OR anti-dépresseur \
 OR autodestruction OR mourir OR isolement ) -RT", lang="fr", count=10) #rpp=10 10 tweets return per page

# Results
for tweet in public_tweets:
    #print(tweet.text)
    print(f"{tweet.user.name}:{tweet.text}")