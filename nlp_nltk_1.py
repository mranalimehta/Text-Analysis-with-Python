from nltk import sent_tokenize, word_tokenize

simple_text = "Hello everyone. It's me Ms. Crazy Programmer. I am learing natural language processing with nltk in python. It is awesome and I am having fun."

print(word_tokenize(simple_text))
print(sent_tokenize(simple_text)) 

print("It will print each word on each line")
for each in word_tokenize(simple_text):
       print(each)

print("It will print each line")
for each in sent_tokenize(simple_text):
       print(each)
