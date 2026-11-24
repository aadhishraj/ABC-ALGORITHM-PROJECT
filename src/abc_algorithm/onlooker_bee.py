import random

from src.abc_algorithm.neighborhood import generate_neighbor
from src.abc_algorithm.fitness import evaluate_candidate


def onlooker_bee_phase(jobs, population, fitness_results, onlooker_count=None):
    """
    Improve candidate schedules using onlooker bees.
    Better candidates have a higher probability of selection.
    """

    if onlooker_count is None:
        onlooker_count = len(population)

    # Calculate selection weights
    weights = [result["fitness"] for result in fitness_results]

    # Select candidates using roulette-wheel selection
    selected_indices = random.choices(
        range(len(population)),
        weights=weights,
        k=onlooker_count
    )

    # Generate and evaluate neighbouring candidates
    for index in selected_indices:
        candidate = population[index]

        neighbor = generate_neighbor(candidate)
        neighbor_result = evaluate_candidate(jobs, neighbor)

        # Keep the better candidate
        if neighbor_result["fitness"] > fitness_results[index]["fitness"]:
            population[index] = neighbor
            fitness_results[index] = neighbor_result

    return population, fitness_results