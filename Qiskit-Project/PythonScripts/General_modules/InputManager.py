from General_modules import Participants as part
import jstyleson as js
import os

def LoadInput(subarg):
  fileName = "JsonFiles/" + subarg + "_input.JSON"
  curr = os.getcwd()
  file = curr + "/" +  fileName
  print("loading from: ", file)
  with open(file, "r") as f:
    jsonFile = js.load(f)
  return jsonFile

def CreateParticipants(participantsInput):
  participants = []

  for p in participantsInput:
    r = part.Participant(p["name"], p["nqubits"])
    if p["layout"]["7q"]:
      r.layout["7q"] = p["layout"]["7q"]
    if p["layout"]["16q"]:
      r.layout["16q"] = p["layout"]["16q"]
    if p["layout"]["27q"]:
      r.layout["27q"] = p["layout"]["27q"]
    
    if p["protocol"]:
      r.qasm = p["protocol"]
    else:
      print("Warning: participant ", p["name"], " does not have protocols")

    participants.append(r)
  return participants