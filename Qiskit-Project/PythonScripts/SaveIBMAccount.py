#########################################################################
"""
Title: general.py
Author: Christopher Sicotte
Date of creation: 31/07/23
Last edited: 10/08/23

"""
#########################################################################
""""
General example of the program with 3 participants.

Contexte:

The goal is to have 2 participants that has random protocol and layout has an example.

Algorithm:

let the 2 participant (Alice, Bob). They have protocols at different time steps and layout to them.
The circuit begin in the |s> state.
The program will Initialize all the necessary, then we will apply all the protocols for the participants and swaps qubits


"""
########################################################################

from qiskit import IBMQ
import argparse
    
def main():
    parser = argparse.ArgumentParser(add_help=True, description=" This script saves your IBM quantum account for this project. You can get it there: https://quantum-computing.ibm.com/")
    parser.add_argument('MY_API_TOKEN', type=str, help="IBM quantum API_TOKEN")
    args = parser.parse_args()
    if len(vars(args)) < 1:
        print("Put your MY_API_TOKEN as argument")
        parser.print_usage()

    IBMQ.save_account(args.API_TOKEN)

if __name__ == "__main__":
    main()
