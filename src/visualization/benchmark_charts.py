
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Load benchmark results
df = pd.read_csv("results/benchmark_results.csv")

output_dir = Path("results/charts")
output_dir.mkdir(parents=True, exist_ok=True)

# 1. Execution time comparison
plt.figure(figsize=(9, 5))

plt.bar(
    df["run"] - 0.2,
    df["sequential_time"],
    width=0.4,
    label="Sequential ABC"
)

plt.bar(
    df["run"] + 0.2,
    df["parallel_time"],
    width=0.4,
    label="Parallel ABC"
)

plt.xlabel("Benchmark Run")
plt.ylabel("Execution Time (seconds)")
plt.title("Sequential vs Parallel Execution Time")
plt.xticks(df["run"])
plt.legend()
plt.tight_layout()
plt.savefig(output_dir / "execution_time.png", dpi=300)
plt.close()

# 2. Makespan comparison
plt.figure(figsize=(9, 5))

plt.plot(
    df["run"],
    df["sequential_makespan"],
    marker="o",
    label="Sequential ABC"
)

plt.plot(
    df["run"],
    df["parallel_makespan"],
    marker="s",
    label="Parallel ABC"
)

plt.xlabel("Benchmark Run")
plt.ylabel("Makespan")
plt.title("Sequential vs Parallel Makespan")
plt.xticks(df["run"])
plt.legend()
plt.tight_layout()
plt.savefig(output_dir / "makespan_comparison.png", dpi=300)
plt.close()

# 3. Speedup comparison
plt.figure(figsize=(9, 5))

plt.bar(df["run"], df["speedup"])

plt.axhline(
    y=1,
    linestyle="--",
    label="Equal execution time"
)

plt.xlabel("Benchmark Run")
plt.ylabel("Speedup")
plt.title("Parallel ABC Speedup")
plt.xticks(df["run"])
plt.legend()
plt.tight_layout()
plt.savefig(output_dir / "speedup.png", dpi=300)
plt.close()

print("All benchmark charts generated successfully!")
print("Charts saved in:", output_dir)
