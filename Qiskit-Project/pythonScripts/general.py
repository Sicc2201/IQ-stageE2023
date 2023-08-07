from general_modules import QasmFileManager as qasm
from general_modules import ProtocolManager as protocol
from general_modules import OutputManager as output
from general_modules import Initialize

import sys 
    
def main():

    # initialaize all the dependencies for the program and return an object with all the necessities
    init = Initialize.InitiateOperation(sys.argv[0])

    commFiles = qasm.GetCommunicationQasmFiles("QasmFiles/" + init.arg + "/communication") # get communication files folder
    for p in init.participants:
      print(p)

    protocol.ApplyProtocol(init.backend, init.qc, init.participants, 1)      # Apply protocol to the circuit at timstep 1

    protocol.ApplyCommunication(init.qc, init.backend, init.arg, "qasm-swap.txt") # Swap the qubits of 2 participants

    protocol.ApplyProtocol(init.backend, init.qc, init.participants, 2)      # Apply protocol to the circuit at timstep 2

    output.SaveCircuitPNG(init.qc, 'my_circuit')                   # save the global circuit as a png
    output.SaveToQasm(init.qc, "qasmCircuit.txt")                  # save the global circuit as qasm file

if __name__ == "__main__":
    main()
