import trafilatura
import grequests


def fetch_parallel(urls):
    rs = [grequests.get(url) for url in urls]
    rs = grequests.map(rs)
    return [response.text for response in rs]


def get_pages_contents(urls):
    pages = fetch_parallel(urls)
    return [
        trafilatura.extract(page, include_comments=False, include_tables=False, no_fallback=True)\
        for page in pages
    ]
