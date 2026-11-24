
import streamlit as st
import matplotlib.pyplot as plt

from src.scheduler.data_loader import load_jobs
from src.scheduler.resource_metrics import calculate_machine_utilization
from src.abc_algorithm.abc import run_abc
from src.abc_algorithm.parallel_abc import run_parallel_abc


st.set_page_config(
    page_title="Parallel ABC Scheduler",
    page_icon="🏭",
    layout="wide"
)

st.title("🏭 Industrial Productivity Optimization")
st.subheader("Artificial Bee Colony Scheduling System")

st.sidebar.header("Algorithm Configuration")

algorithm = st.sidebar.selectbox(
    "Select Algorithm",
    ["Sequential ABC", "Parallel ABC"]
)

population_size = st.sidebar.slider(
    "Population Size", 10, 100, 50, 10
)

iterations = st.sidebar.slider(
    "Iterations", 10, 200, 100, 10
)

workers = st.sidebar.slider(
    "Number of Workers", 2, 8, 4
)

if st.button("Run Optimization", type="primary"):

    jobs = load_jobs("data/large_jobs.json")

    with st.spinner("Optimizing production schedule..."):

        if algorithm == "Sequential ABC":
            result = run_abc(
                jobs,
                population_size=population_size,
                iterations=iterations,
                limit=5
            )
        else:
            result = run_parallel_abc(
                jobs,
                population_size=population_size,
                iterations=iterations,
                limit=5,
                workers=workers
            )

        metrics = calculate_machine_utilization(
            result["best_schedule"]
        )

    st.success("Optimization completed!")

    # Performance metrics
    average_utilization = sum(
        item["utilization"] for item in metrics.values()
    ) / len(metrics)

    col1, col2, col3 = st.columns(3)

    col1.metric("Best Makespan", result["best_makespan"])
    col2.metric("Average Utilization", f"{average_utilization:.2f}%")
    col3.metric("Machines", len(metrics))

    # Convergence chart
    st.subheader("Optimization Convergence")

    fig, ax = plt.subplots(figsize=(10, 4))

    ax.plot(result["history"])
    ax.set_xlabel("Iteration")
    ax.set_ylabel("Best Makespan")
    ax.set_title("ABC Convergence")

    st.pyplot(fig)
    plt.close(fig)

    # Machine utilization chart
    st.subheader("Machine Utilization")

    machines = list(metrics.keys())
    values = [
        metrics[machine]["utilization"]
        for machine in machines
    ]

    fig, ax = plt.subplots(figsize=(10, 4))

    bars = ax.bar(machines, values)
    ax.bar_label(
        bars,
        labels=[f"{value:.2f}%" for value in values]
    )

    ax.set_ylabel("Utilization (%)")
    ax.set_ylim(0, 110)
    ax.set_title("Machine-wise Utilization")

    st.pyplot(fig)
    plt.close(fig)

    # Optimized schedule
    st.subheader("Optimized Production Schedule")

    st.dataframe(
        result["best_schedule"],
        use_container_width=True
    )

