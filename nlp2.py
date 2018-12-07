import spacy

print("Second example on NLP - replacing the token of type PERSON and ORG with PRIVATE.")

nlp = spacy.load('en_core_web_lg')

text = "Amazon.com, Inc., doing business as Amazon, is an American electronic commerce and cloud computing company based in Seattle, Washington, that was founded by Jeff Bezos on July 5, 1994. The tech giant is the largest Internet retailer in the world as measured by revenue and market capitalization, and second largest after Alibaba Group in terms of total sales. The amazon.com website started as an online bookstore and later diversified to sell video downloads/streaming, MP3 downloads/streaming, audiobook downloads/streaming, software, video games, electronics, apparel, furniture, food, toys, and jewelry. The company also produces consumer electronics — Kindle e-readers, Fire tablets, Fire TV, and Echo — and is the world’s largest provider of cloud infrastructure services (IaaS and PaaS). Amazon also sells certain low-end products under its in-house brand AmazonBasics."

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
