#########################################################################
"""
Title: SaveIBMAccount.py
Author: Christopher Sicotte
Date of creation: 31/07/23
Last edited: 12/08/23

"""
#########################################################################
""""
Save your IBM account.

Contexte:

To access the IBM quantum processors, you need to save your account on the PC. This script will allow to do this. All you need is your API_TOKEN.

"""
########################################################################

from qiskit import IBMQ
import argparse
    
def main():
    parser = argparse.ArgumentParser(add_help=True, description=" This script saves your IBM quantum account for this project. You can get it here: https://quantum-computing.ibm.com/")
    parser.add_argument('MY_API_TOKEN', type=str, help="IBM quantum API_TOKEN")
    args = parser.parse_args()
    if len(vars(args)) < 1:
        print("Put your MY_API_TOKEN as argument")
        parser.print_usage()

    IBMQ.save_account(args.MY_API_TOKEN)



if __name__ == "__main__":
    main()
