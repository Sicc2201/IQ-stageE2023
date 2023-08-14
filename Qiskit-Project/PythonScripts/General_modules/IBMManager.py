#########################################################################
"""
Title: IBMManager.py
Author: Christopher Sicotte
Date of creation: 31/07/23
Last edited: 10/08/23

"""
#########################################################################
""""
This file manage and facilitate the loading of IBM dependencies.
You might need to adjust some things to input your credentials.

Functions:

- GetProvider()

- ManageBackend(provider, backendName)

- CheckQubitsError(backend, sumQubits)

"""
########################################################################

from qiskit.visualization import plot_gate_map
from qiskit import IBMQ

# get your IBM credentials and return the provider
def GetProvider(IBM_Token = ""):
    # if this is the first time you use IBM services
    if IBM_Token != "":
        IBMQ.save_account(IBM_Token)
    provider = IBMQ.load_account() # load IBM account if you're already connected
    provider.backends()  # list of backends
    return provider

# get and return the backend object 
def ManageBackend(provider, backendInput):
    backend = provider.get_backend(backendInput) # get the backend
    plot_gate_map(backend)  # plot the layout of the processor
    # print(backend.configuration().basis_gates) # uncomment to print the gates supported by the backend
    return backend

# ensure that the number of qubits necessary does not exceed the number of qubits of the backend
def CheckQubitsError(backend, sumQubits):

    if backend.configuration().n_qubits >= sumQubits:
        print("Backend ok")
    else:
        print("backend qubits: ", backend.configuration().n_qubits, ", your total of qubits: ", sumQubits)
        raise Exception("your backend does not have enough qubits for your protocol")    
