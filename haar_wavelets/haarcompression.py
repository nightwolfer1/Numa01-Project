#!/usr/bin/env python3

"""
Denna filen innehåller det som rör Haar-compression

Ansvarig: CH
"""
import numpy as np
import haar_wavelets.transformarray as ht

def haar_compression(A,i):
    
    ''''
    Method compressing an intensity image of ndarray 
    by iterating transformarray i times

    Parameters
    ----------
    A : ndarray
        The image to be compressed. Quadratic NXM, N is the number of
        pixels in each row of the picture, M is the number of
        pixels in each column.
    
    i : Integer
        Number of iterations.

    Returns
    -------
    B : ndarray
        Compressed image
    
    Type:  Numpy.array

    '''

    #Creating transform matrix, TN for rows and TM for columns.
    TN = ht.create_haar_array(np.shape(A)[0])
    TM = ht.create_haar_array(np.shape(A)[1])
    B = A

    #Iteration
    for s in range(i):
        B = np.dot(np.dot(TN,B),TM.T)

    return B
        
        
        