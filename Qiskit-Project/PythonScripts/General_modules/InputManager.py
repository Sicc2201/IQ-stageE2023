#########################################################################
"""
Title: InputManager.py
Author: Christopher Sicotte
Date of creation: 31/07/23
Last edited: 10/08/23

"""
#########################################################################
""""
This file manages the inputs to the whole system

Functions:

- LoadInput(projectName)

- CreateParticipants(participantsInput)

"""
########################################################################

from General_modules import Participants as part
import jstyleson as js
import os

# load the json input file,  parse it and return the parsed file 
def LoadInput(projectName):
  # extract necessary info
  fileName = "JsonFiles/" + projectName + "_input.JSON"
  curr = os.getcwd()
  file = curr + "/" +  fileName
  print("loading from: ", file)
  # open and parse the file
  with open(file, "r") as f:
    jsonFile = js.load(f)
  return jsonFile

# create each participants based on the input file and return an array containing every participants
def CreateParticipants(participantsInput):
  participants = []

  # for every participants
  for p in participantsInput:
    r = part.Participant(p["name"], p["nqubits"]) # create a participant with name and nqubits
    # if it has a 7 qubit layout
    if p["layout"]["7q"]:
      r.layout["7q"] = p["layout"]["7q"]
    # if it has a 16 qubit layout
    if p["layout"]["16q"]:
      r.layout["16q"] = p["layout"]["16q"]
    # if it has a 27 qubit layout
    if p["layout"]["27q"]:
      r.layout["27q"] = p["layout"]["27q"]

    # if it has already protocols in the json file
    if p["protocol"]:
      r.qasm = p["protocol"]
    else:
      print("Warning: participant ", p["name"], " does not have protocols")

    participants.append(r)
  return participants