# QOSF Mentorship Screening Task

This repo contains my solution to task 1 of the QOSF mentorship screening task. 

The task asks to set up a 4 qubit system, consisting of two sets of gates, U<sub>odd</sub> consisting of RZ and CZ gates, and U<sub>even</sub> consisting of RX gates). One set of odd and even gates constitutes one layer L. The final state vector given random angles &theta; of the parametrized gates and for a given number of layers L is compared with a random state vector |&phi;> by considering &epsilon; =  min(&theta;) || |&Psi;(&theta;)>-|&phi;> ||.

For ease of running the solution I have exported my jupyter notebook to a standalone python module (requires qiskit, numpy, scipy, matplotlib)

The solution of the task is implemented using qiskit to create the quantum circuit and the random state vector. The minimization procedure uses scipy's minimize function, employing standard BFGS to minimize the norm of the difference as a function of &theta;.

The python code can be found in: task1.py

The plot showing &epsilon; as a function of number of layers L is shown in: epsilon.eps

## Structure of code

The python code first initializes a random statevetor (based on qiskit), then loops over L (set 1 to 10 in steps of 1). For each L a random set of angles is first chosen, which are minimized using scipy's minimize function (this calls three functions within my code, norm(), which calculations the norm of the difference of the random state vector and the output of the quantum circtuit, getStateVector(), which calculates the state vector from the quantum circuit, and setupCircuit(), which initializes the quantum circuit for a given L). 

A plot of &epsilon; is generated at the end.

## Output

Typical output (not necessary for getting plot, just for debugging) is shown in output.dat, and the plot is shown in epsilon.eps.

We see that from roughly L=4, &epsilon; is negligibly small, i.e. the norm of the difference of the random state vector and the final state vector of the quantum circuit vanishes. 