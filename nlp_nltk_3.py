from nltk.corpus import stopwords
from nltk import word_tokenize

sample_text = "This is second example of NLTK for NLP."
#sample_text = "Ich lerne natürliche Sprachverarbeitung. Es ist ziemlich lustig und interessant. Es erfordert jedoch viel harte Arbeit und Übung, um durch die Konzepte zu kommen."
stop_words = set(stopwords.words("german"))
print(stop_words)
print("______________________________")
words = word_tokenize(sample_text)
print(words)
print("______________________________")
count = 0
text_stop_word = []
for each_word in words:
       if each_word in stop_words:
              text_stop_word.append(each_word)
              count = count + 1

if count == len(text_stop_word):
       print("Its GERMAN Language")
else:
       print("Its some other language")
