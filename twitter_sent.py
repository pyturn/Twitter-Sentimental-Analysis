import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob 
ckey = '*****************************'
csecret = '*************************************************'
atoken = '**************************************************'
asecret = '*************************************************'

#Maximum Count using twitter api in one round is 100 only.

auth = OAuthHandler(ckey , csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)
public_tweets = api.search('#Trump', count=100)

#This is a document which contains all the tweets.	
documents = []
for tweet in public_tweets:
	documents.append(tweet.text)
	
	
# Now applying concept of removal of stopwords on these tweets.
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
documents1 = []
stop_words = set(stopwords.words('english'))
for tweet in documents:
	word_token=word_tokenize(tweet)
	stre=''
	for w in word_token:
		if w not in stop_words:
			stre=stre+w+ ' '		
	documents1.append(stre)
 
print "Tweets after removal of stopwards"
for tweets in documents1:
	print tweets



#Now I am doing part of speech tagging for only 10 tweets. Here we are using original tweets not the tweets after removal of stopwords.
import nltk
print "Tweets after tagged with Part of Speeches"
def process_content():
	try:
		for i in documents[:10]:
			words = word_tokenize(i)
			tagged = nltk.pos_tag(words)
			print(tagged)
	except Exception as e:
		print(str(e))
process_content()


positive = 0.0

#Now lets pass these stopwords removed tweets in Sentiment Classifier. This will classify my tweets as positive or negative.
print len(documents)
for k in range(1,len(documents1)):
	print documents1[k]
	analysis = TextBlob(documents1[k])
	if analysis.sentiment[0]>0:
		#positive = positive + 1
		print "Positive"
		
	else:
		print "Negative"
	

