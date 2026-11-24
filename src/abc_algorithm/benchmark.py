
import csv
import random
import time
from pathlib import Path
from statistics import mean

from src.abc_algorithm.abc import run_abc
from src.abc_algorithm.parallel_abc import run_parallel_abc


def benchmark_algorithms(
    jobs,
    population_size=10,
    iterations=50,
    limit=5,
    workers=4,
    repetitions=3
):
    sequential_times = []
    parallel_times = []
    sequential_makespans = []
    parallel_makespans = []
    run_records = []

    for run in range(repetitions):
        print(f"\nBenchmark run {run + 1}/{repetitions}")

        # Sequential ABC
        random.seed(42 + run)
        start = time.perf_counter()

        sequential_result = run_abc(
            jobs, population_size, iterations, limit
        )

        sequential_time = time.perf_counter() - start

        # Parallel ABC
        random.seed(42 + run)
        start = time.perf_counter()

        parallel_result = run_parallel_abc(
            jobs, population_size, iterations, limit, workers
        )

        parallel_time = time.perf_counter() - start

        sequential_times.append(sequential_time)
        parallel_times.append(parallel_time)

        sequential_makespans.append(
            sequential_result["best_makespan"]
        )
        parallel_makespans.append(
            parallel_result["best_makespan"]
        )

        run_records.append({
            "run": run + 1,
            "sequential_time": sequential_time,
            "parallel_time": parallel_time,
            "sequential_makespan": sequential_result["best_makespan"],
            "parallel_makespan": parallel_result["best_makespan"],
            "speedup": sequential_time / parallel_time
        })

    sequential_avg = mean(sequential_times)
    parallel_avg = mean(parallel_times)

    # Save individual benchmark results
    output_path = Path("results/benchmark_results.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "run",
                "sequential_time",
                "parallel_time",
                "sequential_makespan",
                "parallel_makespan",
                "speedup"
            ]
        )

        writer.writeheader()
        writer.writerows(run_records)

    return {
        "sequential_avg": sequential_avg,
        "parallel_avg": parallel_avg,
        "speedup": sequential_avg / parallel_avg,
        "sequential_makespan": min(sequential_makespans),
        "parallel_makespan": min(parallel_makespans),
        "repetitions": repetitions,
        "csv_path": str(output_path)
    }
