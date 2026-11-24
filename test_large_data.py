from src.scheduler.data_loader import load_jobs, validate_jobs

jobs = load_jobs("data/large_jobs.json")

validate_jobs(jobs)

total_operations = sum(len(operations) for operations in jobs.values())

machines = set(
    operation["machine"]
    for operations in jobs.values()
    for operation in operations
)

print("Dataset validation passed!")
print("Total jobs:", len(jobs))
print("Total machines:", len(machines))
print("Total operations:", total_operations)
print("Machines:", sorted(machines))