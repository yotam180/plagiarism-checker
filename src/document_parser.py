import spacy
import numpy as np
from collections import Counter

from math_util import softmax


nlp = spacy.load("en_core_web_md")


IRRELEVANT_TOKEN_TYPES = ("CARDINAL", "DATE", "ORDINAL", "PERCENTAGE")


class Document(object):
    # TODO: Support multiple languages?

    def __init__(self, doc_text: str):
        self.doc = nlp(doc_text)
        self.counter = None

    def get_weighted_entities(self):
        """
        Returns a numpy array of entities (strings) and a numpy array of their corresponding weights.
        """
        entities, counts = self.get_entities()
        weighted = Document._entity_weight(entities, counts)

        sort_index = weighted.argsort()[::-1]
        return entities[sort_index], weighted[sort_index]

    def get_entities(self):
        """
        Returns two numpy arrays - one with the entities themselves (strings), and one with their counts (float64)
        The order of the entities in the arrays is the order in which they appear in the document.
        """
        entities = self._get_entity_counter().keys()
        counts = self._get_entity_counter().values()

        return np.array(list(entities)), np.fromiter(counts, dtype=np.float64)

    def _get_entity_counter(self):
        if not self.counter:
            self.counter = Counter(ent.text for ent in self.doc.ents if Document._filter_entity(ent))

        return self.counter
        
    @staticmethod 
    def _entity_weight(entities, counts):
        """
        The weight of the entity affects the probability of it being used to search websites. The higher the weight, the more
        searches this entity will appear in.

        TODO: Reason about the weights and the use of softmax in the formula.
        """
        ENTITY_LENGTH_WEIGHT = 0.5
        ENTITY_LOCATION_WEIGHT = 1.0
        ENTITY_COUNT_WEIGHT = 2

        if not len(entities):
            # TODO: Overcome this problem. What can we do if we hadn't found any entities?
            raise ValueError("No entities found in text!")
        
        lengths = np.array(list(map(len, entities)))
        locations = np.arange(len(entities), 0, -1)

        return softmax(locations) * ENTITY_LOCATION_WEIGHT + \
                softmax(lengths) * ENTITY_LENGTH_WEIGHT + \
                softmax(counts) * ENTITY_COUNT_WEIGHT

    @staticmethod
    def _filter_entity(entity):
        return entity.label_ not in IRRELEVANT_TOKEN_TYPES
