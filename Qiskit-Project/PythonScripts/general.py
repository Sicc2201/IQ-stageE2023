#########################################################################
"""
Title: general.py
Author: Christopher Sicotte
Date of creation: 31/07/23
Last edited: 10/08/23

"""
#########################################################################
""""
General example of the program with 3 participants.

Contexte:

The goal is to have 2 participants that has random protocol and layout has an example.

Algorithm:

let the 2 participant (Alice, Bob). They have protocols at different time steps and layout to them.
The circuit begin in the |s> state.
The program will Initialize all the necessary, then we will apply all the protocols for the participants and swaps qubits


"""
########################################################################

from General_modules import QasmFileManager as qasm
from General_modules import ProtocolManager as protocol
from General_modules import OutputManager as output
from General_modules import Initialize
from General_modules import CleanupManager as cl

import sys 
    
def main():

    # clear the images folder before creating new ones
    cl.ClearImages()

    nBits = 1
    # initialaize all the dependencies for the program and return an object with all the necessities
    init = Initialize.InitiateOperation(sys.argv[0], nBits)

    alice = init.participants[0]
    for p in init.participants:
      print(p)

    GlobalFiles = qasm.GetGlobalQasmFiles("QasmFiles/" + init.arg + "/Global") # get global files folder
    qasmFiles = qasm.GetParticipantQasmFiles(alice) # get the qasm files of a participant

    # print the files
    print("qasmfiles of "+ alice.name + ": ", qasmFiles)
    print("globalfiles: ", GlobalFiles)

    protocol.ApplyProtocol(init.backend, init.qc, init.participants, 1, isTranspiled=False, showPrint=False)      # Apply protocols to the circuit at timstep 1

    protocol.ApplyGlobalProtocol(init.qc, init.backend, init.arg, "qasm-swap.txt", ) # Swap the qubits of 2 participants

    protocol.ApplyProtocol(init.backend, init.qc, init.participants, 2)      # Apply protocols to the circuit at timstep 2

    protocol.ApplyGlobalProtocol(init.qc, init.backend, init.arg, "qasm-swap.txt") # Swap the qubits of 2 participants

    protocol.ApplySingleProtocol(init.backend, init.qc, alice, 1)      # Apply protocol 1 of alice to the circuit

    # save output
    output.SaveCircuitPNG(init.qc, 'my_circuit') # save the global circuit as a png
    output.SaveToQasm3(init.qc, "qasm3Circuit.txt") # save the global circuit as qasm file
    output.SaveToQasm2(init.qc, "qasm2Circuit.txt") # save the global circuit as qasm2.0 file

if __name__ == "__main__":
    main()
