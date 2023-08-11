#########################################################################
"""
Title: Grover.py
Author: Christopher Sicotte
Date of creation: 31/07/23
Last edited: 10/08/23

"""
#########################################################################
""""
We want to find the intersection in two calendar.

Contexte: 

Applying the Grover's search algorithm to find the intersection in two calendar. 
Each participants has a calendar. We will then apply the Distributed version on Grover's algorithm to find the position
in which we have an intersection.


Algorithme:

Wait for the input of the user to get the calendars
Initialize the global quantum circuit

Starting Grover's search algorithm
- initialize the qubit of the first participant in the |s> state
- apply the oracle of the first participant
- swap the qubits
- apply the oracle of the second participant
- swap the qubits
- apply the oracle of the first participant again to eliminate junk qubits
- apply diffuser

Iterate the Grover part about sqrt(N) times where N is the length of calendars
Run the job and save results

"""
########################################################################

from General_modules import ProtocolManager as protocol
from General_modules import OutputManager as output
from General_modules import Initialize
from General_modules import CleanupManager as cl
from General_modules import RunJob as rj

from Grover_modules import Utility as util
from Grover_modules import OracleUtility as oracle
from Grover_modules import GlobalUtility as gl

import sys 
    
def main():

    # clear the images folder before creating new ones
    cl.ClearImages()

    # waiting for the input of the user
    while(True):
        calendar_a = input("enter the calendar (length = 4) of Alice (only 0 or 1):\n")
        calendar_b = input("enter the calendar (length = 4) of Bob (only 0 or 1):\n")
        if util.CheckCalendars(calendar_a, calendar_b, 7):
            break
    
    nBits = 2 # number of classical bit in the global circuit

    # initialize all the dependencies for the program and return an object with all the necessities
    init = Initialize.InitiateOperation(sys.argv[0], nBits)

    alice = init.participants[0]
    bob = init.participants[1]

    nbSolutions = 1

    # iter = floor((ceil(sqrt(2**nPosQubits)) - 1)/nbSolutions) # if you know the number of solutions
    iter = 1 # If we don't know the number of solutions

    gl.Init_S_state(init.qc, init.backend, alice)

    for i in range(iter):

        oracle.ApplyOracle(init.backend, init.qc, alice, calendar_a, isTranspiled = False, showPrint=False) # apply alice oracle

        protocol.ApplyGlobalProtocol(init.qc, init.backend, init.arg, "Qasm-swap.txt", showPrint=False) # swap alice and bob qubits

        oracle.ApplyOracle(init.backend, init.qc, bob, calendar_b, isTranspiled = False, showPrint=False) # apply bob oracle
        
        protocol.ApplyGlobalProtocol(init.qc, init.backend, init.arg, "Qasm-swap.txt", showPrint=False) # swap alice and bob qubits

        oracle.ApplyOracle(init.backend, init.qc, alice, calendar_a, isTranspiled = False, showPrint=False) # apply alice oracle

        protocol.ApplyGlobalProtocol(init.qc, init.backend, init.arg, "Qasm-diffuser.txt", showPrint=False) # Apply the diffuser to the circuit

    # measure 2 firsts qubits in 2 classical bits
    init.qc.measure(alice.map[0:-1], [1, 0])

    # run the job on the simulator
    job = rj.RunSimulator(init.qc)

    # plot and saves the result
    rj.SaveResults(job)

    # save the global circuit as a png and a qasm file
    output.SaveCircuitPNG(init.qc, 'my_circuit', showPrint=False)                   
    output.SaveToQasm3(init.qc, "qasmCircuit.txt", showPrint=False)

    # show the result in the terminal
    util.ShowResults(job)

if __name__ == "__main__":
    main()
