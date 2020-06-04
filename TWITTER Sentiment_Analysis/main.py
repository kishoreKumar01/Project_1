import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import GetOldTweets3 as got

def get_tweets():
    Tweet_Criteria = got.manager.TweetCriteria().setQuerySearch('CoronaOutbreak').setMaxTweets(500) \
    .setSince("2020-03-20") \
    .setUntil("2020-04-25")
    tweets = got.manager.TweetManager.getTweets(Tweet_Criteria)
    tweet_txt = [[tweet.text] for tweet in tweets]
    return tweet_txt

text = get_tweets()
print(text)
length = len(text)
#reading the twitter text as a string
twitter_txt = ""
for i in range(0,length):
    twitter_txt += text[i][0] + " "

#print(twitter_txt)

lower_txt = ""
#with open('read.txt',encoding='utf-8') as text:
for word in twitter_txt:
    # converting all text to the lower case for analysis
    word = word.lower()
    lower_txt += word

#removing all the special characters that are not useful for our analysis
clear_txt = lower_txt.translate(str.maketrans('','',string.punctuation))
text_lst = word_tokenize(clear_txt,'English')
#removing the unnecessary words form the file
final_lst = []
for words in text_lst:
    if words not in stopwords.words("English") and words.isalpha() is True:
        final_lst.append(words)

#print(final_lst)
#getting the emotion of each words form the emotion.txt
emotion_lst = []
with open('emotion.txt', 'r') as file:
    for line in file:
        line = line.replace(",","").replace("'","").replace("\n","").strip()
        words,emotion_words = line.split(':')
        if words in final_lst:
            emotion_lst.append(emotion_words)

#print(emotion_lst)
count = (Counter(emotion_lst))
x,y = count.keys(),count.values()
plot = plt.bar(x,y)
plt.savefig('sentiment_Analysis')
plt.title('sentiment_Analysis')
plt.xlabel("Emotions in the content")
plt.ylabel("Rate of Emotions")
plt.show()