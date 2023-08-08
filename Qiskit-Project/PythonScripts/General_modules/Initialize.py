from General_modules import UtilityMapping as map
from General_modules import UtilityCommunication as comm
from General_modules import QasmFileManager as qasm
from General_modules import InputManager as inputManager
from General_modules import IBMManager as ibm
from General_modules import InitClass

from qiskit import transpile
import re

def InitiateOperation(sysArg):
    #######################################################################################################    

    #      Get the inputs and set the participants

    #######################################################################################################    

    arg = re.findall(r"/.*\.", sysArg)
    arg_str = arg[0]
    subarg =  arg_str[1 : -1]
    inputFile = inputManager.LoadInput(subarg)                                  # get the input file
    backendInput = inputFile["backend"]                                   # get the backend
    participantsInput = inputFile["participants"]                         # get the participants infos
    participants = inputManager.CreateParticipants(participantsInput)     # create the participants based on the input JSON file

    qasm.SetParticipantsQasmFolder(participants, subarg)                          # set the qasm dictionary to each participants

    provider = ibm.GetProvider()                                          # get the provider
    backend = ibm.ManageBackend(provider, backendInput)                   # get the backend

    #######################################################################################################    

    #      Create circuits

    #######################################################################################################

    qcirc = comm.CreateQuantumCircuit(backend, participants)             # create the global quantum circuit with the registers of the participants
    map.CreateLayout(provider, backendInput, qcirc, participants)        # create the layout dictionary for the participants
    map.CreateCouplingMaps(backend, participants)                        # create the backend coupling map for the transpiler
    transpiled_qc = transpile(qcirc, backend, optimization_level = 0)    # transpile the circuit at the beginning to attribute the logical qubits to the physical ones

    initObject = InitClass.Init(transpiled_qc, participants, backend, subarg)
    return initObject