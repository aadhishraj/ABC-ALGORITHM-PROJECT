
from src.scheduler.data_loader import load_jobs
from src.scheduler.schedule import (
    create_schedule,
    calculate_makespan,
    validate_schedule
)

jobs = load_jobs("data/jobs.json")

operation_order = ["J1", "J2", "J3", "J1", "J2", "J3"]

schedule = create_schedule(jobs, operation_order)

print("Schedule:")
for operation in schedule:
    print(operation)

print("\nMakespan:", calculate_makespan(schedule))

is_valid, errors = validate_schedule(jobs, schedule)

print("\nSchedule validation:", is_valid)

if errors:
    for error in errors:
        print(error)
else:
    print("All scheduling constraints satisfied!")
