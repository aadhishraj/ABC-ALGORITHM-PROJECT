
import random

from src.abc_algorithm.population import generate_population
from src.abc_algorithm.fitness import evaluate_candidate
from src.abc_algorithm.employed_bee import employed_bee_phase
from src.abc_algorithm.onlooker_bee import onlooker_bee_phase
from src.abc_algorithm.scout_bee import scout_bee_phase


def run_abc(jobs, population_size=10, iterations=50, limit=5):
    """Run the complete sequential Artificial Bee Colony algorithm."""

    # Step 1: Initialize population
    population = generate_population(jobs, population_size)

    fitness_results = [
        evaluate_candidate(jobs, candidate)
        for candidate in population
    ]

    trial_counts = [0] * population_size

    # Store the best solution found
    best_index = max(
        range(population_size),
        key=lambda i: fitness_results[i]["fitness"]
    )

    best_candidate = population[best_index].copy()
    best_result = fitness_results[best_index].copy()

    history = []

    # Step 2: Run ABC iterations
    for iteration in range(iterations):

        # Employed Bee phase
        previous_fitness = [r["fitness"] for r in fitness_results]

        population, fitness_results = employed_bee_phase(
            jobs, population, fitness_results
        )

        for i in range(population_size):
            if fitness_results[i]["fitness"] > previous_fitness[i]:
                trial_counts[i] = 0
            else:
                trial_counts[i] += 1

        # Onlooker Bee phase
        previous_fitness = [r["fitness"] for r in fitness_results]

        population, fitness_results = onlooker_bee_phase(
            jobs, population, fitness_results
        )

        for i in range(population_size):
            if fitness_results[i]["fitness"] > previous_fitness[i]:
                trial_counts[i] = 0
            else:
                trial_counts[i] += 1

        # Scout Bee phase
        population, fitness_results, trial_counts = scout_bee_phase(
            jobs, population, fitness_results, trial_counts, limit
        )

        # Update global best
        current_best_index = max(
            range(population_size),
            key=lambda i: fitness_results[i]["fitness"]
        )

        if fitness_results[current_best_index]["fitness"] > best_result["fitness"]:
            best_candidate = population[current_best_index].copy()
            best_result = fitness_results[current_best_index].copy()

        history.append(best_result["makespan"])

        if (iteration + 1) % 10 == 0:
            print(
                f"Iteration {iteration + 1}/{iterations} | "
                f"Best Makespan: {best_result['makespan']}"
            )

    return {
        "best_candidate": best_candidate,
        "best_schedule": best_result["schedule"],
        "best_makespan": best_result["makespan"],
        "best_fitness": best_result["fitness"],
        "history": history
    }
