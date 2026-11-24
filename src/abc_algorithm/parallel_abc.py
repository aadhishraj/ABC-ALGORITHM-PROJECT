
import random
from multiprocessing import Pool, cpu_count

from src.abc_algorithm.population import generate_population, generate_candidate
from src.abc_algorithm.fitness import evaluate_candidate
from src.abc_algorithm.neighborhood import generate_neighbor


def _evaluate_task(args):
    """Worker function for parallel fitness evaluation."""
    jobs, candidate = args
    return evaluate_candidate(jobs, candidate)


def run_parallel_abc(
    jobs,
    population_size=10,
    iterations=50,
    limit=5,
    workers=None
):
    """Run ABC with parallel candidate evaluation."""

    if workers is None:
        workers = cpu_count()

    population = generate_population(jobs, population_size)

    history = []
    trial_counts = [0] * population_size

    with Pool(processes=workers) as pool:

        # Initial parallel evaluation
        tasks = [(jobs, candidate) for candidate in population]
        fitness_results = pool.map(_evaluate_task, tasks)

        # Initialize global best
        best_index = max(
            range(population_size),
            key=lambda i: fitness_results[i]["fitness"]
        )

        best_candidate = population[best_index].copy()
        best_result = fitness_results[best_index].copy()

        for iteration in range(iterations):

            # EMPLOYED BEE PHASE
            neighbors = [
                generate_neighbor(candidate)
                for candidate in population
            ]

            tasks = [(jobs, candidate) for candidate in neighbors]
            neighbor_results = pool.map(_evaluate_task, tasks)

            for i in range(population_size):
                if neighbor_results[i]["fitness"] > fitness_results[i]["fitness"]:
                    population[i] = neighbors[i]
                    fitness_results[i] = neighbor_results[i]
                    trial_counts[i] = 0
                else:
                    trial_counts[i] += 1

            # ONLOOKER BEE PHASE
            weights = [result["fitness"] for result in fitness_results]

            selected_indices = random.choices(
                range(population_size),
                weights=weights,
                k=population_size
            )

            onlooker_neighbors = [
                generate_neighbor(population[index])
                for index in selected_indices
            ]

            tasks = [(jobs, candidate) for candidate in onlooker_neighbors]
            onlooker_results = pool.map(_evaluate_task, tasks)

            for index, neighbor, result in zip(
                selected_indices, onlooker_neighbors, onlooker_results
            ):
                if result["fitness"] > fitness_results[index]["fitness"]:
                    population[index] = neighbor
                    fitness_results[index] = result
                    trial_counts[index] = 0
                else:
                    trial_counts[index] += 1

            # SCOUT BEE PHASE
            scout_indices = [
                i for i in range(population_size)
                if trial_counts[i] >= limit
            ]

            scout_candidates = [
                generate_candidate(jobs)
                for _ in scout_indices
            ]

            tasks = [(jobs, candidate) for candidate in scout_candidates]
            scout_results = pool.map(_evaluate_task, tasks)

            for index, candidate, result in zip(
                scout_indices, scout_candidates, scout_results
            ):
                population[index] = candidate
                fitness_results[index] = result
                trial_counts[index] = 0

            # UPDATE GLOBAL BEST
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
                    f"Parallel Iteration {iteration + 1}/{iterations} | "
                    f"Best Makespan: {best_result['makespan']}"
                )

    return {
        "best_candidate": best_candidate,
        "best_schedule": best_result["schedule"],
        "best_makespan": best_result["makespan"],
        "best_fitness": best_result["fitness"],
        "history": history
    }
