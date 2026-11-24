
from src.abc_algorithm.neighborhood import generate_neighbor
from src.abc_algorithm.fitness import evaluate_candidate


def employed_bee_phase(jobs, population, fitness_results):
    """Improve candidate schedules using employed bees."""

    for i, candidate in enumerate(population):

        neighbor = generate_neighbor(candidate)

        neighbor_result = evaluate_candidate(jobs, neighbor)

        if neighbor_result["fitness"] > fitness_results[i]["fitness"]:

            population[i] = neighbor
            fitness_results[i] = neighbor_result

    return population, fitness_results
