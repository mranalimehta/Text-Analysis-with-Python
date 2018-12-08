import spacy
import os

print("Fifth example on NLP - replacing the token of type PERSON and ORG with PRIVATE and reading text from text file")

nlp = spacy.load('en_core_web_lg')

file = open("../nlp_text_1.txt",'r')
text = file.read()

def replace_entity_with_placeholder(token):
       if token.ent_iob != 0 and (token.ent_type_ == "PERSON" or token.ent_type_ == "ORG"):
              return "PRIVATE"
       else:
              return token.string

def scrub(text):
       document = nlp(text)
       for entity in document.ents:
              entity.merge()
       tokens = map(replace_entity_with_placeholder, document)
       return "".join(tokens)

print(scrub(text))
