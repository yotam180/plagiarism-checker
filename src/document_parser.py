import spacy
import random
import numpy as np

from collections import Counter

nlp = spacy.load("en_core_web_sm")


IRRELEVANT_TOKEN_TYPES = ("CARDINAL", "DATE", "ORDINAL", "PERCENTAGE")


def load_document(doc_text: str) -> "spacy.tokens.doc.Doc":
    return nlp(doc_text)


# TODO: Weight entities based on their order of appearance in the document? (meaning first would get a higher weight?)
def get_document_entities(doc: "spacy.tokens.doc.Doc"):
    for ent in doc.ents:
        print(ent.text, ent.label_)

    print("===========")

    nouns = Counter(ent.text for ent in doc.ents if ent.label_ not in IRRELEVANT_TOKEN_TYPES) # TODO: Proper filter?
    return np.array([*nouns.keys()]), np.array([*nouns.values()], dtype=np.float64)


def get_weighted_document_entities(doc: "spacy.tokens.doc.Doc"):
    ents, counts = get_document_entities(doc)
    weighted = _weighted_counts_formula(ents, counts)

    idx = weighted.argsort()[::-1]
    return ents[idx], weighted[idx]


def random_entity_select(ents, counts, entity_selection_size=3, count=10):
    choices = random.choices(ents, weights=counts, k=entity_selection_size * count)
    return np.array(choices).reshape(-1, entity_selection_size)


def _weighted_counts_formula(ents: np.array, counts: np.array) -> np.array:
    # TODO: Choose a better formula?
    lengths = np.array([*map(len, ents)])
    locations = np.arange(len(ents), 0, -1)

    return 3 * softmax(locations) + 0.5 * softmax(lengths) + 2 * softmax(counts)

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()