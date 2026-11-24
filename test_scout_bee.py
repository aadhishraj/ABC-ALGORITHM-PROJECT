from src.scheduler.data_loader import load_jobs
from src.abc_algorithm.population import generate_population
from src.abc_algorithm.fitness import evaluate_candidate
from src.abc_algorithm.scout_bee import scout_bee_phase

jobs = load_jobs("data/jobs.json")

population = generate_population(jobs, population_size=10)

fitness_results = [
    evaluate_candidate(jobs, candidate)
    for candidate in population
]

# Simulate candidates reaching the stagnation limit
trial_counts = [0] * len(population)
trial_counts[0] = 5

print("Trial count before:", trial_counts[0])

population, fitness_results, trial_counts = scout_bee_phase(
    jobs, population, fitness_results, trial_counts, limit=5
)

print("Trial count after:", trial_counts[0])
print("Best makespan:", min(r["makespan"] for r in fitness_results))
print("\nScout Bee phase completed!")