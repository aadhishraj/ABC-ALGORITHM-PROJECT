
from multiprocessing import Pool, cpu_count

from src.abc_algorithm.fitness import evaluate_candidate


def _evaluate_single_candidate(args):
    """Evaluate one candidate inside a worker process."""
    jobs, candidate = args
    return evaluate_candidate(jobs, candidate)


def parallel_evaluate_population(jobs, population, workers=None):
    """Evaluate population candidates using multiple processes."""

    if workers is None:
        workers = cpu_count()

    tasks = [(jobs, candidate) for candidate in population]

    with Pool(processes=workers) as pool:
        results = pool.map(_evaluate_single_candidate, tasks)

    return results
