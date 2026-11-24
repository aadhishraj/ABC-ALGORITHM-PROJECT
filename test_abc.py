from src.scheduler.schedule import validate_schedule
from src.scheduler.data_loader import load_jobs
from src.abc_algorithm.abc import run_abc

# Load scheduling problem
jobs = load_jobs("data/jobs.json")

# Run sequential ABC
result = run_abc(
    jobs,
    population_size=10,
    iterations=50,
    limit=5
)

print("\n========== ABC RESULTS ==========")
print("Best Makespan:", result["best_makespan"])
print("Best Fitness:", result["best_fitness"])
print("Best Candidate:", result["best_candidate"])

print("\nBest Schedule:")
for operation in result["best_schedule"]:
    print(operation)

print("\nTotal Iterations:", len(result["history"]))
print("\nABC Algorithm completed successfully!")

is_valid, errors = validate_schedule(
    jobs,
    result["best_schedule"]
)

print("\nSchedule Valid:", is_valid)
print("Validation Errors:", errors)