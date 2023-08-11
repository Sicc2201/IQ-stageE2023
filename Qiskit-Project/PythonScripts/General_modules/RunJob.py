#########################################################################
"""
Title: RunJob.py
Author: Christopher Sicotte
Date of creation: 31/07/23
Last edited: 10/08/23

"""
#########################################################################
""""
This file manage and facilitate the execution of a job

Functions:

- RunSimulator(transpiled_qc)

- RunBackend(backend, transpiled_qc)

- SaveResults(job, fileName = "job_results")

"""
########################################################################

# imports
from qiskit import Aer
from qiskit.visualization import plot_histogram

# run the given job on the simulator
def RunSimulator(transpiled_qc):
    backend = Aer.get_backend('qasm_simulator') # run on a simulator
    job = backend.run(transpiled_qc)            # run the job on the given backend
    return job

# run the given job on the selected backed
def RunBackend(backend, transpiled_qc):
    print("Now waiting for the result on the backend")
    job = backend.run(transpiled_qc)            # run the job on the given backend
    return job

# plot and saves as a PNG the results of a given job
def SaveResults(job, fileName = "job_results"):
    plot_histogram(job.result().get_counts(), filename = "Images/" + fileName + ".png")
