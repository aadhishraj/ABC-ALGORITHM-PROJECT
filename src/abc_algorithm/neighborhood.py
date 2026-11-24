
import random


def generate_neighbor(candidate):
    """Generate a neighbouring candidate by swapping two positions."""

    neighbor = candidate.copy()

    if len(neighbor) < 2:
        return neighbor

    i, j = random.sample(range(len(neighbor)), 2)

    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]

    return neighbor
