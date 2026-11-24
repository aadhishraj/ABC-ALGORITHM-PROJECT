
import random


def generate_candidate(jobs):
    """Generate one valid operation-based candidate."""

    candidate = []

    for job, operations in jobs.items():
        candidate.extend([job] * len(operations))

    random.shuffle(candidate)

    return candidate


def generate_population(jobs, population_size=10):
    """Generate multiple candidate solutions."""

    population = []

    for _ in range(population_size):
        candidate = generate_candidate(jobs)
        population.append(candidate)

    return population

