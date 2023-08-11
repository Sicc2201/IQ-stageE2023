#########################################################################
"""
Title: ProtocolManager.py
Author: Christopher Sicotte
Date of creation: 31/07/23
Last edited: 10/08/23

"""
#########################################################################
""""
This file manage the protocols of the participants and the global circuit.

Contexte:

If we transpile the global circuit, the transpiler will mess with all the layout and the coupling map we want. So, we need
to create individual circuits externals from the global circuit. We then transpile them if necessary and add them to the
global circuit afterward.

Functions:

- AddProtocolToQc(backend, qc, p, t, isTranspiled=True, showPrint=True)

- ApplyProtocol(backend, qc, participants, timestep, isTranspiled=True, showPrint=True)

- ApplySingleProtocol(backend, qc, p, timestep, isTranspiled=True, showPrint=True)

- ApplyGlobalProtocol(qc, backend, project, fileName, layout = [], isTranspiled=True, showPrint=True)

"""
########################################################################

# importing
from qiskit import transpile
from General_modules import OutputManager as output
import qiskit_qasm2

# A function that transpile and add all operations done on the circuit of a given participant
def AddProtocolToQc(backend, qc, p, t, isTranspiled = True, showPrint=True):

    # output.SaveCircuitPNG(p.qc, p.name + "_" + t + '_qc', showPrint=showPrint) # uncomment to save participant's circuit as png

    # if bool true, transpile the circuit
    if isTranspiled:
        # if there is a coupling map, transpile with it
        if len(p.map) > 1:
            tr_circuit = transpile(p.qc, basis_gates = backend.configuration().basis_gates, coupling_map = p.cm, optimization_level=0)
        else:
            tr_circuit = transpile(p.qc, basis_gates = backend.configuration().basis_gates, optimization_level=0)
        output.SaveCircuitPNG(tr_circuit, p.name + "_" + t + '_qc_tr', showPrint=showPrint) # save transpiled circuit as png
    else:
        tr_circuit = p.qc

    qc.compose(tr_circuit, inplace = True, qubits = p.map) # add the participant's circuit to the global circuit
    qc.barrier() # apply a barrier
    
    p.qc.clear() # empty the participant's circuit

# apply the protocols of every participant at a given timestep
def ApplyProtocol(backend, qc, participants, timestep, isTranspiled = True, showPrint=True):
    t = str(timestep)
    # for every participants, add the protocol to the circuit
    for p in participants:
        if t in p.qasm:
            qasm_str = p.qasm[t]
            p.qc = qiskit_qasm2.load(p.qasmPath + "/" + qasm_str) # extract qasm file
            AddProtocolToQc(backend, qc, p, t, isTranspiled = isTranspiled, showPrint=showPrint) # add to glbal circuit

# apply protocols of a single participant at a given timestep
def ApplySingleProtocol(backend, qc, p, timestep, isTranspiled = True, showPrint=True):
    t = str(timestep)
    if t in p.qasm:
        qasm_str = p.qasm[t]
        p.qc = qiskit_qasm2.load(p.qasmPath + "/" + qasm_str) # extract qasm file
        AddProtocolToQc(backend, qc, p, t, isTranspiled = isTranspiled, showPrint=showPrint) # add to glbal circuit

# apply a global protocol directly to the global circuit
def ApplyGlobalProtocol(qc, backend, project, fileName, layout = [], isTranspiled = True, showPrint=True):
    # you may add a layout to your global protocol
    if not layout:
        layout = [i for i in range(qc.num_qubits)]
    comm_qc = qiskit_qasm2.load("QasmFiles/" + project + "/Global/" + fileName) # get and parse qasm circuit
    output.SaveCircuitPNG(comm_qc, fileName, showPrint=showPrint) # save the circuit

    # if bool true, the circuit is transpiled
    if isTranspiled:
        comm_tr = transpile(comm_qc, backend, initial_layout = layout)
        output.SaveCircuitPNG(comm_tr, fileName + "_tr", showPrint=showPrint)
    else:
        comm_tr = comm_qc
    
    qc.compose(comm_tr, inplace = True) # add the protocol to the global circuit
    qc.barrier()