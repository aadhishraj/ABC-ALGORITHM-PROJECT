from src.abc_algorithm.population import generate_candidate
from src.abc_algorithm.fitness import evaluate_candidate


def scout_bee_phase(jobs, population, fitness_results, trial_counts, limit=5):
    """
    Replace candidates that have failed to improve
    for a specified number of attempts.
    """

    for i in range(len(population)):

        if trial_counts[i] >= limit:

            # Generate a fresh random candidate
            new_candidate = generate_candidate(jobs)
            new_result = evaluate_candidate(jobs, new_candidate)

            # Replace the stagnant candidate
            population[i] = new_candidate
            fitness_results[i] = new_result

            # Reset its trial counter
            trial_counts[i] = 0

    return population, fitness_results, trial_counts