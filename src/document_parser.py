import spacy
import random
import numpy as np

from collections import Counter
from typing import NamedTuple

from math_util import softmax

nlp = spacy.load("en_core_web_md")


IRRELEVANT_TOKEN_TYPES = ("CARDINAL", "DATE", "ORDINAL", "PERCENTAGE")


class Document(object):
    # TODO: Support multiple languages?

    def __init__(self, doc_text: str):
        self.doc = nlp(doc_text)
        self.counter = None

    def get_entities(self):
        """
        Returns two numpy arrays - one with the entities themselves (strings), and one with their counts (float64)
        The order of the entities in the arrays is the order in which they appear in the document.
        """
        entities = self._get_entity_counter().keys()
        counts = self._get_entity_counter().values()

        return np.array(list(entities)), np.array(list(counts), dtype=np.float64)

    def get_weighted_entities(self):
        entities, counts = self.get_entities()
        weighted = Document._entity_weight(entities, counts)

        sort_index = weighted.argsort()[::-1]
        return entities[sort_index], weighted[sort_index]

    def _get_entity_counter(self):
        if not self.counter:
            self.counter = Counter(ent.text for ent in self.doc.ents if Document._filter_entity(ent))

        return self.counter

    @staticmethod
    def _filter_entity(entity):
        return entity.label_ not in IRRELEVANT_TOKEN_TYPES
        
    @staticmethod 
    def _entity_weight(entities, counts):
        """
        The weight of the entity affects the probability of it being used to search websites. The higher the weight, the more
        searches this entity will appear in.

        TODO: Reason about the weights and the use of softmax in the formula.
        """
        ENTITY_LENGTH_WEIGHT = 0.5
        ENTITY_LOCATION_WEIGHT = 3.0
        ENTITY_COUNT_WEIGHT = 2
        
        lengths = np.array(list(map(len, entities)))
        locations = np.arange(len(entities), 0, -1)

        return softmax(locations) * ENTITY_LOCATION_WEIGHT + \
                softmax(lengths) * ENTITY_LENGTH_WEIGHT + \
                softmax(counts) * ENTITY_COUNT_WEIGHT


def random_entity_select(ents, counts, entity_selection_size=3, count=10):
    choices = random.choices(ents, weights=counts, k=entity_selection_size * count)
    return np.array(choices).reshape(-1, entity_selection_size)
