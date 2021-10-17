import numpy as np

import random


def random_entity_select(entities: np.array, weights: np.array, entity_selection_size=3, count=10):
    """
    Selects randomized sets of `entity_selection_size` entities, based on the `weights` parameter (higher-weight entities
    will be chosen more frequently)

    TODO: Force sets to contain different entities (no double entities)
    """
    choices = random.choices(entities, weights=weights, k=entity_selection_size * count)
    return np.array(choices).reshape(-1, entity_selection_size)
