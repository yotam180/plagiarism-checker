import trafilatura


def get_page_contents(url: str) -> str:
    html_content = trafilatura.fetch_url(url)
    return trafilatura.extract(html_content, include_comments=False, include_tables=False, no_fallback=True)
