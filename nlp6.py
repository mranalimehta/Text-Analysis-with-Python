import spacy
import textacy.extract
import os

nlp = spacy.load('en_core_web_lg')

file = open("../nlp_text_2.txt",'r')
text = file.read()

document = nlp(text)

statements = textacy.extract.semistructured_statements(document,"washington")

print("Information from Washington Wikipedia Page")

for statement in statements:
       subject, verb, fact = statement
       print("Statement - ", statement)
       print("Fact - ", fact)
       

