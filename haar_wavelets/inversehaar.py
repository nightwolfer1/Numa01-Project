#!/usr/bin/env python3

"""
Denna filen innehåller det som rör Inverse Haar Transformation

Ansvarig: Daniel Levin
"""

import numpy as np

def concatenate_matrices(m1,m2,m3,m4):
    """
    The method concatenate_matrices takes in 4 sub matrices m1, m2, m3, m4
    and creates a bigger matrix B where each sub matrix positioned according 
    to the following:
    m1 is placed in the upper left corner
    m2 is placed in the upper right corner
    m3 is placed in the lower left corner
    m4 is placed in the lower right corner
    """

    E = np.concatenate((m1,m2), axis=1)
    F = np.concatenate((m3,m4), axis=1)
    B = np.concatenate((E,F))
    return B

def inverse_haar_transformation(B,WM,WN, n):
    """
    The method inverse_haar_transformation takes in a matrix B with dimensions MxN and two haar wavelet matrices 
    WN and WM with dimensions N and M respectively. 

    The method return B multiplied with the inverse of WM from the left and WN from 
    the right  

    alternativt
    Input parameters:
    Matrix B with dimensions MxN
    Matrix WM with dimensions MxM
    Matrix WN with dimensions NxN

    The method returns 
    inv(WM)*B*WN
    """

    # Jag tog mig friheten att lägga till denna loopen // Emil
    result = []
    result = np.dot(np.dot(np.linalg.inv(WM),B), WN)
    for i in range(n - 1):
        result = np.dot(np.dot(np.linalg.inv(WM),result), WN)
    return result