
import matplotlib.pyplot as plt
from pathlib import Path
from multiprocessing import freeze_support

from src.scheduler.data_loader import load_jobs
from src.abc_algorithm.abc import run_abc
from src.abc_algorithm.parallel_abc import run_parallel_abc


def main():
    # Load dataset
    jobs = load_jobs("data/large_jobs.json")

    # Run Sequential ABC
    print("Running Sequential ABC...")
    sequential_result = run_abc(
        jobs,
        population_size=50,
        iterations=100,
        limit=5
    )

    # Run Parallel ABC
    print("\nRunning Parallel ABC...")
    parallel_result = run_parallel_abc(
        jobs,
        population_size=50,
        iterations=100,
        limit=5,
        workers=4
    )

    # Extract convergence history
    sequential_history = sequential_result["history"]
    parallel_history = parallel_result["history"]

    # Create output directory
    output_dir = Path("results/charts")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Plot convergence graph
    plt.figure(figsize=(10, 6))

    plt.plot(
        range(1, len(sequential_history) + 1),
        sequential_history,
        label="Sequential ABC"
    )

    plt.plot(
        range(1, len(parallel_history) + 1),
        parallel_history,
        label="Parallel ABC"
    )

    plt.xlabel("Iterations")
    plt.ylabel("Best Makespan")
    plt.title("Convergence Comparison of Sequential and Parallel ABC")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(
        output_dir / "convergence_comparison.png",
        dpi=300
    )

    plt.close()

    print("\nConvergence graph generated successfully!")
    print("Saved at: results/charts/convergence_comparison.png")
    print("Sequential best makespan:", sequential_result["best_makespan"])
    print("Parallel best makespan:", parallel_result["best_makespan"])


if __name__ == "__main__":
    freeze_support()
    main()
