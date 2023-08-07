# importing Qiskit
from qiskit import transpile
from general_modules import OutputManager as output
import qiskit_qasm2

# A function that transpile and add all operations done on the circuit of a given participant
def AddProtocolToQc(backend, qc, p, t):
    if len(p.map) > 1:
        tr_circuit = transpile(p.qc, basis_gates = backend.configuration().basis_gates, coupling_map = p.cm)
    else:
        tr_circuit = transpile(p.qc, basis_gates = backend.configuration().basis_gates)
    qc.compose(tr_circuit, inplace = True, qubits = p.map)
    qc.barrier()
    output.SaveCircuitPNG(p.qc, p.name + "_" + t + '_qc')
    p.qc.clear()

def ApplyProtocol(backend, qc, participants, timestep):
    t = str(timestep)
    for p in participants:
        if t in p.qasm:
            qasm_str = p.qasm[t]
            p.qc = qiskit_qasm2.load(p.qasmPath + "/" + qasm_str)
            AddProtocolToQc(backend, qc, p, t)

def ApplyCommunication(qc, backend, project, fileName, layout = []):
    if not layout:
        layout = [i for i in range(qc.num_qubits)]
    comm_qc = qiskit_qasm2.load("QasmFiles/" + project + "/communication/" + fileName)
    output.SaveCircuitPNG(comm_qc, 'swap', showPrint=False)
    comm_tr = transpile(comm_qc, backend, initial_layout = layout)
    output.SaveCircuitPNG(comm_tr, 'swap_tr', showPrint=False)
    qc.compose(comm_tr, inplace = True)