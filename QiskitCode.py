#initialization
import matplotlib.pyplot as plt
import numpy as np
import math

# importing Qiskit
from qiskit import IBMQ, Aer, transpile, execute
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.providers.ibmq import least_busy

# import basic plot tools
from qiskit.visualization import plot_histogram

from qiskit.circuit.library import MCMT, MCMTVChain, Diagonal

def Initialize_S(qc, first, last):
    """Apply a H-gate to 'qubits' in qc"""
    for i in range(last - first):
        qc.h(qc.qubits[i])
    return qc

#######################################################################################################
def Diffuser(nqubits):
    qc = QuantumCircuit(nqubits)
    # Apply transformation |s> -> |00..0> (H-gates)
    for qubit in range(nqubits):
        qc.h(qubit)
    # Apply transformation |00..0> -> |11..1> (X-gates)
    for qubit in range(nqubits):
        qc.x(qubit)
    # Do multi-controlled-Z gate
    qc.h(nqubits-1)
    qc.mct(list(range(nqubits-1)), nqubits-1)  # multi-controlled-toffoli
    qc.h(nqubits-1)
    # Apply transformation |11..1> -> |00..0>
    for qubit in range(nqubits):
        qc.x(qubit)
    # Apply transformation |00..0> -> |s>
    for qubit in range(nqubits):
        qc.h(qubit)
    # We will return the diffuser as a gate
    U_s = qc.to_gate()
    U_s.name = "U$_s$"
    return U_s

def CreateOracle(messages, n):
    diagonal = [1]*(2**n)
    #print('diagonal = ', diagonal)
    for message in messages:
        diagonal[int(message, 2)] = -1
        #print('message =', int(message, 2))
    return diagonal

def GroverOracle(n, messages, print_solutions=False):
    
    nsolutions = len(messages)
    diagonal= CreateOracle(messages, n)
    #print(diagonal)
    oracle_gate = Diagonal(diagonal)
    oracle_gate.name = "Oracle\nn=%i" % (n)
    if print_solutions:
        print("Solutions:")
        for idx, e in enumerate(diagonal):
            if e < 1:
                print("|%s>" % format(idx, "0%ib" % n))
    return oracle_gate

def AppendOracle(qc, oracle):
    array = []
    for n in range(len(qc.qubits)):
        array.append(n)
    qc.append(oracle, array)
    
def AppendDiffuser(qc, nqubits):
    array = []
    for n in range(nqubits):
        array.append(n)
    qc.append(Diffuser(nqubits), array)

##############################################################################################################3


def FindAvailability(calendar):
    i = 0
    array = []
    for n in calendar:
        if n == "1":
            array.append(i)
        i += 1
    print("indexes ", array)
    return array

def ApplyAvailabilityToQC(qc, array):
    for i in array:
        qc.z(i)

def CreateBellPairCircuit():
    """
    Returns:
        QuantumCircuit: Circuit that produces a Bell pair
    """
    qc = QuantumCircuit(2, name="Charlie")
    qc.h(1)
    qc.cx(1, 0)
    return qc

def CreateBellPair(qc):
    """
    Returns:
        QuantumCircuit: Circuit that produces a Bell pair
    """
    qc.h(1)
    qc.cx(1, 0)

    
def BellMeasurement(qc, target, control):
    qc.cx(target, control)
    qc.h(target)
    
def encodeMessage(qc, qubit, msg):
    """Encodes a two-bit message on qc using the superdense coding protocol
    Args:
        qc (QuantumCircuit): Circuit to encode message on
        qubit (int): Which qubit to add the gate to
        msg (str): Two-bit message to send
    Returns:
        QuantumCircuit: Circuit that, when decoded, will produce msg
    Raises:
        ValueError if msg is wrong length or contains invalid characters
    """
    if len(msg) != 2 or not set(msg).issubset({"0","1"}):
        raise ValueError(f"message '{msg}' is invalid")
    if msg[1] == "1":
        qc.x(qubit)
    if msg[0] == "1":
        qc.z(qubit)



calendar_a = "1001"

nqubits_a = len(calendar_a)

# availability_a = FindAvailability(calendar_a)

qc_a = QuantumCircuit(nqubits_a, name = "Alice")
Initialize_S(qc_a, 0, 4)


# ApplyAvailabilityToQC(qc_a, availability_a)
qc_a.barrier()

oracle = GroverOracle(nqubits_a, calendar_a, print_solutions=True)
AppendOracle(qc_a, oracle)

qc_a.barrier()
AppendDiffuser(qc_a, nqubits_a)

qc_a.measure_all()

qc_a.draw("mpl")

# Simulate and plot results
qasm_simulator = Aer.get_backend('qasm_simulator')
transpiled_qc = transpile(qc_a, qasm_simulator)
result = qasm_simulator.run(transpiled_qc).result()
plot_histogram(result.get_counts())