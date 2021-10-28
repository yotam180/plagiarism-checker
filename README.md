# Plagiarism Checker

Catches naughty students who copy from Wikipedia! Searches the web for similar webpages and finds plagiarism

## Example

![Screenshot](https://raw.githubusercontent.com/yotam180/plagiarism-checker/master/doc/sample_picture.png)

## How does this work (sort of)

Simply put, we divide the process to 3 stages:

1. Extract entity data from the text
1. Use those entities to find relevant web pages on Google
1. Fetch and parse those webpages, and perform a sentence-by-sentence similarity comparison

The NLP part is all done using the [spaCy](https://spacy.io/) Python package.

### Entity extraction

We use the `en_core_web_md` model to split the text to sentences and extract named entities (NER). Each entity is then given a score, based on a few parameters:

1. Its length ("The football association of Israel" will have a higher score than "football" or "Israel", since it is assumed that longer entities are more specific)
1. Its first appearance in the text (based on the assumption that a text should open with the main parts, and the later paragraphs are specifications, and may be focused on niche-areas or more specific details)
1. Count (We assume that entities appearing more in the text are more relevant)

The parameters are weighted together (more information in `src/document_parser.py`).

### Google Searches

Triplets of entities are selected for each Google search (I empirically observed that it yields much better results)
We perform multiple Google searches with different sets of random entities, and count the results.
The 10 web pages returned on the highest percentage of searches are selected for examination.

### Sentence comparison

We use the `trafilatura` package to try and extract the main text from each webpage, split it to sentences with spaCy, and perform a word-vector based sentence comparison between every sentence in the original text and every sentence in the fetched article.

We keep track of the most-similar sentence to any sentence in the articles (with a certain similarity threshold) and then report the results.
