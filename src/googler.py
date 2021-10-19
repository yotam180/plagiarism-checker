from collections import Counter
from itertools import chain
from typing import List

from bs4 import BeautifulSoup
import grequests


def cross_search(terms_list: List[List[str]]) -> List[str]:
    """
    Takes sets of search terms and looks them up together on Google.

    For example, given the next terms list:
    [
        ["A", "B", "C"],
        ["D", "E", "F"]
    ]

    Two Google searches will be issued - "A B C" and "D E F"

    The results URLs are accumulated in a counter, and the 10 most frequent results amongst all searches are returned

    The reason for that is the belief that random selection of different combinations of the search terms will (in high probability) yield relevant results,
        and cross-counting these results should increase the chance of selecting the most relevant pages to return.
    """
    responses = _fetch_parallel(" ".join(terms) for terms in terms_list)
    parsed_responses = _parse_multiple(responses)
    return Counter(chain(*parsed_responses)).most_common(10)


def _fetch_parallel(search_terms: List[str], num_results: int = 10, lang: str = "en") -> List[str]:
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
    return texts


def _parse_results(raw_html):
    soup = BeautifulSoup(raw_html, 'html.parser')
    result_block = soup.find_all('div', attrs={'class': 'g'})
    for result in result_block:
        link = result.find('a', href=True)
        title = result.find('h3')
        if link and title:
            yield link['href']


def _parse_multiple(result_list):
    return [list(_parse_results(result)) for result in result_list]
