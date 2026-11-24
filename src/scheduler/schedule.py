def create_schedule(jobs, operation_order):
    """
    Generate a valid job-shop schedule using
    an operation-based sequence.
    """

    job_next_operation = {job: 0 for job in jobs}
    job_available_time = {job: 0 for job in jobs}
    machine_available_time = {}

    schedule = []

    for job in operation_order:

        operation_index = job_next_operation[job]
        operation = jobs[job][operation_index]

        machine = operation["machine"]
        duration = operation["duration"]

        start_time = max(
            job_available_time[job],
            machine_available_time.get(machine, 0)
        )

        end_time = start_time + duration

        schedule.append({
            "job": job,
            "operation": operation_index + 1,
            "machine": machine,
            "start": start_time,
            "end": end_time,
            "duration": duration
        })

        job_available_time[job] = end_time
        machine_available_time[machine] = end_time
        job_next_operation[job] += 1

    return schedule


def calculate_makespan(schedule):
    """Calculate total production completion time."""

    if not schedule:
        return 0

    return max(operation["end"] for operation in schedule)

def validate_schedule(jobs, schedule):
    """Check whether a schedule follows all job-shop constraints."""

    errors = []

    # 1. Check whether every operation is present exactly once
    expected_operations = sum(len(ops) for ops in jobs.values())

    if len(schedule) != expected_operations:
        errors.append("Incorrect number of scheduled operations.")

    scheduled_ids = [
        (item["job"], item["operation"])
        for item in schedule
    ]

    if len(scheduled_ids) != len(set(scheduled_ids)):
        errors.append("Duplicate operations found.")

    # 2. Check operation details and processing times
    for item in schedule:
        job = item["job"]
        operation_number = item["operation"]

        if job not in jobs:
            errors.append(f"Unknown job: {job}")
            continue

        if not 1 <= operation_number <= len(jobs[job]):
            errors.append(f"Invalid operation number for {job}.")
            continue

        original = jobs[job][operation_number - 1]

        if item["machine"] != original["machine"]:
            errors.append(f"Incorrect machine for {job}.")

        if item["duration"] != original["duration"]:
            errors.append(f"Incorrect duration for {job}.")

        if item["start"] < 0 or item["end"] != item["start"] + item["duration"]:
            errors.append(f"Invalid timing for {job}.")

    # 3. Check job operation order
    for job in jobs:
        operations = sorted(
            [item for item in schedule if item["job"] == job],
            key=lambda item: item["operation"]
        )

        for previous, current in zip(operations, operations[1:]):
            if current["operation"] != previous["operation"] + 1:
                errors.append(f"Missing operation in {job}.")
                continue

            if current["start"] < previous["end"]:
                errors.append(f"Job precedence conflict in {job}.")

    # 4. Check machine conflicts
    machines = set(item["machine"] for item in schedule)

    for machine in machines:
        machine_operations = sorted(
            [item for item in schedule if item["machine"] == machine],
            key=lambda item: item["start"]
        )

        for previous, current in zip(
            machine_operations, machine_operations[1:]
        ):
            if current["start"] < previous["end"]:
                errors.append(f"Machine conflict on {machine}.")

    return len(errors) == 0, errors
