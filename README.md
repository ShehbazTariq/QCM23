# QC Mentorship Program

This repository contains solutions for the QC Mentorship Program tasks.

## Task 1: Find the Largest Number

The goal of this task is to develop a quantum algorithm that can determine which of two integers is larger, given that the integers can be positive or negative. The solution will consider an appropriate number of qubits and explain why it is valid for all kinds of numbers.

## Task 2: Is Rectangle?

The goal of this task is to determine whether a rectangle exists given four positive integers A, B, C, and D. If there is a rectangle, the solution will return 1; otherwise, it will return 0.

## Task 3: QSVM

The goal of this task is to generate a Quantum Support Vector Machine (QSVM) using the iris dataset and propose a kernel from a parametric quantum circuit to classify the three classes (setosa, versicolor, virginica) using the one-vs-all format. The kernel only works as a binary classification. The solution will identify the proposal with the lowest number of qubits and depth to obtain higher accuracy. The solution can use the UU† format or using the Swap-Test.

## Task 4: Random Circuits

The goal of this task is to design a function that generates a random quantum circuit. The function should consider the number of qubits, the number of depths, and the base of gates to be used. The function can only use the quantum gates of 1 and 2 qubits.

---

### How to Use

To run any of the tasks, clone the repository and navigate to the respective task directory. Each directory contains the code for the respective task.

```sh
git clone https://github.com/<your-username>/qc-mentorship-program.git
cd QCM23/task-<task-number>
