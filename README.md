# QC Mentorship Program

## Random Quantum Circuit Generator

This repository contains a Python function for generating random quantum circuits using only single-qubit U gates and controlled-U (CU) gates. The function is implemented in Qiskit and can be used to generate circuits of arbitrary size and depth.

## Installation

To use this function, you will need to have Qiskit installed on your system. You can install Qiskit using pip:

```sh
pip install qiskit
```
## Usage

To use the `random_circuit()` function to generate a random quantum circuit, import the function from the `random_circuit.py` file and call it with the desired number of qubits, depth, and basis gates:

```python
#Example
from random_circuit import random_circuit

num_qubits = 3
depth = 10

basis_gates = ['x', 'rx', 'rz', 'cx']
circuit = random_circuit(num_qubits, depth, basis_gates)
circuit.draw(output='mpl')

```

