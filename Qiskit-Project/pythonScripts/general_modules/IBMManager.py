from qiskit.visualization import plot_gate_map
from qiskit import IBMQ

def GetProvider():
    provider = IBMQ.load_account()
    provider.backends()  # list of backends
    return provider

def ManageBackend(provider, backendInput):
    backend = provider.get_backend(backendInput)
    plot_gate_map(backend)  # plot the layout of the processor
    # print(backend.configuration().basis_gates) # uncomment to print the gates supported by the backend
    return backend