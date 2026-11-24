
def calculate_machine_utilization(schedule):
    """Calculate machine utilization using overall makespan."""

    if not schedule:
        return {}

    overall_makespan = max(
        operation["end"] for operation in schedule
    )

    machine_working_time = {}

    for operation in schedule:
        machine = operation["machine"]

        machine_working_time[machine] = (
            machine_working_time.get(machine, 0)
            + operation["duration"]
        )

    results = {}

    for machine, working_time in machine_working_time.items():

        utilization = (
            working_time / overall_makespan
        ) * 100 if overall_makespan > 0 else 0

        results[machine] = {
            "working_time": working_time,
            "completion_time": overall_makespan,
            "utilization": round(utilization, 2)
        }

    return results
