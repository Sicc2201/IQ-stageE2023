
from qiskit import qasm3

def SaveToQasm(qc, fileName, showPrint=True):
  filePath = "Qasm_output"
  qasm = qasm3.dumps(qc)
  f = open(filePath + "/" + fileName, "w")
  f.write(qasm)
  if showPrint:
    print("Circuit Saved as QASM file '", filePath + "/" + fileName, "'")
  f.close()

def SaveCircuitPNG(qc, fileName, showPrint=True):
  qc.draw(output='mpl', filename = "images/" + fileName + ".png")
  if showPrint:
    print("Circuit saved as PNG '", "images/" + fileName + ".png'")
