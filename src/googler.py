from collections import Counter
from rich.progress import track

from bs4 import BeautifulSoup
import grequests


def fetch_parallel(search_terms, num_results=10, lang="en"):
    usr_agent = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/92.0.3163.100 Safari/537.36'}

    escaped_search_terms = [search_term.replace(' ', '+') for search_term in search_terms]
    google_urls = [
        'https://www.google.com/search?q={}&num={}&hl={}'.format(
            escaped_search_term, num_results+1, lang) for escaped_search_term in escaped_search_terms]

    rs = [grequests.get(u, headers=usr_agent) for u in google_urls[:10]]
    rs = grequests.map(rs, gtimeout=10)
    
    texts = [response.text for response in rs if response]
    print(len(texts))
    return texts


def parse_results(raw_html):
    soup = BeautifulSoup(raw_html, 'html.parser')
    result_block = soup.find_all('div', attrs={'class': 'g'})
    for result in result_block:
        link = result.find('a', href=True)
        title = result.find('h3')
        if link and title:
            yield link['href']


def parse_multiple(result_list):
    return [list(parse_results(result)) for result in result_list]


def cross_search(terms_list):
    """
    TODO: Come up with a better name
    
    Takes sets of search terms and looks them up together on Google.

    For example, given the next terms list:
    [
        ["A", "B", "C"],
        ["D", "E", "F"]
    ]

    Two Google searches will be issued - "A B C" and "D E F"

    The results are accumulated in a counter, and the 10 most frequent results amongst all searches are returned (see below)

    The reason for that is the belief that random selection of different combinations of the search terms will (in high probability) yield relevant results,
        and cross-counting these results should increase the chance of selecting the most relevant pages to return.

    Yields three objects:
        - int - searches conducted so far
        - int - total searches to be conducted
        - List[str] - leading 10 results
    """

    responses = fetch_parallel(
        [" ".join(terms) for terms in terms_list]
    )
    responses = parse_multiple(responses)

    result_counter = Counter()
    for response in responses:
        result_counter.update(response)

    return result_counter.most_common(10)
