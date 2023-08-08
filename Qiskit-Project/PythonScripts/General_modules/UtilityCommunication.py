# importing Qiskit
from qiskit import QuantumCircuit, ClassicalRegister

import numpy as np

#######################################################################################################    
    
#      Inter-participants communications 
    
#######################################################################################################   

# create the global circuit for the inter-participants communications
def CreateQuantumCircuit(backend, participants):
    if not participants:
        raise Exception("You must create participants and add them to an array as parameter")
    else:
        areEqual = True
        for i in range(len(participants) - 1):
            if participants[i].nqubits != participants[i + 1].nqubits:
                areEqual = False
        if areEqual:  
            nbWorkingQubits = 1
            cr = ClassicalRegister(nbWorkingQubits)    # classical register to store the measurement
            if len(participants) == 2:
                qc = QuantumCircuit(participants[0].qr, participants[1].qr, cr) #create circuit with registers
            elif len(participants) == 3:
                qc = QuantumCircuit(participants[0].qr, participants[1].qr, participants[2].qr, cr)
            elif len(participants) == 4:
                qc = QuantumCircuit(participants[0].qr, participants[1].qr, participants[2].qr, participants[3].qr, cr)
            
            # add the positions of participants in the circuit
            q = [i for i in range(participants[0].nqubits)]
            qubits = np.array(q)
            for i, p in enumerate(participants):
                nqubits = qubits + i * participants[0].nqubits
                p.qubits = nqubits
                qc.compose(p.qc, qubits = p.qubits, inplace = True)
        else:
            raise Exception("participants must have the same amount of qubits")
    return qc
