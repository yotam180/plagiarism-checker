import spacy

from bs4 import BeautifulSoup
from urllib.request import urlopen

from itertools import product

article_sample = """
The FA Women's Premier League is the 26th season of the competition. It began on 1992.
At level 3 in the league, The only divisions in 2013 and 2014 with WPL branding were the Northern Division and Southern Division.
"""

wikipedia_scraped = """
The 2017–18 season of the FA Women's Premier League is the 26th season of the competition, which began in 1992. It sits at the third and fourth levels of the women's football pyramid, below the two divisions of the FA Women's Super League and above the eight regional football leagues.

The league features six regional divisions: the Northern and Southern divisions at level three of the pyramid, and below those Northern Division 1, Midlands Division 1, South East Division 1, and South West Division 1. 71 teams were members of the league before the start of the 2017–18 season, divided equally into five divisions of twelve teams, and one division of eleven teams.[1] At the end of the season Blackburn Rovers and Charlton Athletic, respectively the champions of the Northern and Southern divisions, qualified for a Championship Play Off match against each other which Charlton Athletic won 2-1 thus becoming the overall National League Champion, and winning them promotion to the re-branded FA Women's Championship. As part of the restructuring of the top 4 tiers of women football by The Football Association, West Ham United was awarded promotion to the FA WSL, with Leicester City Womens, Lewes, and Sheffield United awarded promotion to the FA Women's Championship.

Advanced Engineering Materials is a peer-reviewed materials science journal that publishes monthly. Advanced Engineering Materials publishes peer-reviewed reviews, communications, and full papers, on topics centered around structural materials, such as metals, alloys, ceramics, composites, plastics etc..

Before the National League, women's teams nationally had competed in the WFA Cup (Women's FA Cup) since 1970, and there were English regional leagues, but this was the first regular nationwide competition of its kind.

The Women's National League was inaugurated in the 1991–92 season by the Women's Football Association (WFA),[1] with a monetary grant from the Sports Council.[2] Eight teams played in the top flight in that year. From the League's foundation, it consisted of a national premier division and two lower divisions, the Northern and Southern Divisions, whose winners each season were promoted to the top flight.


Doncaster Belles were the first champions of the Women's National League in 1991–92
From 1991–92 until 2012–13, the national premier division was above the Northern and Southern Divisions. Since 1991–92, the Northern and Southern Divisions have run on an equal basis with promotion, and this continues today. The terms Women's Premiership and Ladies Premiership were generally used for the National Division only.

After the League's third season, the FA assumed responsibility for the competition and renamed it, beginning with the 1994–95 FA Women's Premier League (FA WPL).[3]

The Women's Premier League remained level 1 and 2 of women's football until the end of the 2009–10 season. From 2000 until 2008, the WPL champions competed in the annual FA Women's Community Shield.

The National Division's most successful clubs were Arsenal (12 titles), Croydon (3 titles), Doncaster Belles (2 titles and 7 times runners-up), Everton (1 title and 5 times runners-up), and Sunderland (3 titles at league level 2).

The Women's Premier League lost several clubs prior to the 2010–11 season and the National Division was demoted to level 2, due to the creation of the FA WSL in 2011.[4] (The WSL was a summer league for its first six years, as opposed to the WPL's winter format.) Strangely, the lower divisions were still given the name "Premier League" for eight more seasons. The number of clubs competing in the Northern and Southern Divisions decreased from 12 to 10. The National Division decreased from 12 clubs to eight (2010–11), then increased to 10 clubs (2011–12 and 2012–13).

After the WPL National Division's three seasons at level 2, that division was scrapped after 2012–13, due to the FA's decision to add another WSL division, WSL 2, for its 2014 season, which included some clubs that moved from the WPL.

The only divisions in 2013–14 with WPL branding were the Northern and Southern Divisions at league level 3.

From the 2014–15 season, the Women's Premier League incorporated the four existing Combination Women's Football Leagues (level 4), as the Premier League's "Division One", with four groups of Division One leagues: North, Midlands, South East and South West.[5] The FA proposed rebranding the WPL collectively as the Women's Championship League,[6] but instead the six divisions kept the name Women's Premier League until 2018.

The winners of the Northern and Southern Divisions have played each other since 2014–15 in a single play-off at a neutral venue, to win the Women's Premier League/National League championship and promotion into the level 2 division. This was the first instance of promotion from the WPL to the WSL when the first play-off occurred in 2015. In that year's play-off between Portsmouth and Sheffield F.C. at Stratford FC's ground, Sheffield won through a stoppage-time goal.

The six divisions were renamed the Women's National League from 2018–19.

"""

from document_parser import *

doc = load_document(wikipedia_scraped)
print(get_weighted_document_entities(doc))

# nlp = spacy.load("en_core_web_md")

# doc1 = nlp(article_sample)
# doc2 = nlp(wikipedia_scraped)

# print(doc1.ents)

# sents1 = list(sent for sent in doc1.sents if sent.text.strip())
# sents2 = list(sent for sent in doc2.sents if sent.text.strip())

# for sent1, sent2 in product(sents1, sents2):
#     sim = sent1.similarity(sent2)
#     if sim >= .95:
#         print("=======")
#         print("SENT1:", sent1.text.strip())
#         print("SENT2:", sent2.text.strip())
#         print("SENT1 ents:", sent1.ents)
#         print("SENT2 ents:", sent2.ents)
#         print(sim)
