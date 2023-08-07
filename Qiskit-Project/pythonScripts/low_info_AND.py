from general_modules import ProtocolManager as protocol
from general_modules import OutputManager as output
from general_modules import Initialize
from general_modules import ClearManager as cl
from general_modules import RunJob as rj

import sys 
    
def main():

    cl.ClearImages()

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
    # initialaize all the dependencies for the program and return an object with all the necessities
    init = Initialize.InitiateOperation(sys.argv[0])

    r = 4

    for iter in range(r - 1):
        if x == 1:
            protocol.ApplyProtocol(init.backend, init.qc, init.participants, 1)      # Apply protocol to the circuit at timstep 1
        protocol.ApplyCommunication(init.qc, init.backend, init.arg, "qasm-swap-ab.txt") # Swap the qubits of Alice and Bob

        if y == 0:
            protocol.ApplyProtocol(init.backend, init.qc, init.participants, 2)      # Apply protocol to the circuit at timstep 2
        protocol.ApplyCommunication(init.qc, init.backend, init.arg, "qasm-swap-bc.txt") # Swap the qubits of Bob and Charlie

        if z == 0:
            protocol.ApplyProtocol(init.backend, init.qc, init.participants, 3)      # Apply protocol to the circuit at timstep 3
        protocol.ApplyCommunication(init.qc, init.backend, init.arg, "qasm-swap-ac.txt") # Swap the qubits of Alice and Charlie

    if x == 1:
        protocol.ApplyProtocol(init.backend, init.qc, init.participants, 1)      # Apply protocol to the circuit at timstep 1
    protocol.ApplyCommunication(init.qc, init.backend, init.arg, "qasm-swap-ab.txt") # Swap the qubits of Alice and Bob

    if y == 0:
        protocol.ApplyProtocol(init.backend, init.qc, init.participants, 2)      # Apply protocol to the circuit at timstep 2
    protocol.ApplyCommunication(init.qc, init.backend, init.arg, "qasm-swap-bc.txt") # Swap the qubits of Bob and Charlie

    if z == 0:
        protocol.ApplyProtocol(init.backend, init.qc, init.participants, 3)      # Apply protocol to the circuit at timstep 3   


    init.qc.measure(2, 0)
    rj.RunSimulator(init.qc)

    output.SaveCircuitPNG(init.qc, 'my_circuit')           # save the global circuit as a png
    output.SaveToQasm(init.qc, "qasmCircuit.txt")                  # save the global circuit as qasm file

if __name__ == "__main__":
    main()
