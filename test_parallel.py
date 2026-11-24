



from src.scheduler.data_loader import load_jobs
from src.abc_algorithm.population import generate_population
from src.abc_algorithm.fitness import evaluate_candidate
from src.abc_algorithm.parallel_evaluator import parallel_evaluate_population


def main():
    jobs = load_jobs("data/jobs.json")

    population = generate_population(jobs, population_size=10)

    # Sequential evaluation
    sequential_results = [
        evaluate_candidate(jobs, candidate)
        for candidate in population
    ]

    # Parallel evaluation
    parallel_results = parallel_evaluate_population(
        jobs, population, workers=4
    )

    print("Sequential evaluation results:")
    print([r["makespan"] for r in sequential_results])

    print("\nParallel evaluation results:")
    print([r["makespan"] for r in parallel_results])

    # Verify both methods produce identical results
    sequential_makespans = [r["makespan"] for r in sequential_results]
    parallel_makespans = [r["makespan"] for r in parallel_results]

    print("\nResults match:", sequential_makespans == parallel_makespans)
    print("\nParallel evaluation test completed!")


if __name__ == "__main__":
    main()
