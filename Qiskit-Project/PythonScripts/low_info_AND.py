#########################################################################
""""
Implementation of a low information protocol of a AND with 3 participants.

Contexte:

The goal is to have 3 participants that carry a value of 1 or 0.
If and aonly if all participants carry a 1 will the final measurement be 1. Else, the measurement will be 0.

Algorithme:

let the 3 participant (Alice, Bob, Charlie) have a variable, x, y, z, respectively.
The circuit begin in the |s> state
If x = 1, Alice will apply a rotation gate of U(pi/8*r, 0, 0)
Alice and Bob then swaps qubits
If y = 0, Bob will reset the qubit to |0> state
If z = 0, Charlie will reset the qubit to |0> state

This protocol iterates 4 * r times
We then measure the qubit of Charlie to get the final measurement.

"""
########################################################################

from General_modules import ProtocolManager as protocol
from General_modules import OutputManager as output
from General_modules import Initialize
from General_modules import ClearManager as cl
from General_modules import RunJob as rj

import sys 
    
def main():

    # clear the images folder before creating new ones
    cl.ClearImages()

    # waiting for the input of the user
    while(True):
        x = int(input("enter the value of x (0 or 1):\n"))
        if x == 0 or x == 1:
            break
    while(True):
        y = int(input("enter the value of y (0 or 1):\n"))
        if y == 0 or y == 1:
            break
    while(True):
        z = int(input("enter the value of z (0 or 1):\n"))
        if z == 0 or z == 1:
            break
    # initialize all the dependencies for the program and return an object with all the necessities
    init = Initialize.InitiateOperation(sys.argv[0])

    # arbitrary value of r
    # the value of r is hardcoded because we cannot have variables in the qasm file and the angle of the rotation depends on r.
    # if we change this value, we must change the angle in the qasm file by hand.
    r = 1

    # we iterate 4 *r times, so 4 * r -1 + last iteration without swap Alice and Charlie
    for iter in range(4 * r - 1):
        if x == 1:
            protocol.ApplyProtocol(init.backend, init.qc, init.participants, 1)      # Apply protocol to the circuit at timstep 1
        protocol.ApplyCommunication(init.qc, init.backend, init.arg, "qasm-swap-ab.txt") # Swap the qubits of Alice and Bob

        # This is what it would look like to apply the reset gate in qasm to the circuit at timstep 2 if the reset gate would work with the transpiler
        # if y == 0:
            # protocol.ApplyProtocol(init.backend, init.qc, init.participants, 2)      
        # Qiskit parser does not keep the reset gate in Qasm circuit while transpiling so we do the reset on qiskit directly
        if y == 0:
            init.qc.reset(1)
        protocol.ApplyCommunication(init.qc, init.backend, init.arg, "qasm-swap-bc.txt") # Swap the qubits of Bob and Charlie

        # This is what it would look like to apply the reset gate in qasm to the circuit at timstep 3 if the reset gate would work with the transpiler
        # if z == 0:
        #     protocol.ApplyProtocol(init.backend, init.qc, init.participants, 3)      # Apply protocol to the circuit at timstep 3
        # Qiskit parser does not keep the reset gate in Qasm circuit while transpiling so we do the reset on qiskit directly
        if z == 0:
            init.qc.reset(2)
        protocol.ApplyCommunication(init.qc, init.backend, init.arg, "qasm-swap-ac.txt") # Swap the qubits of Alice and Charlie

    if x == 1:
        protocol.ApplyProtocol(init.backend, init.qc, init.participants, 1)      # Apply protocol to the circuit at timstep 1
    protocol.ApplyCommunication(init.qc, init.backend, init.arg, "qasm-swap-ab.txt") # Swap the qubits of Alice and Bob

    if y == 0:
        init.qc.reset(1)
    protocol.ApplyCommunication(init.qc, init.backend, init.arg, "qasm-swap-bc.txt") # Swap the qubits of Bob and Charlie

    if z == 0:
        init.qc.reset(2)  


    # measure the qubit of Charlie
    init.qc.measure(2, 0)

    # run the job on the simulator
    rj.RunSimulator(init.qc)

    # run this instead to run the job on selected backend
    # rj.RunBackend(init.backend, init.qc)

    # save the global circuit as a png
    output.SaveCircuitPNG(init.qc, 'my_circuit')
    # save the global circuit as qasm file     
    output.SaveToQasm(init.qc, "qasmCircuit.txt")

if __name__ == "__main__":
    main()
