
from src.scheduler.schedule import (
    create_schedule,
    calculate_makespan,
    validate_schedule
)


def evaluate_candidate(jobs, candidate):
    """
    Generate and evaluate a candidate schedule.
    Higher fitness represents a better schedule.
    """

    schedule = create_schedule(jobs, candidate)

    is_valid, errors = validate_schedule(jobs, schedule)

    if not is_valid:
        return {
            "fitness": 0,
            "makespan": float("inf"),
            "schedule": None,
            "valid": False,
            "errors": errors
        }

    makespan = calculate_makespan(schedule)

    fitness = 1 / (1 + makespan)

    return {
        "fitness": fitness,
        "makespan": makespan,
        "schedule": schedule,
        "valid": True,
        "errors": []
    }
