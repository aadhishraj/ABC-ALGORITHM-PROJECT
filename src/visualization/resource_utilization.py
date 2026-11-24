
import matplotlib.pyplot as plt
from pathlib import Path

from src.scheduler.data_loader import load_jobs
from src.scheduler.resource_metrics import calculate_machine_utilization
from src.abc_algorithm.abc import run_abc


def main():
    jobs = load_jobs("data/large_jobs.json")

    print("Optimizing schedule using ABC...")

    result = run_abc(
        jobs,
        population_size=50,
        iterations=100,
        limit=5
    )

    # Use the optimized schedule
    metrics = calculate_machine_utilization(
        result["best_schedule"]
    )

    machines = list(metrics.keys())
    utilization = [
        metrics[machine]["utilization"]
        for machine in machines
    ]

    average = sum(utilization) / len(utilization)

    output_dir = Path("results/charts")
    output_dir.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(9, 5))

    bars = plt.bar(machines, utilization)

    plt.bar_label(
        bars,
        labels=[f"{value:.2f}%" for value in utilization],
        padding=3
    )

    plt.xlabel("Machines")
    plt.ylabel("Utilization (%)")
    plt.title("Optimized Machine Utilization - ABC Algorithm")
    plt.ylim(0, 110)
    plt.grid(axis="y", linestyle="--", alpha=0.5)

    plt.tight_layout()
    plt.savefig(
        output_dir / "optimized_machine_utilization.png",
        dpi=300
    )
    plt.close()

    print("\nOptimized Makespan:", result["best_makespan"])
    print("Average Machine Utilization:", round(average, 2), "%")
    print("Chart saved: results/charts/optimized_machine_utilization.png")


if __name__ == "__main__":
    main()
