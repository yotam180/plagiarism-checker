from collections import Counter

from rich.progress import track
from googlesearch import search


def search_terms(terms):
    """
    Performs a simple Google search with a given list of terms and returns a list of results (URLs only)

    TODO: Make this return titles of pages too.
    """
    search_string = " ".join(terms)
    return search(search_string)


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

    result_counter = Counter()
    for i, terms in enumerate(terms_list):
        result = search_terms(terms)
        result_counter.update(result)

        yield i + 1, len(terms_list), result_counter.most_common(10)
