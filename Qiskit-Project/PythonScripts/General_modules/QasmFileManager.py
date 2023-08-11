#########################################################################
"""
Title: QasmFileManager.py
Author: Christopher Sicotte
Date of creation: 31/07/23
Last edited: 10/08/23

"""
#########################################################################
""""
This file facilitate the management of qasm files

Functions:

- GetParticipantsQasmFiles(folderPath)

- SetParticipantsQasmFolder(participants, projectName)

- GetGlobalQasmFiles(folderPath)

"""
########################################################################

import os

# return an array containing all the qasm files of a participant
def GetParticipantQasmFiles(p):
  qasmfiles = []
  folderPath = p.qasmPath
  for folderName in os.listdir(folderPath):
    f = os.path.join(folderPath, folderName)
    qasmfiles.append(f)
    print(f)
  return qasmfiles

# set the folder of the qasm files 
def SetParticipantsQasmFolder(participants, projectName):
  folderPath = "QasmFiles/" + projectName + "/Participants/"
  for p in participants:
    p.qasmPath = folderPath + p.name

# return an array containing all the global qasm files of the project
def GetGlobalQasmFiles(folderPath):
  commFiles = []
  for fileName in os.listdir(folderPath):
    f = os.path.join(folderPath, fileName)
    commFiles.append(f)
  return commFiles
  