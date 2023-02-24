from qiskit import QuantumCircuit, transpile
import random
import numpy as np

# Define a constant for pi
pi = np.pi


def random_circuit(num_qubits, depth, basis_gates):
    """
    Generates a random quantum circuit using only single-qubit U gates and controlled-U (CU) gates.

    Args:
        num_qubits (int): The number of qubits in the circuit.
        depth (int): The depth of the circuit, i.e., the number of layers of gates.
        basis_gates (list): A list of basis gates to use in the circuit, in this case U and CU.

    Returns:
        QuantumCircuit: A randomly generated quantum circuit with the given number of qubits and depth.
    """
    # Create a new QuantumCircuit object with the specified number of qubits
    circuit = QuantumCircuit(num_qubits)

    # Add gates to the circuit until it reaches the specified depth
    while circuit.depth() < depth:
        # Choose two random qubits for the CU gate
        q = random.randint(0, num_qubits - 1)
        q2 = random.randint(0, num_qubits - 1)
        
        # Add the CU gate to the circuit if the qubits are different and the depth is less than the specified depth
        if q2 != q and circuit.depth() < depth:
            circuit.cu(
                random.uniform(0, 2 * pi),  # Angle for the theta parameter
                random.uniform(0, pi),  # Angle for the phi parameter
                random.uniform(0, 2 * pi),  # Angle for the lambda parameter
                random.uniform(0, 2 * pi),  # Angle for the gamma parameter
                q, q2
            )
            
            # Transpile the circuit into the specified basis gates
            circuit = transpile(circuit, basis_gates=basis_gates)

    # Remove any instructions beyond the specified depth
    for i in range(circuit.depth() - depth):
        circuit.data.pop()

    # Return the generated circuit
    return circuit
