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

### Disclaimer

All of this project as been done on linux. It is tested on windows but, there might still be some errors. Not tested on MAC.

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
pip install -r requirements.txt
```

Windows:

1. Clone or download this git repository 
2. Open a Anaconda Prompt
3. Move in the Qiskit-Project directory
```
cd <full PATH to Qiskit-Project directory>
```
4. Create a new virtual environnement:
```
conda create -n <Name of venv>
```
5. Activate venv:
```
conda activate <Name of venv>
```
6. Install pip requirements
```
pip install -r requirements.txt
```

Both OS:

IMPORTANT!!
If it is the first time you use the IBM quantum processors, you need to create your IBM quantum account there: https://quantum-computing.ibm.com/ and then add your API_TOKEN:
- Run the script "SaveIBMAccount.py" with your API TOKEN as argument:
```
python PythonScripts\SaveIBMAccount.py MY_API_TOKEN
```
or
```
python3 PythonScripts/SaveIBMAccount.py MY_API_TOKEN
```

## Structure



## Usage

Note that Linux paths use "/" and windows paths use "\\". So when you need to run a command keep that in mind

### Run premade algorithms
1. Make sure your working directory is Qiskit-Project and your venv is activated (see installation)
2. Execute one of the python scripts in the "PythonScripts" directory. For example:
```
python PythonScripts\Grover.py
```
or
```
python3 PythonScripts/Grover.py
```
### Create new project
In this project, the user have the opportunity to create his own with a head start. The script "GenerateProject.py" allow the 
user to create his project and create all the dependencies and template to create participants and protocol of his own. 
At the execution of the script, the user can choose to add arguments to set some parameters for the project.
possibles arguments:
-h: print help message in terminal
-b backend: set the project backend
-q nqubits: set the participants number of qubits

Usage:
1. Make sure your working directory is Qiskit-Project and your venv is activated (see installation)
2. Execute the "GenerateProject" script with wanted arguments. For example:
```
python PythonScripts/GenerateProject.py -q 3 -b ibm_perth
```
(You might need to execute it with "python3" command instead of "python")

3. Open the project in the code editor of your choice. Here are some:

- vs code (the one used to create the initial project)
- visual studio
- pyCharm

4. What you need to modify to create your project:

- JsonFiles/< project name >_input.JSON:
    This file is the input that the main script will use to create participants and create the global circuit. All informations about this file is in the header of the file.

- PythonScripts/< project name >.py
    This file is the main script that the user must change to add protocols, save circuits, clear folders, etc. All informations about this file is in the header of the file. Looking at other main scripts for ideas and protocols is recommended.

- QasmFiles/< project name > 
    This directory is where the input qasm files are. 

## Contact

Christopher Sicotte - Sicc2201@usherbrooke.ca

## References

<a id="1">[1]</a> 
Andrew W. Cross, Lev S. Bishop, John A. Smolin, Jay M. Gambetta. Open Quantum Assembly Language. https://arxiv.org/pdf/1707.03429.pdf, 2017. accessed July 2023.

<a id="2">[2]</a> 
Mark Braverman, Ankit Garg, Young Kun Ko, Jieming Mao. Near-optimal bounds on bounded-round quantum communication complexity of disjointness. https://arxiv.org/pdf/1505.03110.pdf, 2018. accessed July 2023.

<a id="3">[3]</a> 
Ronald de Wolf, Quantum Computing: Lecture Notes. https://arxiv.org/pdf/1907.09415.pdf, 2011. accessed May 2023.
