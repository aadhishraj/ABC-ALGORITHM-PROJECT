
from src.scheduler.data_loader import load_jobs
from src.abc_algorithm.population import generate_population
from src.abc_algorithm.fitness import evaluate_candidate

jobs = load_jobs("data/jobs.json")

population = generate_population(jobs, population_size=10)

print("Generated Population:\n")

for index, candidate in enumerate(population, start=1):

    result = evaluate_candidate(jobs, candidate)

    print(f"Candidate {index}: {candidate}")
    print("Makespan:", result["makespan"])
    print("Fitness:", round(result["fitness"], 4))
    print("Valid:", result["valid"])
    print("-" * 40)

print("Total candidates:", len(population))
