from src.scheduler.data_loader import load_jobs
from src.abc_algorithm.population import generate_population
from src.abc_algorithm.fitness import evaluate_candidate
from src.abc_algorithm.onlooker_bee import onlooker_bee_phase

# Load dataset
jobs = load_jobs("data/jobs.json")

# Generate population
population = generate_population(jobs, population_size=10)

# Evaluate initial population
fitness_results = [
    evaluate_candidate(jobs, candidate)
    for candidate in population
]

best_before = min(result["makespan"] for result in fitness_results)

# Run Onlooker Bee phase
population, fitness_results = onlooker_bee_phase(
    jobs, population, fitness_results
)

best_after = min(result["makespan"] for result in fitness_results)

print("Best makespan before:", best_before)
print("Best makespan after:", best_after)
print("\nOnlooker Bee phase completed!")