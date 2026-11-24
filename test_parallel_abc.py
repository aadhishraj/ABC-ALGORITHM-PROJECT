
import random

from src.scheduler.data_loader import load_jobs
from src.abc_algorithm.abc import run_abc
from src.abc_algorithm.parallel_abc import run_parallel_abc


def main():
    jobs = load_jobs("data/jobs.json")

    # Run sequential ABC with a fixed random seed
    random.seed(42)
    sequential_result = run_abc(
        jobs,
        population_size=10,
        iterations=50,
        limit=5
    )

    # Run parallel ABC with the same random seed
    random.seed(42)
    parallel_result = run_parallel_abc(
        jobs,
        population_size=10,
        iterations=50,
        limit=5,
        workers=4
    )

    print("\n========== COMPARISON ==========")
    print("Sequential Makespan:", sequential_result["best_makespan"])
    print("Parallel Makespan:", parallel_result["best_makespan"])

    print(
        "Makespans Match:",
        sequential_result["best_makespan"]
        == parallel_result["best_makespan"]
    )

    print("\nParallel ABC completed successfully!")


if __name__ == "__main__":
    main()
