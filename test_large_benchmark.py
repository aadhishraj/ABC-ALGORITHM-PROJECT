
from src.scheduler.data_loader import load_jobs
from src.abc_algorithm.benchmark import benchmark_algorithms


def main():
    jobs = load_jobs("data/large_jobs.json")

    results = benchmark_algorithms(
        jobs,
        population_size=50,
        iterations=100,
        limit=10,
        workers=4,
        repetitions=3
    )

    print("\n========== LARGE DATASET BENCHMARK ==========")
    print("Jobs:", len(jobs))
    print("Total operations:", sum(len(ops) for ops in jobs.values()))

    print(f"\nSequential Average Time: {results['sequential_avg']:.4f} seconds")
    print(f"Parallel Average Time: {results['parallel_avg']:.4f} seconds")
    print(f"Speedup: {results['speedup']:.2f}x")

    print("Sequential Makespan:", results["sequential_makespan"])
    print("Parallel Makespan:", results["parallel_makespan"])

    print("\nLarge dataset benchmark completed!")


if __name__ == "__main__":
    main()

