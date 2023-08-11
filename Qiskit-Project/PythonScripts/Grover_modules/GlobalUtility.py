#########################################################################
"""
Title: GlobalUtility.py
Author: Christopher Sicotte
Date of creation: 31/07/23
Last edited: 11/08/23

"""
#########################################################################
""""
This file manage global protocols that must interact with several participants

Functions:

- CreateInitialCircuit(p, nqubits)

- Init_S_state(qc, backend, p)

"""
########################################################################

# imports
from qiskit import QuantumCircuit, transpile

# create a quantum circuit that will create the |s> state for a participant
def CreateInitialCircuit(p, nqubits):
    init_qc = QuantumCircuit(nqubits) # create empty circuit
    for q in p.map[0:-1]:  # place the gates according to the right mapping
        init_qc.h(q)       # add an hadamard gate on every working qubits of a participant
    return init_qc # return the circuit

# create the |s> state circuit, transpile it then add it to the global circuit
def Init_S_state(qc, backend, p):
    init = CreateInitialCircuit(p, qc.num_qubits) # create the |s> state for a participant quantum circuit
    tr_init = transpile(init, backend) # transpile the circuit
    qc.compose(tr_init, inplace = True) # add the transpiled circuit to the global one
    qc.barrier()    