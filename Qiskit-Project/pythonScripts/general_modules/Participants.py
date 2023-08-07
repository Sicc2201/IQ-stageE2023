# importing Qiskit
from qiskit import QuantumCircuit, QuantumRegister

# constructor for the "Participant" class
class Participant:
    def __init__(self, pname, nqubits, qasmPath = "", q7_order = [], q16_order = [], q27_order = []):
        self.name = pname                                                  # name
        self.nqubits = nqubits                                             # number of qubits in its register
        self.layout = {"7q": q7_order, "16q": q16_order, "27q": q27_order} # dictionnary for its layouts
        self.cm = None                                                     # coupling map
        self.map = []                                                      # array that stock the layout for the job
        self.qr = QuantumRegister(nqubits, name = pname)                   # quantum register of the participant
        self.qc = QuantumCircuit(nqubits)                                  # quantum circuit of the articipant
        self.qubits = []                                                   # qubits indices in the global circuit
        self.qasmPath = qasmPath                                           # path to participant's qasm files folder
        self.qasm = []                                                     # array that contains the protocols and timstep
        
    # function that allows to print the participant (why not)    
    def __str__(self):                            
        return f"{self.name} ({self.nqubits}qubits)"   # print the name and the number of qubits of the participant 