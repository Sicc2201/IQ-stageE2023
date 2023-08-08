from General_modules import QasmFileManager as qasm
from General_modules import ProtocolManager as protocol
from General_modules import OutputManager as output
from General_modules import Initialize
from General_modules import ClearManager as cl
from General_modules import RunJob as rj

from Grover_modules import Utility as util
from Grover_modules import OracleUtility as OUtil

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

    # initialize all the dependencies for the program and return an object with all the necessities
    init = Initialize.InitiateOperation(sys.argv[0])

    alice = init.participants[0]
    bob = init.participants[1]

    OUtil.ApplyOracleAlice(init.backend, init.qc, alice)

    # protocol.ApplyCommunication(init.qc, init.backend, init.arg, "qasm-swap.txt") # Swap the qubits of 2 participants


    output.SaveCircuitPNG(init.qc, 'my_circuit')                   # save the global circuit as a png
    output.SaveToQasm(init.qc, "qasmCircuit.txt")                  # save the global circuit as qasm file

if __name__ == "__main__":
    main()
