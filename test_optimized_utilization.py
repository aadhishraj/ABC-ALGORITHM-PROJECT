
from src.scheduler.data_loader import load_jobs
from src.scheduler.resource_metrics import calculate_machine_utilization
from src.abc_algorithm.abc import run_abc

# Load industrial scheduling dataset
jobs = load_jobs("data/large_jobs.json")

# Run Sequential ABC
print("Optimizing schedule using ABC...")

result = run_abc(
    jobs,
    population_size=50,
    iterations=100,
    limit=5
)

# Get the optimized schedule
best_schedule = result["best_schedule"]

# Calculate utilization using optimized schedule
metrics = calculate_machine_utilization(best_schedule)

print("\nOPTIMIZED SCHEDULE RESULTS")
print("Best Makespan:", result["best_makespan"])

print("\nMACHINE UTILIZATION")

for machine, values in metrics.items():
    print(f"\n{machine}")
    print("Working Time:", values["working_time"])
    print("Completion Time:", values["completion_time"])
    print("Utilization:", values["utilization"], "%")

# Calculate average machine utilization
average_utilization = sum(
    values["utilization"] for values in metrics.values()
) / len(metrics)

print("\nAverage Machine Utilization:", round(average_utilization, 2), "%")
