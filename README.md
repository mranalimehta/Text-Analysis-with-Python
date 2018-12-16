# Natural-Language-Processing-with-Python
# All the examples are collection of those I found on online tutorial while learning NLP. These can be found while learning from youtube videos or any other blog. 
****************In nlp1.py *****************

It is first example of getting started with nlp using spaCy. 
spaCy is first imported.
Then english dictionary is loaded and then the text we want to analyse is assigned to the variable.
We pass our text to spacy to parse it and return a parsed data containing text and the type of text it is.


****************In nlp2.py *****************

Second example of NLP. started with importing spaCy and the loading the dictionary and assigning the text to the variable.
In this example we basically want to replace the word token whose type is either PERSON or ORG with PRIVATE in the given text. 
This is done by defining a function replace_entity_with_placeholder.


****************In nlp3.py *****************

The third example is about extracting some useful information from text. For this we make use of another library of python "textacy" along with spacy.
We use the method semistructured_statements and pass it the text and the token about the information is needed.


****************In nlp4.py *****************

In this example we interact with the text which is saved in some text file(here it is named as nlp_text_1.txt).
The example is similar to nlp1.py with only difference of making use of file handling. We open file in read mode and use the text for analysis.


****************In nlp5.py *****************

The fifth example is similar to second example where we replace the particalr type of token with some other token or word. Here we are interacting with a file for reading the text instead direct assigning the text to a variable.

****************In nlp6.py *****************

6th example similar to 3rd where we try to extract information from the text. Again here the text is taken from a text file.


****************In nlp_nltk_1.py *****************

From this example we start using nltk - natural language toolkit for NLP instead of spacy. First example only tokenize the text. We can tokenize text in two ways - either by word or by sentence.
This example is getting started with NLTK.

****************In nlp_nltk_2.py *****************

With this example we introduce stopword. stopwords are the word which are most commonly used in any language. To analyse the text we basically focus on main words from which we can extract information and we do not need commonly and frequently used words. Therefore before starting analysis process or information retrieval we first clean our text by filtering the text and removing the stopwords. 
The code is pretty much straight forward. 


****************In nlp_nltk_3.py *****************

With ths example we introduce stemming with nltk. from nltk.stem import 
PorterStemmer. Now we perform stemming firstly on a list of words with same roots. Then we consider a text and tokenize it to use the stem concept on it. The words will be stemmed to their root words by the Porterstemmer library and its method stem(). The example is pretty straight forward.
























