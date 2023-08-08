# importing Qiskit transpiler
from qiskit.transpiler import CouplingMap

#######################################################################################################    
    
#      Utility
    
#######################################################################################################   
    
# ensure that the number of qubits necessary does not exceed the number of qubits of the backend
def CheckQubitsError(backend, sumQubits):

    if backend.configuration().n_qubits >= sumQubits:
        print("Backend ok")
    else:
        print("backend qubits: ", backend.configuration().n_qubits, ", your total of qubits: ", sumQubits)
        raise Exception("your backend does not have enough qubits for your protocol")    

# Create an array (participant.map) that will be used as coupling map when transpiling
# inputs: array[Participant], nb qubits of the backend ("7q", "16q", etc)
def CreateParticipantMap(participants, nqubits_str):
    for p in participants:
        cm = []
        for i, j in zip(p.layout[nqubits_str], range(p.nqubits)):
            cm.extend([i])
        p.map = cm

# Create the coupling map of every participants based on the layout 
def CreateCouplingMaps(backend, participants):
    cm = CouplingMap(backend.configuration().coupling_map)
    if backend.configuration().n_qubits == 7:           
        for p in participants:
            print(p.name, "map: ", p.map) 
            p.cm = cm.reduce(p.map)
    elif backend.configuration().n_qubits == 16:  
        for p in participants:
            p.cm = cm.reduce(p.layout["16q"])
    else:
        raise Exception("No coupling map for this backend")

# create the layout for a processor of 7 qubits
def Create7qubitsLayout(participants):
    # participants cannot reserve more than 4 qubits each

    for p in participants:
        if p.nqubits > 4 and len(participants) < 2:
            raise Exception("One or more participants cannot have more than 4 qubits")
        
    defaultLayout = True # bool: True if none of the participants has a 7q layout
    allFilled = True     # bool: false if all of the participants have a 7q layout
    
    for p in participants:
        if p.layout["7q"]:
            defaultLayout = False
            break
    if defaultLayout == False:
        for p in participants:
            print(p.name, " layout[7q]: ", p.layout["7q"])
            if not p.layout["7q"]:
                allFilled = False
                break
    
    # participants must both have a custom layout of none of them
    # if none of the participants has a custom layout, it will get the default one
    if defaultLayout:

#################### default layout for 7 qubits ############################

            if len(participants) == 2:
                if participants[0].nqubits >= participants[1].nqubits:
                    participants[0].layout["7q"] =  [3]
                else:
                    participants[1].layout["7q"] = [3]
                    
                participants[0].layout["7q"].extend([ 1, 0, 2])
                participants[1].layout["7q"].extend([ 5, 4, 6])

            if len(participants) == 3:
                       
                participants[0].layout["7q"].extend([3])
                participants[1].layout["7q"].extend([1])
                participants[2].layout["7q"].extend([5])
        
############################################################################# 

    # all or none participants can have custom layout, not only some of them
    elif not defaultLayout and not allFilled:
        raise Exception("you must specify the layout for all participants")

    # create the coupling map to use for every participants
    CreateParticipantMap(participants, "7q") 

# create the layout for a processor of 16 qubits
def Create16qubitsLayout(participants):
    
    defaultLayout = True # bool: True if none of the participants has a 16q layout
    allFilled = True     # bool: false if all of the participants have a 16q layout
    
    for p in participants:
        if p.layout["16q"]:
            defaultLayout = False
            break
    if defaultLayout == False:
        for p in participants:
            if not p.layout["16q"]:
                allFilled = False
                break
            
    print("defaultLayout = ", defaultLayout)
    
    qubitOrder = []
    if defaultLayout:
        # default layout for 2 participants
        if len(participants) == 2:
            # 8 qubits each
            qubitOrder.append = [ 1, 0, 4, 7, 6, 10, 12, 15]
            qubitOrder.append = [ 2, 3, 5, 8, 9, 11, 14, 13]
            
            for p, q in zip(participants, qubitOrder):
                p.layout["16q"].extend(q)

        # default layout for 3 participants
        elif len(participants) == 3:
            # 5 qubits each
            qubitOrder.append = [ 0, 1, 2, 3, 4]
            qubitOrder.append = [ 6, 7, 10, 12, 15]
            qubitOrder.append = [ 5, 8, 11, 14, 13]
            
            for p, q in zip(participants, qubitOrder):
                p.layout["16q"].extend([q])

                
        # default layout for 4 participants
        elif len(participants) == 4:
            # 4 qubits each
            qubitOrder.append = [ 0, 1, 2, 3]
            qubitOrder.append = [ 5, 8, 9, 11]
            qubitOrder.append = [ 14, 13, 12, 15]
            qubitOrder.append = [ 4, 7, 6, 10]
            
            for p, q in zip(participants, qubitOrder):
                p.layout["16q"].extend([q])

    # all or none participants can have custom layout, not only some of them
    elif not defaultLayout and not allFilled:
        raise Exception("you must specify the layout for all participants")

    # create the coupling map to use for every participants
    CreateParticipantMap(participants, "16q") 

# call the good layout function depending on the size of the backend
def CreateLayout(provider, backendInput, qc, participants):
    backend = provider.get_backend(backendInput)
    sumQubits = 0
    for p in participants:
        sumQubits += p.nqubits

    CheckQubitsError(backend, sumQubits)     # raise exception if you need more qubits than the backend provides

    if backend == provider.get_backend("ibmq_jakarta") or provider.get_backend("ibm_perth") or provider.get_backend("ibm_lagos") or provider.get_backend("ibm_nairobi"):
        print("backend: ", backend, ", ", backend.configuration().n_qubits, "qubits")
        if len(participants) <= 3: # 7 qubits backend cannot have more than 3 participants
            Create7qubitsLayout(participants)
        else:
            raise Exception("Too much participants for this backend")
        
    elif backend == provider.get_backend("ibmq_guadalupe"):
        print("backend: ", backend, ", ", backend.configuration().n_qubits, "qubits")
        if len(participants) <= 4: # 16 qubits backend cannot have more than 4 participants
            Create16qubitsLayout(participants)
        else:
            raise Exception("Too much participants for this backend")
        
    else:
        raise Exception("No layout for this backend") # if no real backend correspond to the ackend provided
