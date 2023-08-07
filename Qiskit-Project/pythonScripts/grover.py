from general_modules import UtilityMapping as map
from general_modules import UtilityCommunication as comm
from general_modules import QasmFileManager as qasm
from general_modules import ProtocolManager as protocol
from general_modules import InputManager as inputManager
from general_modules import IBMManager as ibm
from general_modules import OutputManager as output

from qiskit import transpile

def main():
#######################################################################################################    

#      Get the inputs and set the participants

#######################################################################################################    
 
  inputFile = inputManager.LoadInput()                                  # get the input file
  backendInput = inputFile["backend"]                                   # get the backend
  participantsInput = inputFile["participants"]                         # get the participants infos
  participants = inputManager.CreateParticipants(participantsInput)     # create the participants based on the input JSON file

  qasm.SetParticipantsQasmFolder(participants)                          # set the qasm dictionary to each participants

  commFiles = qasm.GetCommunicationQasmFiles("QasmFiles/communication") # get ccommunication files folder
  for p in participants:
    print(p)

  provider = ibm.GetProvider()                                          # get the provider
  backend = ibm.ManageBackend(provider, backendInput)                   # get the backend

#######################################################################################################    

#      Create circuits

#######################################################################################################

  qcirc = comm.CreateQuantumCircuit(backend, participants)             # create the global quantum circuit with the registers of the participants
  map.CreateLayout(provider, backendInput, qcirc, participants)        # create the layout dictionary for the participants
  map.CreateCouplingMaps(backend, participants)                        # create the backend coupling map for the transpiler
  transpiled_qc = transpile(qcirc, backend, optimization_level = 0)    # transpile the circuit at the beginning to attribute the logical qubits to the physical ones

  protocol.ApplyProtocol(backend, transpiled_qc, participants, 1)      # Apply protocol to the circuit at timstep 1
  
  protocol.ApplyCommunication(transpiled_qc, backend, "qasm-swap.txt") # Swap the qubits of 2 participants

  protocol.ApplyProtocol(backend, transpiled_qc, participants, 2)      # Apply protocol to the circuit at timstep 2

  output.SaveCircuitPNG(transpiled_qc, 'my_circuit')                   # save the global circuit as a png
  output.SaveToQasm(transpiled_qc, "qasmCircuit.txt")                  # save the global circuit as qasm file

if __name__ == "__main__":
    main()
