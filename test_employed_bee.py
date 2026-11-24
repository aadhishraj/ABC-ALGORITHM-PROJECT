
from src.scheduler.data_loader import load_jobs
from src.abc_algorithm.population import generate_population
from src.abc_algorithm.fitness import evaluate_candidate
from src.abc_algorithm.employed_bee import employed_bee_phase

jobs = load_jobs("data/jobs.json")

population = generate_population(jobs, 10)

fitness_results = [
    evaluate_candidate(jobs, candidate)
    for candidate in population
]

print("Best makespan before:", min(
    result["makespan"] for result in fitness_results
))

population, fitness_results = employed_bee_phase(
    jobs, population, fitness_results
)

print("Best makespan after:", min(
    result["makespan"] for result in fitness_results
))

print("\nEmployed Bee phase completed!")
