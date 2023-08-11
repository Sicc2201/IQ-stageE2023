#########################################################################
"""
Title: InitClass.py
Author: Christopher Sicotte
Date of creation: 31/07/23
Last edited: 10/08/23

"""
#########################################################################
""""
This is the constructor of the Init class

Contexte:

The goal of this class is to have a general object that can be easily accessible in any main file and get all the main info

Attributes:

- name -> name
- nqubits -> number of qubits in its register
- layout -> dictionnary for its layouts
- cm -> coupling map (None by default)
- map -> array that stock the layout for the job (empty by default)
- qr -> quantum register
- qc -> quantum circuit
- qasmPath -> path to participant's qasm files folder
- qasm -> array that contains the protocols and their associated timstep as a dictionnary

functions:

- init -> create the participant
- str -> allow to print the participant

"""
########################################################################

# importing Qiskit
from qiskit import QuantumCircuit, QuantumRegister

# constructor for the "Participant" class
class Participant:
    def __init__(self, pname, nqubits, qasmPath = "", q5_order = [], q7_order = [], q16_order = [], q27_order = []):
        self.name = pname
        self.nqubits = nqubits
        self.layout = {"5q": q5_order,"7q": q7_order, "16q": q16_order, "27q": q27_order}
        self.cm = None
        self.map = []
        self.qr = QuantumRegister(nqubits, name = pname)
        self.qc = QuantumCircuit(nqubits)
        self.qasmPath = qasmPath
        self.qasm = []
        
    # function that allows to print the participant (why not)    
    def __str__(self):                            
        return f"{self.name} ({self.nqubits}qubits), global mapping {self.map}"   # print the name, the number of qubits and the mapping 