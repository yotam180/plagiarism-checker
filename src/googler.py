from collections import Counter

from rich.progress import track
from googlesearch import search


def search_terms(terms):
    search_string = " ".join(terms)
    return search(search_string)


# TODO: Come up with a better name
def cross_search(terms_list):
    result_counter = Counter()
    for terms in track(terms_list, description="Searching Google..."):
        print()
        result = search_terms(terms)
        result_counter.update(result)

    return result_counter.most_common(10)
