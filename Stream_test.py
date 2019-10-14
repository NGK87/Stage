import tweepy
import csv
from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer
import re

# my user credential in order to access TWITTER API
consumer_key = "mFBcbp8mZkZlEVAFcarY0JQEv"
consumer_secret = "hhuzxiV1EZQOc4sY9e5qhzFOxHauC8s5ydaxQER2NLqwwhtcGm"
access_token = "624059394-D881rOiRH0xTpkrP2SxOZor09jOiV6m1NFtYSMZM"
access_token_secret = "moT59pM1dNi0GxRuUNXR9O1tddU0Wd2uCTYT4T9wYtvu3"

# Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# ----------------------------------------------------------------------------------------------------------------------
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)


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
        sentiment = TextBlob(status.text, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
        polarity = sentiment.polarity

        def num(polarity):
            if polarity < 0:
                return "Negatif"
            elif polarity > 0:
                return "Positif"
            else:
                return "Neutral"

        subjectivity = sentiment.subjectivity
        result = re.sub(r"http\S+", "", status.text)  # remove url from tweets

        keywords_list = ['stress', 'violences', 'insultes', 'menaces', 'agressions', 'troubles', 'anxiété',
                         'dépression',
                         'burnout', 'boreout', 'épuisement', 'suicide', 'irritabilité', 'nervosité', 'fatigue',
                         'palpitations', 'hostile', 'risque', 'déséquilibre', 'harcèlement', 'démuni', 'éreinté',
                         'mal-être', 'difficultés', 'répit', 'frustration', 'suicidaire', 'panique', 'anti-dépresseur',
                         'autodestruction', 'mourir', 'isolement', 'morale', 'calmants', 'annihilation', 'dévastation',
                         'abattement', 'vide', 'anéantissement', 'peine', 'destruction', 'déprime', 'désespoir',
                         'poids',
                         'souffrance', 'libération', 'écroulement', 'abandon', 'détresse', 'découragement',
                         'délaissement', 'supplice', 'tristesse', 'agonie', 'rechute', 'négativité', 'dignité',
                         'psychiatrie', 'tracas', 'regrets', 'peur', 'douleur', 'tourment', 'doutes', 'pleurs',
                         'épreuve', 'amertume', 'noir', 'inquiétude', 'ennui', 'neurasthénie', 'affaiblissement',
                         'lassitude', 'las', 'oppressé', 'agressé', 'signalement', 'thérapie', 'arrêt', 'culpabilité',
                         'surmenage', 'morosité', 'fatigue', 'repli', 'insomnie', 'trinquent', 'terrible', 'contraint',
                         'esclavage', 'péril', 'absentéisme', 'turnover', 'mauvaise ambiance', 'démission', 'viré',
                         'rupture', 'pdv', 'perte', 'conflits', 'interdit', 'tabou', 'déséquilibre', 'crise', 'blocage',
                         'échec', 'rcc', 'départs', 'fermer', 'suppressions', 'licenciement', 'licencié',
                         'reclassement',
                         'absurdité', 'chômage', 'bien-être', 'meilleur', 'respect', 'motivation', 'confiance',
                         'amélioration', 'envie', 'développement', 'heureux', 'motivé', 'considération', 'écoute',
                         'dialogue', 'humain', 'perspective', 'bonheur', 'consécration', 'délice', 'égaiement',
                         'enthousiasme', 'euphorie', 'exaltation', 'extase', 'gaieté', 'fier', 'fierté', 'honneur',
                         'joie', 'jubilation', 'lauriers', 'plaisir', 'prospérité', 'ravissement', 'réjouissance',
                         'régal', 'réussite', 'satisfait', 'satisfaction', 'succès', 'triomphe', 'trophée', 'exaucé',
                         'agréable', 'chanceux', 'estimer', 'idéal', 'juste', 'passionnant', 'passionner', 'triomphe',
                         'merveille', 'bénéfique', 'contempler', 'respirer', 'emplir', 'amour', 'positif', 'abonder',
                         'favoriser', 'élever', 'favorable', 'rayonner', 'veinard', 'plaisanter', 'rigoler', 'créer',
                         'vie', 'vitalité', 'vivant', 'serein', 'merci', 'bravo', 'compliments', 'félicitation',
                         'remerciement', 'gratitude', 'performance', 'égalité', 'conciliation', 'cohésion', 'harmonie',
                         'partage', 'pacifier', 'contribuer', 'comprendre', 'estime']

        for words in keywords_list:
            if words in result:
                return result
                #df.append(result)

        # def keywords_result():
        #     if re.search(keywords_list, result):
        #         return result

        print(status.user.screen_name, result, status.created_at, status.retweet_count, status.source,
              polarity, subjectivity, num(polarity))
        # Write tweet
        with open('/Users/tanguy/PycharmProjects/Pepites/csv/results_stream.csv', "a") as csvFile:
            csvWriter = csv.writer(csvFile)
            csvWriter.writerow([status.user.screen_name, result, status.created_at, status.retweet_count,
                                status.source, polarity, subjectivity, num(polarity)])

        # with open('/Users/tanguy/PycharmProjects/Pepites/csv/results_stream_keywords.csv', "a") as csvFile2:
        #     csvWriter2 = csv.writer(csvFile2)
        #     csvWriter2.writerow([status.user.screen_name, keywords_result(), status.created_at, status.retweet_count,
        #                         status.source, polarity, subjectivity, num(polarity)])

    # ----------------------------------------------------------------------------------------------------------------------
    # Sentiment Analysis
    # sentiment = TextBlob(status.text)  # add .sentiment?
    # polarity = sentiment.polarity
    # subjectivity = sentiment.subjectivity
    # The polarity score is a float within the range [-1.0, 1.0]
    # The subjectivity is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective
    # ----------------------------------------------------------------------------------------------------------------------

    # Writing csv titles
    with open('/Users/tanguy/PycharmProjects/Pepites/csv/results_stream.csv', "a") as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(
            ['User Name', 'Text', 'Date', 'RT Count', 'Source', 'Polarity', 'Subjectivity', 'Type of Polarity'])

    # with open('/Users/tanguy/PycharmProjects/Pepites/csv/results_stream_keywords.csv', "a") as csvFile2:
    #     csvWriter2 = csv.writer(csvFile2)
    #     csvWriter2.writerow(
    #         ['User Name', 'Text', 'Date', 'RT Count', 'Source', 'Polarity', 'Subjectivity', 'Type of Polarity'])


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
