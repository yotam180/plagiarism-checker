import numpy as np

import random


def random_entity_select(entities: np.array, weights: np.array, entity_selection_size=3, count=10):
    """
    Selects randomized sets of `entity_selection_size` entities, based on the `weights` parameter (higher-weight entities
    will be chosen more frequently)

    """
    return [_randomly_select_with_weights(entities, weights, entity_selection_size) for _ in range(count)]


def _randomly_select_with_weights(entities: np.array, weights: np.array, count: int = 3):
    return list(_pop_random_n(entities, weights, count))


def _pop_random(entities: np.array, weights: np.array):
    """
    Pops a (weighted) randomly selected element, and returns:
        - The popped elements
        - The entities list without the popped element
        - The weights list without the weight of the popped element
    """
    if not len(entities):
        raise ValueError("Cannot pop out of an empty array")

    [choice] = random.choices(entities, weights=weights, k=1)

    return choice, entities[entities != choice], weights[entities != choice]


def _pop_random_n(entities: np.array, weights: np.array, count: int = 3):
    """
    Yield up to `count` different randomly chosen entities from the entities array.
    """
    for _ in range(count):
        if not len(entities):
            return

        choice, entities, weights = _pop_random(entities, weights)
        yield choice