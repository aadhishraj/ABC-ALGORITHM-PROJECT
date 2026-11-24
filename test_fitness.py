
from src.scheduler.data_loader import load_jobs
from src.abc_algorithm.fitness import evaluate_candidate

jobs = load_jobs("data/jobs.json")

candidate_1 = ["J1", "J2", "J3", "J1", "J2", "J3"]

candidate_2 = ["J2", "J1", "J3", "J2", "J3", "J1"]

candidates = [candidate_1, candidate_2]

for index, candidate in enumerate(candidates, start=1):

    result = evaluate_candidate(jobs, candidate)

    print(f"\nCandidate {index}")
    print("Valid:", result["valid"])
    print("Makespan:", result["makespan"])
    print("Fitness:", round(result["fitness"], 4))

print("\nFitness evaluation completed!")
