import random
from textblob import TextBlob

# File = open("twitter_scraping/TEXT/KylieJenner_tweet_reduced.txt") #open file
# txt = File.read() #read all lines


# decoded_txt = txt.decode("utf-8") 
# blob = TextBlob(decoded_txt)

# nouns = []
# nouns.append(blob.noun_phrases)


# for elem in nouns[0]:
# 	print str(elem.encode("utf-8"))
# print nouns





File = open("kylie_words_reduced.txt") #open file
txt = File.read() #read all lines

# encoded_text = txt.encode("utf-8")
	# decoded_txt = txt.decode("utf-8") 
	# blob = TextBlob(decoded_txt)

	# nouns = []
	# nouns.append(blob.noun_phrases)

print txt 
# word = random.choice(txt)

# print encoded_text


# new_text = txt[1]
# print new_text


# word


# sentences = nltk.sent_tokenize(lines) #tokenize sentences
# nouns = [] #empty to array to hold all nouns

# for sentence in sentences:
#      for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
#          if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
#              nouns.append(word)