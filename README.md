# IQ-stageE2023

## About The Project

This repo is an intership(E2023) project  in research in the field of quantum information with Dave Touchette as Superviser.
This repo contains jupyter notebooks and scripts that are implementation of different algorithms. 

The goal of the project was 
to find a way to simulate communication of differents participants on a physical quantum processor. So each participants must 
create compile their protocols on specific qubits on the provided backend. Depending on the configuration of the backend, we
want to allow the user of the project to generate participants and map each participants to the specified qubits. We must then 
avoid transpiling a global circuit.

The strategy here is to create each participants a quantum circuit and transpile it before adding it to a global circuit. The
Addition is done according to a default layout or a layout given by the user.

As mentionned above, there is also jupyter notebook with some distributed algorithms.

## Getting Started

Disclaimer: All of this project as been done on linux.

### Prequisite

- python 3.8 or higher:
```
https://www.python.org/downloads/
```
- Anaconda:
```
https://www.anaconda.com/download
```  

### Installation
Linux:
1. Clone or download this git repository 
2. You need to open a terminal in the Qiskit-Project directory
3. activate the virtual environnement:
```
source .venv/bin/activate
```
4. Install pip requirements

```
pip install -r requirement.txt
```
Windows:
################################################################### TO DO################################
1. Clone or download this git repository 
2. You need to open a terminal in the Qiskit-Project directory
3. activate the virtual environnement:
```
source .venv/bin/activate
```
4. Install pip requirements

```
pip install -r requirement.txt
```
#############################################################################################################
## Usage

### Run premade algorithms
1. Make sure your working directory is Qiskit-Project and your venv is activated (see installation)
2. Execute one of the python scripts in the "PythonScript" directory. For example:
```
python3 PythonScripts/Gover.py
```
### Create new project
In this project, te user have the opportunity to create his own with a head start. The script "GenerateProject.py" allow the 
user to create his project and create all the dependencies and template to create participants and protocol of his own. 
At the execution of the script, the user can choose to add arguments to set some parameters for the project.
possibles arguments:
-h: print help message in terminal
-b backend: set the project backend
-q nqubits: set the participants number of qubits

Usage:
1. Make sure your working directory is Qiskit-Project and your venv is activated (see installation)
2. Execute the "GeneratePrject" script with wanted arguments. For example:
```
python3 PythonScripts/GenerateProject.py -q 3 -b ibmq_perth
```

## Contact

Christopher Sicotte - Sicc2201@usherbrooke.ca

## References
<a id="1">[1]</a> 
Dijkstra, E. W. (1968). 
Go to statement considered harmful. 
Communications of the ACM, 11(3), 147-148.

https://www.mathstat.dal.ca/~mamy/Papers/staq.pdf

https://arxiv.org/abs/1707.03429

https://arxiv.org/abs/1505.03110

https://arxiv.org/abs/1907.09415
