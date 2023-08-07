from qiskit import Aer, execute
from qiskit.visualization import plot_histogram

def RunSimulator(transpiled_qc, fileName = "job_results"):
    backend = Aer.get_backend('qasm_simulator') # run on a simulator
    # transpiled_qc = transpile(qc, backend)
    job = backend.run(transpiled_qc)            # run the job on the given backend

    plot_histogram(job.result().get_counts(), filename = "images/" + fileName + ".png")   # uncomment to plot the result


def RunBackend(backend, transpiled_qc, fileName = "job_results"):
    # transpiled_qc = transpile(qc, backend)
    job = backend.run(transpiled_qc)            # run the job on the given backend

    plot_histogram(job.result().get_counts(), filename = "images/" + fileName + ".png")   # uncomment to plot the result