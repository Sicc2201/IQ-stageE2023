#########################################################################
"""
Title: OracleUtility.py
Author: Christopher Sicotte
Date of creation: 31/07/23
Last edited: 11/08/23

"""
#########################################################################
""""
General operations for the oracle of the participants based on the qasm files

"""
########################################################################

# imports
from General_modules import ProtocolManager as pm

# create the oracle for a participant depending on given calendar
def ApplyOracle(backend, qc, p, calendar, isTranspiled = True, showPrint=True):
    # for every positions in calendar add the right protocol
    for i in range(len(calendar)):
        # if the ith element in the calendar = 1, then add the protocol to the circuit
        if calendar[i] == "1":
            pm.ApplySingleProtocol(backend, qc, p, i, isTranspiled = isTranspiled, showPrint=showPrint) # add the right protocol to the global circuit