#########################################################################
"""
Title: UtilityMapping.py
Author: Christopher Sicotte
Date of creation: 31/07/23
Last edited: 11/08/23

"""
#########################################################################
""""
This file manage the layout and coupling map when inserting individual circuit into the global circuit

Functions:

- CreateParticipantMap(participants, nqubits_str)

- CreateCouplingMaps(backend, participants)

- Create7qubitsLayout(participants)

- Create16qubitsLayout(participants)

- CreateLayout(provider, backendInput, qc, participants)

"""
########################################################################

# importing
from qiskit.transpiler import CouplingMap 

from General_modules import IBMManager as ibm

# Create an array (participant.map) that will be used as coupling map when transpiling
# inputs: array[Participant], nb qubits of the backend ("5q", "7q", "16q", etc)
def CreateParticipantMap(participants, nqubits_str):
    for p in participants:
        cm = []
        for i, j in zip(p.layout[nqubits_str], range(p.nqubits)):
            cm.extend([i])
        p.map = cm

# Create the coupling map of every participants based on the given layout 
def CreateCouplingMaps(backend, participants):
    cm = CouplingMap(backend.configuration().coupling_map)
    nMaps = 0 
    for p in participants:
            nMaps += len(p.map)

    if backend.configuration().n_qubits >= nMaps:           
        for p in participants:
            # print(p.name, "map: ", p.map) 
            p.cm = cm.reduce(p.map)
    else:
        raise Exception("The size of your coupling map is too large for your backend")

# create the layout for a processor of 7 qubits
def Create5qubitsLayout(participants):
    # participants cannot reserve more than 4 qubits each
    for p in participants:
        if p.nqubits > 3 and len(participants) < 2:
            raise Exception("One or more participants cannot have more than 4 qubits")
        
    defaultLayout = True # bool: True if none of the participants has a 7q layout input
    allFilled = True     # bool: false if all of the participants have a 7q layout
    
    for p in participants:
        if p.layout["5q"]:
            defaultLayout = False
            break
    if defaultLayout == False:
        for p in participants:
            print(p.name, " layout[5q]: ", p.layout["5q"])
            if not p.layout["5q"]:
                allFilled = False
                break
    
    # participants must both have a custom layout of none of them
    # if none of the participants has a custom layout, it will get the default one
    if defaultLayout:

#################### default layout for 5 qubits ############################

            # default layout for 2 participants
            if len(participants) == 2:
                if participants[0].nqubits >= participants[1].nqubits:
                    participants[0].layout["5q"] =  [1]
                else:
                    participants[1].layout["5q"] = [1]
                    
                participants[0].layout["5q"].extend([ 0, 2])
                participants[1].layout["5q"].extend([ 3, 4])
            # default layout for 3 participants
            if len(participants) == 3:
                       
                participants[0].layout["5q"].extend([3])
                participants[1].layout["5q"].extend([1])
                participants[2].layout["5q"].extend([4])
        
############################################################################# 

    # all or none participants can have custom layout, not only some of them
    elif not defaultLayout and not allFilled:
        raise Exception("you must specify the layout for all participants")

    # create the coupling map to use for every participants
    CreateParticipantMap(participants, "5q") 

# create the layout for a processor of 7 qubits
def Create7qubitsLayout(participants):
    # participants cannot reserve more than 4 qubits each
    for p in participants:
        if p.nqubits > 4 and len(participants) < 2:
            raise Exception("One or more participants cannot have more than 4 qubits")
        
    defaultLayout = True # bool: True if none of the participants has a 7q layout input
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

            # default layout for 2 participants
            if len(participants) == 2:
                if participants[0].nqubits >= participants[1].nqubits:
                    participants[0].layout["7q"] =  [3]
                else:
                    participants[1].layout["7q"] = [3]
                    
                participants[0].layout["7q"].extend([ 1, 0, 2])
                participants[1].layout["7q"].extend([ 5, 4, 6])
            # default layout for 3 participants
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
    
#################### default layout for 16 qubits ############################
    qubitOrder = []
    if defaultLayout:
        # default layout for 2 participants
        if len(participants) == 2:
            # 8 qubits each
            participants[0].layout["16q"].extend([ 1, 0, 4, 7, 6, 10, 12, 15])
            participants[1].layout["16q"].extend([ 2, 3, 5, 8, 9, 11, 14, 13])

        # default layout for 3 participants
        elif len(participants) == 3:
            # 5 qubits each
            participants[0].layout["16q"].extend([ 0, 1, 2, 3, 4])
            participants[1].layout["16q"].extend([ 6, 7, 10, 12, 15])
            participants[2].layout["16q"].extend([ 5, 8, 11, 14, 13])

                
        # default layout for 4 participants
        elif len(participants) == 4:
            # 4 qubits each
            participants[0].layout["16q"].extend([ 0, 1, 2, 3])
            participants[1].layout["16q"].extend([ 5, 8, 9, 11])
            participants[2].layout["16q"].extend([ 14, 13, 12, 15])
            participants[3].layout["16q"].extend([ 4, 7, 6, 10])

############################################################################# 

    # all or none participants can have custom layout, not only some of them
    elif not defaultLayout and not allFilled:
        raise Exception("you must specify the layout for all participants")

    # create the coupling map to use for every participants
    CreateParticipantMap(participants, "16q") 

# call the good layout function depending on the size of the backend
def CreateLayout(provider, backendInput, participants):
    backend = provider.get_backend(backendInput)
    sumQubits = 0
    for p in participants:
        sumQubits += p.nqubits

    ibm.CheckQubitsError(backend, sumQubits)     # raise exception if you need more qubits than the backend provides

    # if the backend has 7 qubit mapping create associated layout
    if provider.get_backend("ibmq_quito") or provider.get_backend("ibmq_belem") or provider.get_backend("ibmq_lima"): # ibmq_manila does not have the same mapping
        print("backend: ", backend, ", ", backend.configuration().n_qubits, "qubits")
        if len(participants) <= 3: # 5 qubits backend cannot have more than 3 participants
            Create5qubitsLayout(participants)
        else:
            raise Exception("Too much participants for this backend")

    # if the backend has 7 qubit mapping create associated layout
    if backend == provider.get_backend("ibmq_jakarta") or provider.get_backend("ibm_perth") or provider.get_backend("ibm_lagos") or provider.get_backend("ibm_nairobi"):
        print("backend: ", backend, ", ", backend.configuration().n_qubits, "qubits")
        if len(participants) <= 3: # 7 qubits backend cannot have more than 3 participants
            Create7qubitsLayout(participants)
        else:
            raise Exception("Too much participants for this backend")
        
    # if the backend has 16 qubit mapping create associated layout
    elif backend == provider.get_backend("ibmq_guadalupe"):
        print("backend: ", backend, ", ", backend.configuration().n_qubits, "qubits")
        if len(participants) <= 4: # 16 qubits backend cannot have more than 4 participants
            Create16qubitsLayout(participants)
        else:
            raise Exception("Too much participants for this backend")
        
    else:
        raise Exception("No layout for this backend") # if no real backend correspond to the backend provided
