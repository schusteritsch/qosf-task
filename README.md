# QOSF Mentorship Screening Task

This attemps to solve the task using qiskit to create the quantum circuit and the random state vector.

Code to solve task 1: **task1.py**
Plot showing epsilon as a function of number of layers L:**epsilon.eps**

The task asks to set up a 4 qubit system, consisting of sets of gates (U_odd: RZ and CZ gates, U_even RX gates), where one set of odd and even gates constitutes one layer L. This is compared with a random state vector |phi> by considering epsilon =  min(theta) || |Psi(theta)>-|phi> ||.

The minimization procedure uses scipy's minimize function (employing BFGS).

