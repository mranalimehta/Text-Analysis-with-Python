from nltk.corpus import stopwords
from nltk import word_tokenize

sample_text = "This is an example to show the stopword filtration."

stop_words = set(stopwords.words("english"))
print(stop_words)

words = word_tokenize(sample_text)

filtered_text = []

for w in words:
       if w not in stop_words:
              filtered_text.append(w)

print(filtered_text)
