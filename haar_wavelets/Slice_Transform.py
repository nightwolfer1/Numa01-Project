# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 16:52:16 2020

@author: nightwolfer
"""


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import scipy.misc as sm
import datetime as dt
import time



Kvinna=sm.imread('kvinna.jpg',True) # 

N,M=Kvinna.shape 
def create_haar_array(N):
    '''
    Method generates a transform matrix 

    Parameters
    ----------
    N : Integer,Float
        The Generated transform matrix is quadratic NXN, N is the dimension
        meaning how many pixels in each column of the picture.
        Has to be even number and size of atleast 2.

    Returns
    -------
    Transform Matrix Wn. 
    
    Type:  Numpy.array

    '''
    
    if N%2 != 0:
        raise ValueError('Transform matrix has to be assigned with even number')
    elif N < 2:
        raise ValueError('Smallest dimension for transform matrix is 2x2')
    
    

    
    #Initialize the matrix NXN dimensions
    Wn=np.zeros((N,N))
    '''
    The Transform matrix is multiplied by the matrix representing grey scale image.
    The resulting array is going to be of same dimension as Transform matrix
    where each column is N/2 weighted averages followed by N/2 weighted differences.
    
    '''
    #Weighted factor
    Factor=np.sqrt(2)
    '''
    The weighted average and difference is computed on two consectuive pixels, therefor
    in first row the two first columns in the row are used for tranforming weighted average
    then the next two consecutive columns in next row and so on untill we reach row N/2.
    Then we do the same but with the differences untill last indice.
    Dot products with transform matrix result in sums for average 1/2*sum of two pixels is average
    and 1/2*(pixel(n+1)-pixel(n) ) is difference. If the transform matrix is used
    with a matrix simply in resulting matrix each column will contain averages to N/2 and differences N/2 -> N. 
    '''
    #Assigning too transform matrix
    Lp=0#Low pass filter tick
    Hp=0#High pass filter tick
    for n in range(N):
        if n < N/2:
            Wn[n,Lp:(Lp+2)]=np.array([1/2,1/2])
            Lp=Lp+2 #this is because in next row the Lp filter values are two indices to the right
        else:
            Wn[n,Hp:(Hp+2)]=np.array([-1/2,1/2])
            Hp=Hp+2 #this is because in next row the Hp filter values are two indices to the right
        
    return Factor*Wn

#enkel transformering med matris multiplikation
t0=time.time()
Transformed_with_matrix=create_haar_array(N).dot(Kvinna)
t1=time.time()
Time_with_matrix=t1-t0


t2=time.time() 
#Transformering via slicing.
New_Kvinna_mean=(Kvinna[1:N+1:2,:]+Kvinna[0:N:2,:])/2
New_Kvinna_diff=(Kvinna[1:N+1:2,:]-Kvinna[0:N:2,:])/2
Transformed=np.concatenate((New_Kvinna_mean,New_Kvinna_diff),axis=0)
#with weighted factor
Transformed=np.sqrt(2)*Transformed
t3=time.time()     
Time_with_slicing=t3-t2
print('Execution time of simple compression with Matrix multiplication  '+str(Time_with_matrix)+ ' seconds' )
print('Execution time of simple compression with slicing '+str(Time_with_slicing)+ ' seconds' )

#Test om det blev samma matris
if np.allclose(Transformed,Transformed_with_matrix):#test if same shape, elements have close enough value rtol 1e-5 ,atol 1e-8
    print("same Matrix")
else:
    print("failed")
        
sm.imsave('matrix_T.jpg',Transformed)
sm.imsave('Slic_T.jpg',Transformed_with_matrix)