import numpy as np

import random


def random_entity_select(entities: np.array, weights: np.array, entity_selection_size=3, count=10):
    """
    Selects randomized sets of `entity_selection_size` entities, based on the `weights` parameter (higher-weight entities
    will be chosen more frequently)

    TODO: Force sets to contain different entities (no double entities) - done, this should be implemented more efficiently
    """
    # choices = random.choices(entities, weights=weights, k=entity_selection_size * count)
    # return np.array(choices).reshape(-1, entity_selection_size)

    results = []
    for i in range(count):
        results.append(_randomly_select_with_weights(entities, weights, entity_selection_size))

    return results


def _randomly_select_with_weights(entities: np.array, weights: np.array, entity_selection_size=3):
    ents = entities
    w = weights
    results = []
    for i in range(entity_selection_size):
        if not len(ents):
            break

        [choice] = random.choices(ents, weights=list(w), k=1)
        
        w = w[ents != choice]
        ents = ents[ents != choice]
        results.append(choice)

    return results