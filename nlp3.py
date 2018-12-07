import spacy
import textacy.extract

nlp = spacy.load('en_core_web_lg')

text = "Washington, D.C., formally the District of Columbia and commonly referred to as Washington or D.C., is the capital of the United States of America.[4] Founded after the American Revolution as the seat of government of the newly independent country, Washington was named after George Washington, first President of the United States and Founding Father.[5] Washington is the principal city of the Washington metropolitan area, which has a population of 6,131,977.[6] As the seat of the United States federal government and several international organizations, the city is an important world political capital.[7] Washington is one of the most visited cities in the world, with more than 20 million annual tourists.[8][9] \
The signing of the Residence Act on July 16, 1790, approved the creation of a capital district located along the Potomac River on the country's East Coast. The U.S. Constitution provided for a federal district under the exclusive jurisdiction of the Congress and the District is therefore not a part of any state. The states of Maryland and Virginia each donated land to form the federal district, which included the pre-existing settlements of Georgetown and Alexandria. Named in honor of President George Washington, the City of Washington was founded in 1791 to serve as the new national capital. In 1846, Congress returned the land originally ceded by Virginia; in 1871, it created a single municipal government for the remaining portion of the District. \
Washington had an estimated population of 693,972 as of July 2017, making it the 20th largest American city by population. Commuters from the surrounding Maryland and Virginia suburbs raise the city's daytime population to more than one million during the workweek. The Washington metropolitan area, of which the District is the principal city, has a population of over 6 million, the sixth-largest metropolitan statistical area in the country. \
All three branches of the U.S. federal government are centered in the District: U.S. Congress (legislative), President (executive), and the U.S. Supreme Court (judicial). Washington is home to many national monuments and museums, which are primarily situated on or around the National Mall. The city hosts 177 foreign embassies as well as the headquarters of many international organizations, trade unions, non-profit, lobbying groups, and professional associations, including the Organization of American States, AARP, the National Geographic Society, the Human Rights Campaign, the International Finance Corporation, and the American Red Cross. A locally elected mayor and a 13‑member council have governed the District since 1973. However, Congress maintains supreme authority over the city and may overturn local laws. D.C. residents elect a non-voting, at-large congressional delegate to the House of Representatives, but the District has no representation in the Senate. The District receives three electoral votes in presidential elections as permitted by the Twenty-third Amendment to the United States Constitution, ratified in 1961.### Parse the text with spaCy"

document = nlp(text)

statements = textacy.extract.semistructured_statements(document,"washington")

print("Information from Washington Wikipedia Page")

for statement in statements:
       subject, verb, fact = statement
       print("Statement - ", statement)
       print("Fact - ", fact)
       

