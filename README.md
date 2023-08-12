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
Addition is done according to a default layout or a layout given by the user

As mentionned above, there is also jupyter notebook with some distributed algorithms

## Getting Started

Disclaimer: All of this project as been done on linux.

### Prequisite

- python 3.8 or higher

### Installation

1. You need to open a terminal in the Qiskit-Project directory
2. activate the virtual environnement

```
pip install -r requirement.txt
```

## Usage

1. You need to open a terminal in the Qiskit-Project directory
2. activate the virtual environnement

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
