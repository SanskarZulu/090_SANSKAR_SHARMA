#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Assignment 2: Unification algorithm implementation in solving linear equations using matrix
#submitted by: Sanskar sharma
#PRN: 0120180381
#Roll no: 090


import numpy as np

def solution_equations(A,B,X):
    """
    Solve a linear matrix equation, or system of linear scalar equations.
    """
    
    solution = np.linalg.inv(A).dot(B)
    return solution


def unify(X,values):
    req_substitutions={}
    for i in range(len(X)):
        req_substitutions[X[i]]=values[i]
    return req_substitutions

def main():
    """
    The main driving function of the program, this takes the input equations from user
    and also call the further required functions for the program execution 
    """ 
    
    n=int(input("Enter the number of variables in the equaation: ")) 
    #n variable equations
    X=[]
    
    for i in range(n):
        x = input("Enter the name of variable: ")
        X.append(x)
        
    A=np.zeros((n,n))
    #initialising the coeficient matrix of n equations to solve n variable equations 
    
    print("Enter coeficient with proper sign and order as ",X)
    B=[]
    
    for i in range(n):
        A[i] = list(map(int, input("Enter the LHS coefficients of equation with spaces: ").split()))
        #inputing one equation in one line on LHS side
        
        b = float(input("Enter the constant on RHS of equation: "))
        #constant of that equation on RHS side
        B.append(b)
        
    X=np.array(X)
    B=np.array(B)
    #converting lists into np array
    
    values=solution_equations(A,B,X)
    #finding solutions of that equations
    
    print("Hence, the required substitution for unifying these equations simoultaneously: ", unify(X,values))
    
    return 


main()
#Main function

"""
Output:

Enter the number of variables in the equaation: 2
Enter the name of variable: a
Enter the name of variable: b
Enter coeficient with proper sign and order as  ['a', 'b']
Enter the LHS coefficients of equation with spaces: 1 1
Enter the constant on RHS of equation: 10
Enter the LHS coefficients of equation with spaces: 1 -1
Enter the constant on RHS of equation: 8
Hence, the required substitution for unifying these equations simoultaneously:  {'a': 9.0, 'b': 1.0}
"""

