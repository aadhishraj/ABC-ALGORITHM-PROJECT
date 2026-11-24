from src.scheduler.data_loader import load_jobs, validate_jobs

jobs = load_jobs("data/jobs.json")

validate_jobs(jobs)

print("Dataset loaded successfully!\n")

for job, operations in jobs.items():
    print(job, ":", operations)

print("\nTotal jobs:", len(jobs))

machines = {
    operation["machine"]
    for operations in jobs.values()
    for operation in operations
}

print("Total machines:", len(machines))
print("Machines:", sorted(machines))
print("\nDataset validation passed!")
