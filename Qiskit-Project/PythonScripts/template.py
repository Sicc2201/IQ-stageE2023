#########################################################################
""""
This is a template by default that the GenerateProject.py use to create a base program.

Contexte:

There is an example of everything so the user can start from there when crating a new project.

Algorithm:

...

"""
########################################################################


# DO NOT FORGET TO ADD THE MODULES YOU USE IN THE SCRIPT
from General_modules import QasmFileManager as qasm
from General_modules import ProtocolManager as protocol
from General_modules import OutputManager as output
from General_modules import Initialize
from General_modules import ClearManager as cl
from General_modules import RunJob as rj

import sys 
    
def main():

    # clear the images folder before creating new ones
    cl.ClearImages()

    # initialize all the dependencies for the program and return an object with all the necessities
    init = Initialize.InitiateOperation(sys.argv[0])

    # protocol.ApplyProtocol(init.backend, init.qc, init.participants, 1)      # Apply protocol to the circuit at timstep 1

    # protocol.ApplyCommunication(init.qc, init.backend, init.arg, "qasm-swap.txt") # Swap the qubits of 2 participants

    # protocol.ApplyProtocol(init.backend, init.qc, init.participants, 2)      # Apply protocol to the circuit at timstep 2

    # measure the qubit of Charlie
    # init.qc.measure(2, 0)

    # run the job on the simulator
    # rj.RunSimulator(init.qc)

    # run this instead to run the job on selected backend
    # rj.RunBackend(init.backend, init.qc)

    output.SaveCircuitPNG(init.qc, 'my_circuit')                   # save the global circuit as a png
    output.SaveToQasm(init.qc, "qasmCircuit.txt")                  # save the global circuit as qasm file

if __name__ == "__main__":
    main()
