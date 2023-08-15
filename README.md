# IQ-stageE2023

## About The Project

This repo is an intership(E2023) project in research in the field of quantum information with Dave Touchette as Superviser.
This repo contains jupyter notebooks and scripts that are implementation of different algorithms. 

The goal of the project was to find a way to simulate communication of differents participants on a physical quantum processor. So each participants must 
create compile their protocols on specific qubits on the provided backend. Depending on the configuration of the backend, we
want to allow the user of the project to generate participants and map each participants to the specified qubits. We must then 
avoid transpiling a global circuit.

The strategy here is to create each participants a quantum circuit and transpile it before adding it to a global circuit. The
Addition is done according to a default layout or a layout given by the user.

As mentionned above, there is also jupyter notebook with some distributed algorithms.

## Getting Started

### Disclaimer

All of this project as been done on linux. It is tested on windows but, there might still be some errors. Not tested on MAC.

This project can have qasm files as input, but it is not required. You can still only write qiskit code and it will compile as expected from a qiskit project.

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

_NB. If the activation of the default venv does not work, install virtualenv, create a new venv and activate it._
```
pip install virtualenv
virtualenv venv_name
source venv_name/bin/activate

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
conda create -n venv_name
```
5. Activate venv:
```
conda activate venv_name
```
6. Install pip requirements
```
pip install -r requirements.txt
```

Both OS:

** **IMPORTANT** **
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

This project has 5 main directories when running protocols:

- Images: This is the directory where all the saved PNG images will be stored. Saved PNG includes pictures of final circuit, participants circuit, job results, etc.
- JsonFiles: This is the directory where all the json input files are. This is where the main scripts will fetch the file to create the participants.
- Qasm_output: This is the directory where all the saved qasm files will be stored. When you create a circuit and save in qasm format it will be there.
- QasmFiles: This is the directory where all the qasm input files are stored. When you create a qasm file as a protocol to feed the scripts, you must put them there.This directory contains other directories:
    - QasmFiles/<_projectName_>/participants -> Contains folders of the name of every participants which contains every qasm protocols files of the participants.
    - QasmFiles/<_projectName_>/Global -> Contains all the qasm protocol file that affects more than one participants and must be applied in the global circuit.
- PythonScripts: Contains all the python scripts of the projects. The main scripts are in this directory, but the utility functions are in seperate folders.
This directory contains other directories:
    - PythonScripts/General_modules -> Contains all the general utility functions used in all the projects.
    - PythonScripts/<_projectName_>_modules -> Automatically created when a new project is generated. It is for the user, if he wants to create new utility functions specific to the project. Some Specific modules have already been created for the example project.

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

- JsonFiles/<_projectName_>_input.JSON:
    This file is the input that the main script will use to create participants and create the global circuit. All informations about this file is in the header of the file.

- PythonScripts/<_projectName_>.py
    This file is the main script that the user must change to add protocols, save circuits, clear folders, etc. All informations about this file is in the header of the file. Looking at other main scripts for ideas and protocols is recommended.

- QasmFiles/<_projectName_> 
    This directory is where the input qasm files are. It needs 2 directories. One named "Participants",  containing a number of folders equal to the number of participants you have in the project. **Each one of these will have the name of a participant**. This is important because **the qasm files of each participants will be fetched there**, so you need to put your qasm files in the corresponding folder. The second folder is named "Global". This is where you will put the qasm files that interact with more than one participants that you have to add to the global circuit directly.

 ** **IMPORTANT** **
If you add participants in the json input file, you **must** add a folder of the name of your new participant in the directory: 
QasmFiles\<_projectName_>\Participants\< new folder with participant name >
## Contact

Christopher Sicotte - Sicc2201@usherbrooke.ca

## References

<a id="1">[1]</a> 
Andrew W. Cross, Lev S. Bishop, John A. Smolin, Jay M. Gambetta. Open Quantum Assembly Language. https://arxiv.org/pdf/1707.03429.pdf, 2017. accessed July 2023.

<a id="2">[2]</a> 
Mark Braverman, Ankit Garg, Young Kun Ko, Jieming Mao. Near-optimal bounds on bounded-round quantum communication complexity of disjointness. https://arxiv.org/pdf/1505.03110.pdf, 2018. accessed July 2023.

<a id="3">[3]</a> 
Ronald de Wolf, Quantum Computing: Lecture Notes. https://arxiv.org/pdf/1907.09415.pdf, 2011. accessed May 2023.
