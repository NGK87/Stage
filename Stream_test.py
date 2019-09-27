import tweepy
import csv

# my user credential in order to access TWITTER API
consumer_key = "mFBcbp8mZkZlEVAFcarY0JQEv"
consumer_secret = "hhuzxiV1EZQOc4sY9e5qhzFOxHauC8s5ydaxQER2NLqwwhtcGm"
access_token = "624059394-D881rOiRH0xTpkrP2SxOZor09jOiV6m1NFtYSMZM"
access_token_secret = "moT59pM1dNi0GxRuUNXR9O1tddU0Wd2uCTYT4T9wYtvu3"

# Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API Object
api = tweepy.API(auth)


# ----------------------------------------------------------------------------------------------------------------------
# api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
# wait_on_rate_limit_notify=True : the api will automatically or not wait for rate limits to replenish
# wait_on_rate_limit_notify=True : the api will print or not notification when rate limits replenish
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# Print own timeline
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
# print(tweet.text)
# ----------------------------------------------------------------------------------------------------------------------

# Override method in StreamListener
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.user.screen_name, status.text, status.created_at, status.retweet_count)
        # Write tweet
        with open('/Users/tanguy/PycharmProjects/Pepites/csv/results_stream.csv', "a") as csvFile:
            csvWriter = csv.writer(csvFile)
            csvWriter.writerow([status.user.screen_name, status.text, status.created_at, status.retweet_count])


# Writing csv titles
with open('/Users/tanguy/PycharmProjects/Pepites/csv/results_stream.csv', "a") as csvFile:
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(['User Name', 'Text', 'Date', 'RT Count'])

# Creating a Stream
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

# Starting A Stream
myStream.filter(track=['CNP Assurances, Axa, Credit Agricole, Generali, BNP Paribas, Groupama, Covéa, Covea, \
                       Credit Mutuel, Crédit Mutuel, Allianz, Société Générale, AG2R, Aviva, Macif, Natixis, \
                       Swiss Life, AIG, MAIF, SMABTP, HSBC, MACSF, A Comme Assure, Active Assurances, ADAP, Affineo, \
                       AGPM, AllSecure, Alptis, Amaguiz, AMV, Aon Assurances, April, Areas Assurances, Assu2000, \
                       Assurance Outremer, Assureo, Assuréo, AssurOnlinem, Assurpeople, Axeria, Camacte, Car-y, \
                       Carrefour Assurances, CGPA, Direct Assurances, Elsassur, Euro Assurances, Generali France, \
                       Groupama, HEYME, Hiscox, Homebrella, Interassurances, La Banque Postale, La Medicale, La Rurale,\
                       Le Finistere Assurance, Le Finistère Assurance, Lovys, Luko, MACSF, MAE, MALJ, Matmut, MAPA, \
                       Monceau Assurances, Mutuaide, Mutuelle de Poitiers Assurances, Opteven, Otherwise, Protech BTP, \
                       SelfAssurance, SMA SA, Sogessur, Thélem Assurances, Verspieren, Zenith Assurance'],
                languages=[
                    'fr'])  # the comma will cause the program  to search any of those terms. for searching all the terms, use spaces only
