#########################################################################
"""
Title: Initialize.py
Author: Christopher Sicotte
Date of creation: 31/07/23
Last edited: 10/08/23

"""
#########################################################################
""""
Initialization of the system

Contexte:

The goal is to automatize the creation of the global circuit and return the init object based on the input provided by the input json file

Algorithme:

Get the data from the input
Set the participants
Manage the IBM account credentials
Create the global quantum circuit
Create the layout from input
Create coupling maps from input
create Init object and set it
return the Init object

"""
########################################################################

#imports
from General_modules import UtilityMapping as map
from General_modules import UtilityGlobal as gl
from General_modules import QasmFileManager as qasm
from General_modules import InputManager as inputManager
from General_modules import IBMManager as ibm
from General_modules import InitClass

from qiskit import transpile
import platform
import re # import REGEX

def InitiateOperation(sysArg, nBits):
    #######################################################################################################    

    #      Get the inputs and set the participants

    #######################################################################################################    

    # use REGEX to isolate the name of the project depending on OS
    if platform.system() == "Windows":
        arg = re.findall(r"\\.*\.", sysArg)
    else:
        arg = re.findall(r"/.*\.", sysArg)

    arg_str = arg[0]
    subarg =  arg_str[1 : -1]   
    inputFile = inputManager.LoadInput(subarg)                        # get the input file
    backendInput = inputFile["backend"]                               # get the backend
    participantsInput = inputFile["participants"]                     # get the participants infos
    participants = inputManager.CreateParticipants(participantsInput) # create the participants based on the input JSON file                                                           # number of classical bits in the circuit

    qasm.SetParticipantsQasmFolder(participants, subarg)              # set the qasm dictionary to each participants

    provider = ibm.GetProvider()                                      # get the provider
    backend = ibm.ManageBackend(provider, backendInput)               # get the backend

    #######################################################################################################    

    #      Create circuits

    #######################################################################################################

    qcirc = gl.CreateQuantumCircuit(participants, nBits)                      # create the global quantum circuit with the registers of the participants
    map.CreateLayout(provider, backendInput, participants)                    # create the layout dictionary for the participants
    map.CreateCouplingMaps(backend, participants)                             # create the backend coupling map for the transpiler
    transpiled_qc = transpile(qcirc, backend, optimization_level = 0)         # transpile the circuit at the beginning to attribute the logical qubits to the physical ones

    initObject = InitClass.Init(transpiled_qc, participants, backend, subarg) # create the init object
    return initObject
