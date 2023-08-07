import os

def GetParticipantsQasmFiles(folderPath):
  for folderName in os.listdir(folderPath):
    f = os.path.join(folderPath, folderName)
    print(f)

def SetParticipantsQasmFolder(participants, subarg):
  folderPath = "QasmFiles/" + subarg + "/participants/"
  for p in participants:
    p.qasmPath = folderPath + p.name

def GetCommunicationQasmFiles(folderPath):
  commFiles = []
  for fileName in os.listdir(folderPath):
    f = os.path.join(folderPath, fileName)
    commFiles.append(f)
  return commFiles
  