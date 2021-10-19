import trafilatura
import grequests

from typing import List


def fetch_parallel(urls: List[str], timeout: float = 15, **get_kwargs) -> List[str]:
    """
    Downloads a list of webpages in parallel, and returns the results.

    For any failed download, returns an empty string.
    """
    rs = [grequests.get(url, **get_kwargs) for url in urls]
    rs = grequests.map(rs, gtimeout=timeout)

    return [response.text if response else "" for response in rs]


def try_fetch_parallel(urls: List[str], **fetch_kwargs) -> List[str]:
    """
    Downloads a list of webpages. Any failed download or empty page will be discarded (thus, the returned list
        may be shorter than the urls parameter)
    """
    return filter(None, fetch_parallel(urls, **fetch_kwargs))


def process_multiple(htmls_list: List[str]) -> List[str]:
    """
    Given a list containing HTML page sources, extracts the content out of all pages and returns a list of page contents.
    """
    return [
        trafilatura.extract(page, include_comments=False, include_tables=False, no_fallback=True)
            for page in htmls_list
    ]


def get_pages_contents(urls: List[str], **fetch_kwargs) -> List[str]:
    """
    Fetches multiple webpages and returns their content.
    """
    return process_multiple(fetch_parallel(urls, **fetch_kwargs))


def try_get_pages_contents(urls: List[str], **fetch_kwargs) -> List[str]:
    """
    Fetches multiple webpages and returns their content. Any failed download will be discarded.
    """
    return process_multiple(try_fetch_parallel(urls, **fetch_kwargs))
