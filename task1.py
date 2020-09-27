#!/usr/bin/env python


"""
task 1 - Quantum Computing Mentorship
"""

__author__ = 'georg'
__copyright__ = "Copyright 2020, Georg Schusteritsch"
__version__ = "0.1.0"
__maintainer__ = "Georg Schusteritsch"
__email__ = "georg.schusteritsch@gmail.com"
__date__ = "Sept 24, 2020"

from qiskit import *
from qiskit.quantum_info import random_statevector
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

#define a function to calculate the norm (to be minimized)
def norm(theta, phi, l):
    theta=theta.reshape(l*2, 4)
    Psi = getStateVector(theta, l) 
    return np.sum(np.abs((phi-Psi).data)**2)

def getStateVector(theta, l):
    circ = setupCircuit(theta, l)
    simulator = Aer.get_backend('statevector_simulator')
    result = execute(circ, backend=simulator).result()
    return result.get_statevector()

def setupCircuit(theta, L):
    qr = QuantumRegister(4)
    cr = ClassicalRegister(4)
    circ = QuantumCircuit(qr,cr)
    for j in range(0, L):
        even = QuantumCircuit(qr, cr)
        odd = QuantumCircuit(qr, cr)
        #define even blocks
        for i in range(0,4):
            even.rz(theta[2*j,i], i)
        even.cz(0,1)
        even.cz(0,2)
        even.cz(0,3)
        even.cz(1,2)
        even.cz(1,3)
        even.cz(2,3)
        #define odd blocks
        for i in range(0,4):
            odd.rx(theta[(2*j+1),i], i)
        circ = circ+odd+even
    return circ

def main():

	L=[i for i in range(1,11)]
	print('Considering {} layers'.format(L))

	#need a vector of random numbers that is normalized to 1, 
	#easiest way to just take function from qiskit
	vec = random_statevector(16)
	epsilon=[]
	for l in L:
	    #define random phi
	    #scipy minimize wants a vector not array
	    theta = np.random.rand(l*2*4)*np.pi*2
	    res = minimize(norm, theta, args=(vec, l), method='BFGS',options={'disp':True,'maxiter':1000})
	    epsilon.append(norm(res.x, vec, l))

	print(epsilon)

	plt.plot(L, epsilon, 'd-')
	plt.xlabel('layers L', fontsize=14)
	plt.ylabel('epsilon', fontsize=14)
	plt.xticks(fontsize=12)
	plt.yticks(fontsize=12)
	plt.ylim([0,0.75])
	plt.savefig('epsilon.eps')





if __name__ == '__main__':
  main()