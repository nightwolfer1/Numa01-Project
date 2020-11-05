'''
Importing Classes that might be needed 
'''

# Jag tog bort onödiga moduler // Emil
# import pandas as pd
import numpy as np 
# import matplotlib.pyplot as plt
import scipy.misc as sm
import datetime as dt


def create_haar_array(N):
    '''
    Method generates a transform matrix 

    Parameters
    ----------
    N : Integer, Float
        The Generated transform matrix is quadratic NXN, N is the dimension meaning how many pixels in each column and row of the picture.
        Has to be even number and size of at least 2.

    Returns
    -------
    Transform Matrix W_N 
    
    Type:  Numpy.array

    '''
    
    if N%2 != 0:
        raise ValueError('Transform matrix has to be assigned with even number')
    elif N < 2:
        raise ValueError('Smallest dimension for transform matrix is 2x2')
    
    

    
    #Initialize the matrix NXN dimensions
    Wn=np.zeros((N,N))
    '''
    The Transform matrix is multiplied by the matrix representing the greyscale image.
    The resulting array is going to be of the same dimension as the Transform matrix
    where each column is N/2 weighted averages followed by N/2 weighted differences.
    
    '''
    #Weighted Factor
    #The transform matrix has an interesting property, we can compute the inverse by doubling the transpose.
    # By doing variable substitution, Wn=sqrt(2)W~n we now have an orthogonal matrice where the inverse is equal to the transponat of the matrice. 
    Factor=np.sqrt(2)
    '''
    The first N/2 rows of the HWT produces a weighted average of the input list (column of matrice) taken two at a time. The weighted factor is sqrt(2)
    The last N/2 rows of the HWT produce a weighted difference of the input list (column of matrice) taken two at a time.
    The weighted factor is also sqrt(2). 
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

'''
Now we will make some simple tests to prove the function yields the transform matrix as expected,
We know from the assignment instruction how the transform matrix W8 I supposed to look. So we reproduce this matrix manually 
and do a boolean comparison, we will also do some minor tests, we cant make a transform matrix of size N < 2 and uneven numbers.
'''
def main():
    #Make the assignment matrix W8 to test if we get the same result
    
    Test_Matrix=np.sqrt(2)*np.array([np.array([1/2,1/2,0,0,0,0,0,0]),np.array([0,0,1/2,1/2,0,0,0,0]),np.array([0,0,0,0,1/2,1/2,0,0]),np.array([0,0,0,0,0,0,1/2,1/2]),np.array([-1/2,1/2,0,0,0,0,0,0]),np.array([0,0,-1/2,1/2,0,0,0,0]),np.array([0,0,0,0,-1/2,1/2,0,0]),np.array([0,0,0,0,0,0,-1/2,1/2])]) 
    
    
    #Test if we can assign N < 2
    try:
        create_haar_array(0)
        
    except ValueError as error: 
        print(error)
    
    #Test if we can assign uneven numers    
    try:
        create_haar_array(3)
        
    except ValueError as error:
        print(error)
    #Test if we get the expected Transform matrix W8
    assert Test_Matrix.all() == create_haar_array(8).all()
    print('Matrix yielded correct output, same transform matrix as assignment, no AssertionError')
    
        
if __name__ == "__main__":
    main()
    
