import json
from pathlib import Path


def load_jobs(file_path):
    """Load job-shop scheduling data from a JSON file."""

    path = Path(file_path)

    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    return data["jobs"]


def validate_jobs(jobs):
    """Validate jobs, operations, machines and durations."""

    if not jobs:
        raise ValueError("No jobs found.")

    for job_name, operations in jobs.items():

        if not operations:
            raise ValueError(f"{job_name} has no operations.")

        for operation in operations:

            if "machine" not in operation or "duration" not in operation:
                raise ValueError(f"Invalid operation in {job_name}.")

            if not isinstance(operation["duration"], (int, float)):
                raise ValueError("Duration must be numeric.")

            if operation["duration"] <= 0:
                raise ValueError("Duration must be positive.")

    return True