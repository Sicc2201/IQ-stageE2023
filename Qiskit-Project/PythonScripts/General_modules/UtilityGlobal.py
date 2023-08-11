#########################################################################
"""
Title: UtilityGlobal.py
Author: Christopher Sicotte
Date of creation: 31/07/23
Last edited: 10/08/23

"""
#########################################################################
""""
This file manage the creation of the global circuit

Contexte:

Making a global circuit made by the participants allow to manage all the circuits in one by composing the global circuit with a sub quantum
circuits when we want to apply the protocol of a participant.

Algorithm:

- create quantum registers for every participants
- create a classical register
- create global circuit from participants registers and classical one
- return global circuit

"""
########################################################################

# importing
from qiskit import QuantumCircuit, ClassicalRegister
import numpy as np  

# create the global circuit for the inter-participants communications
def CreateQuantumCircuit(participants, n_bits):
    if not participants:
        raise Exception("You must create participants and add them to an array as parameter")
    else:
        areEqual = True
        # check if the participants have the same number of qubits
        for i in range(len(participants) - 1):
            if participants[i].nqubits != participants[i + 1].nqubits:
                areEqual = False
        if areEqual:  
            cr = ClassicalRegister(n_bits)    # classical register to store the measurement
            # if 2 participants
            if len(participants) == 2:
                qc = QuantumCircuit(participants[0].qr, participants[1].qr, cr) #create circuit with registers
            # if 3 participants
            elif len(participants) == 3:
                qc = QuantumCircuit(participants[0].qr, participants[1].qr, participants[2].qr, cr)
            # if 4 participants
            elif len(participants) == 4:
                qc = QuantumCircuit(participants[0].qr, participants[1].qr, participants[2].qr, participants[3].qr, cr)
        else:
            raise Exception("participants must have the same amount of qubits")
    return qc
