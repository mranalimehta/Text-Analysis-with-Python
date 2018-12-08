import spacy
import os

print("My fourth Natural Language Processing Example")
print("Reading content saved in a text file")

nlp = spacy.load('en_core_web_lg')

file = open("../nlp_text_1.txt", 'r')
text = file.read()

document = nlp(text)

for entity in document.ents:
       print(entity.text, entity.label_)
