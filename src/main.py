import spacy

from bs4 import BeautifulSoup
from urllib.request import urlopen

from itertools import product

article_sample = """
The FA Women's Premier League is the 26th season of the competition. It began on 1992.
"""

wikipedia_scraped = """
The 2017–18 season of the FA Women's Premier League is the 26th season of the competition, which began in 1992. It sits at the third and fourth levels of the women's football pyramid, below the two divisions of the FA Women's Super League and above the eight regional football leagues.

The league features six regional divisions: the Northern and Southern divisions at level three of the pyramid, and below those Northern Division 1, Midlands Division 1, South East Division 1, and South West Division 1. 71 teams were members of the league before the start of the 2017–18 season, divided equally into five divisions of twelve teams, and one division of eleven teams.[1] At the end of the season Blackburn Rovers and Charlton Athletic, respectively the champions of the Northern and Southern divisions, qualified for a Championship Play Off match against each other which Charlton Athletic won 2-1 thus becoming the overall National League Champion, and winning them promotion to the re-branded FA Women's Championship. As part of the restructuring of the top 4 tiers of women football by The Football Association, West Ham United was awarded promotion to the FA WSL, with Leicester City Womens, Lewes, and Sheffield United awarded promotion to the FA Women's Championship.

Advanced Engineering Materials is a peer-reviewed materials science journal that publishes monthly. Advanced Engineering Materials publishes peer-reviewed reviews, communications, and full papers, on topics centered around structural materials, such as metals, alloys, ceramics, composites, plastics etc..
"""

nlp = spacy.load("en_core_web_md")

doc1 = nlp(article_sample)
doc2 = nlp(wikipedia_scraped)

sents1 = list(sent for sent in doc1.sents if sent.text.strip())
sents2 = list(sent for sent in doc2.sents if sent.text.strip())

for sent1, sent2 in product(sents1, sents2):
    print("=======")
    print(sent1.text.strip())
    print(sent2.text.strip())
    print(sent1.similarity(sent2))
