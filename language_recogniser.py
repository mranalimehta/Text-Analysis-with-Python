from nltk.corpus import stopwords
from nltk import word_tokenize

sample_text = input("Please enter the text")
words = word_tokenize(sample_text)

english_stopwords = set(stopwords.words("english"))
french_stopwords = set(stopwords.words("french"))
german_stopwords = set(stopwords.words("german"))

is_english = False
is_french = False
is_german = False


for w in words:
       if w in english_stopwords and w not in german_stopwords:
              is_english = True
       if w in french_stopwords:
              is_french = True
       if w in german_stopwords and w not in english_stopwords:
              is_german = True

if is_english is True:
       print("You are talking in English")
elif is_german is True:
       print("You are talking in German")
elif is_french is True:
       print("You are talking in French")
else:
       print("I cannot understand your language!! Sorry!!")
