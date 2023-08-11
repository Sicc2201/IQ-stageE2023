#########################################################################
"""
Title: low_info_AND.py
Author: Christopher Sicotte
Date of creation: 31/07/23
Last edited: 10/08/23

"""
#########################################################################
""""
Implementation of a low information protocol of a AND with 3 participants.

Contexte:

The goal is to have 3 participants that carry a value of 1 or 0.
If and aonly if all participants carry a 1 will the final measurement be 1. Else, the measurement will be 0.

Algorithm:

let the 3 participant (Alice, Bob, Charlie) have a variable, x, y, z, respectively.
The circuit begin in the |s> state
If x = 1, Alice will apply a rotation gate of U(pi/8*r, 0, 0)
Alice and Bob then swaps qubits
If y = 0, Bob will reset the qubit to |0> state
If z = 0, Charlie will reset the qubit to |0> state

This protocol iterates 4 * r times
We then measure the qubit of Charlie to get the final measurement.
Run the job and save the results

"""
########################################################################

from General_modules import ProtocolManager as protocol
from General_modules import OutputManager as output
from General_modules import Initialize
from General_modules import CleanupManager as cl
from General_modules import RunJob as rj

from low_info_AND_modules import Utility as util

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

    nBits = 1
    # initialize all the dependencies for the program and return an object with all the necessities
    init = Initialize.InitiateOperation(sys.argv[0], nBits)

    # arbitrary value of r
    # the value of r is hardcoded because we cannot have variables in the qasm file and the angle of the rotation depends on r.
    # if we change this value, we must change the angle in the qasm file by hand angle = pi/(8 * r).
    r = 1

    # we iterate 4 *r times, so 4 * r -1 + last iteration without swap Alice and Charlie
    for iter in range(4 * r - 1):
        if x == 1:
            protocol.ApplyProtocol(init.backend, init.qc, init.participants, 1, showPrint=False)      # Apply protocol to the circuit at timstep 1
        protocol.ApplyGlobalProtocol(init.qc, init.backend, init.arg, "qasm-swap-ab.txt", showPrint=False) # Swap the qubits of Alice and Bob

        # Qiskit parser does not keep the reset gate in Qasm circuit while transpiling so we do the reset on qiskit directly
        if y == 0:
            init.qc.reset(1)
        protocol.ApplyGlobalProtocol(init.qc, init.backend, init.arg, "qasm-swap-bc.txt", showPrint=False) # Swap the qubits of Bob and Charlie

        # Qiskit parser does not keep the reset gate in Qasm circuit while transpiling so we do the reset on qiskit directly
        if z == 0:
            init.qc.reset(2)
        protocol.ApplyGlobalProtocol(init.qc, init.backend, init.arg, "qasm-swap-ac.txt", showPrint=False) # Swap the qubits of Alice and Charlie

    if x == 1:
        protocol.ApplyProtocol(init.backend, init.qc, init.participants, 1, showPrint=False)      # Apply protocol to the circuit at timstep 1
    protocol.ApplyGlobalProtocol(init.qc, init.backend, init.arg, "qasm-swap-ab.txt", showPrint=False) # Swap the qubits of Alice and Bob

    if y == 0:
        init.qc.reset(1)
    protocol.ApplyGlobalProtocol(init.qc, init.backend, init.arg, "qasm-swap-bc.txt", showPrint=False) # Swap the qubits of Bob and Charlie

    if z == 0:
        init.qc.reset(2)  


    # measure the qubit of Charlie
    init.qc.measure(2, 0)

    # run the job on the simulator and save
    job = rj.RunSimulator(init.qc)
    rj.SaveResults(job)

    # save the global circuit as a png
    output.SaveCircuitPNG(init.qc, 'my_circuit')
    # save the global circuit as qasm file     
    output.SaveToQasm3(init.qc, "qasmCircuit.txt")
    # show the result in terminal
    util.ShowResults(job)

if __name__ == "__main__":
    main()
