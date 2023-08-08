from math import floor, ceil, log2

# measure i qubits for i classical bit 
def MesureQubits(qc, nqubits):
    for i in range(nqubits):
        qc.measure(i, i)

def CheckPower2(a):
    return ceil(log2(a)) != floor(log2(a))

# Ensure that two participants has their calendar of the same size        
def CheckCalendars(a, b, nqubits):

    if len(a) != len(b):
        raise Exception("the two calendar must be the same size")
    if not CheckPower2(a):
        raise Exception("the two calendar's length must be a power of 2")
    if not CheckPower2(b):
        raise Exception("the two calendar's length must be a power of 2")
    if (len(a) + len(b) + 2) > nqubits:
        raise Exception("Your calendars are to big for your backend")
    if len(a) != 4 or len(b) != 4:
        raise Exception("Calendars must be of length 4")
    print("calendars ok")
    return True


# swap all working qubits from the messenger to the receiver 
# messenger and receiver are the index of the participant
def SwapAll(qc, nqubits, messenger, receiver):
    for i in range(nqubits):
        qc.swap(i + nqubits * messenger, i + nqubits * receiver)

def InverseResults(results, threshold):
    best_results = []
    # result only consider elements over a certain threshold
    for r in results:
        if r[1] >= threshold:
            best_results.append(r[0])

    # inverse the binary result because qiskit have inversed result
    # Example: result = 001 = 1, true value = 100 = 4
    results = []
    for i in best_results:
        results.append(int(str(i)[::-1], 2))

    if not results:
        print("there are no solutions for these calendars")

    elif len(results) == 1:
        print("the solution is: ", results[0])
    else:
        print("there are", len(results),"solutions: ", results)