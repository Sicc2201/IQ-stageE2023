#########################################################################
"""
Title: OutputManager.py
Author: Christopher Sicotte
Date of creation: 31/07/23
Last edited: 10/08/23

"""
#########################################################################
""""
This file manage and facilitate the output of the system

Functions:

- SaveToQasm2(qc, fileName, showPrint=True)

- SaveToQasm3(qc, fileName, showPrint=True)

- SaveCircuitPNG(qc, fileName, showPrint=True)

"""
########################################################################

#imports
from qiskit import qasm3

# saves the final circuit in a qasm file
def SaveToQasm2(qc, fileName, showPrint=True):
  filePath = "Qasm_output/"
  qasm = qc.qasm() # extract the global circuit and parse it into qasm 2.0 text

  # create a file and put the parsed text inside
  f = open(filePath + fileName, "w")
  f.write(qasm)
  # if bool true, print in terminal
  if showPrint:
    print("Circuit Saved as QASM file '", filePath + fileName, "'")
  f.close()

# saves the final circuit in a qasm file
def SaveToQasm3(qc, fileName, showPrint=True):
  filePath = "Qasm_output/"
  qasm = qasm3.dumps(qc) # extract the global circuit and parse it into qasm 3.0 text

  # create a file and put the parsed text inside
  f = open(filePath + fileName, "w")
  f.write(qasm)
  # if bool true, print in terminal
  if showPrint:
    print("Circuit Saved as QASM file '", filePath + fileName, "'")
  f.close()

def SaveCircuitPNG(qc, fileName, showPrint=True):
  # draw and save the circuit as PNG
  qc.draw(output='mpl', filename = "Images/" + fileName + ".png")
  # if bool true, print in terminal
  if showPrint:
    print("Circuit saved as PNG '", "Images/" + fileName + ".png'")
