#########################################################################
""""
General example of the program with 3 participants.

Contexte:

The goal is to have 2 participants that has random protocol and layout has an example.

Algorithme:

let the 2 participant (Alice, Bob). They have protocols at different time steps and layout to them.
The circuit begin in the |s> state.
The program will Initialize all the necessary, then we will apply all the protocols for the participants and swaps qubits


"""
########################################################################

from General_modules import QasmFileManager as qasm
from General_modules import ProtocolManager as protocol
from General_modules import OutputManager as output
from General_modules import Initialize

import sys 
    
def main():

    # initialaize all the dependencies for the program and return an object with all the necessities
    init = Initialize.InitiateOperation(sys.argv[0])

    commFiles = qasm.GetCommunicationQasmFiles("QasmFiles/" + init.arg + "/communication") # get communication files folder
    for p in init.participants:
      print(p)

    alice = init.participants[0]

    protocol.ApplyProtocol(init.backend, init.qc, init.participants, 1)      # Apply protocols to the circuit at timstep 1

    protocol.ApplyCommunication(init.qc, init.backend, init.arg, "qasm-swap.txt") # Swap the qubits of 2 participants

    protocol.ApplyProtocol(init.backend, init.qc, init.participants, 2)      # Apply protocols to the circuit at timstep 2

    protocol.ApplyCommunication(init.qc, init.backend, init.arg, "qasm-swap.txt") # Swap the qubits of 2 participants

    protocol.ApplySingleProtocol(init.backend, init.qc, alice, 1)      # Apply protocol 1 of alice to the circuit



    output.SaveCircuitPNG(init.qc, 'my_circuit')                   # save the global circuit as a png
    output.SaveToQasm(init.qc, "qasmCircuit.txt")                  # save the global circuit as qasm file

if __name__ == "__main__":
    main()
