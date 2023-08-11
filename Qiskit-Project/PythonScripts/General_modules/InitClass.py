#########################################################################
"""
Title: InitClass.py
Author: Christopher Sicotte
Date of creation: 31/07/23
Last edited: 10/08/23

"""
#########################################################################
""""
This is the constructor of the Init class

Contexte:

The goal of this class is to have a general object that can be easily accessible in any main file and get all the main info

Attributes:

- qc -> the global quantum circuit
- participants -> the list of all participants in the global circuit
- backend -> the backend used for the job
- arg -> the name of the project if needed

"""
########################################################################

# constructor for the "Init" class
class Init:
    def __init__(self, qc, participants, backend, arg):
        self.qc = qc 
        self.participants = participants
        self.backend = backend
        self.arg = arg
