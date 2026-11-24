
from src.scheduler.data_loader import load_jobs
from src.abc_algorithm.benchmark import benchmark_algorithms


def main():
    jobs = load_jobs("data/jobs.json")

    results = benchmark_algorithms(
        jobs,
        population_size=10,
        iterations=50,
        limit=5,
        workers=4,
        repetitions=3
    )

    print("\n========== BENCHMARK RESULTS ==========")

    print(
        f"Sequential Average Time: "
        f"{results['sequential_avg']:.4f} seconds"
    )

    print(
        f"Parallel Average Time: "
        f"{results['parallel_avg']:.4f} seconds"
    )

    print(f"Speedup: {results['speedup']:.2f}x")

    print(
        f"Sequential Best Makespan: "
        f"{results['sequential_makespan']}"
    )

    print(
        f"Parallel Best Makespan: "
        f"{results['parallel_makespan']}"
    )

    print("\nBenchmark completed successfully!")


if __name__ == "__main__":
    main()
