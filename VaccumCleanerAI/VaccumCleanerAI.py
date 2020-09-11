#!/usr/bin/env python
# coding: utf-8

# In[3]:


#AI Lab Assignment1

#By: Sanskar Sharma 090
#PRN: 0120180381

import random
a=random.randint(0,1)#Randomly positioning Vaccum Cleaner 
Room=["A","B"]#a=0 -> A and a=1 -> B
Roomstate={Room[0]:random.randint(0,1),Room[1]:random.randint(0,1)} #1 is dirty,0 is clean
swap={0:1,1:0}#swap dict to switch rooms pointer
Operation=["None.","Suck.","Move Right.","Move Left."]


def AgentFunction(Operationindex):
    """The agent function is a mathematical function 
    that maps a sequence of perceptions into action."""
    
    print("\tOperation: "+Operation[Operationindex])

    
def AgentProgram(a,Room,Roomastate):
    """"an agent program is a real implementation of an 
    agent function. In other words, it implements an 
    agent function which maps percepts to actions."""
    
    if Roomstate[Room[a]]==1:
        print("Location: "+Room[a])
        print("Room "+Room[a]+" is dirty.")
        AgentFunction(Operationindex=1)
        if Roomstate[Room[swap[a]]]==1:
            print("Room "+Room[swap[a]]+" is dirty.")
            if a==0:
                AgentFunction(Operationindex=2)
                a=swap[a]
                print("Location: "+Room[a])
                AgentFunction(Operationindex=1)
            else:
                AgentFunction(Operationindex=3)
                a=swap[a]
                print("Location: "+Room[a])
                AgentFunction(Operationindex=1)
            
        else:
            print("Room "+Room[swap[a]]+" is clean.")
            AgentFunction(Operationindex=0)
    else:
        print("Location: "+Room[a])
        print("Room "+Room[a]+" is clean.")
        AgentFunction(Operationindex=0)
        if Roomstate[Room[swap[a]]]==1:
            print("Room "+Room[swap[a]]+" is dirty.")
            if a==0:
                AgentFunction(Operationindex=2)
                a=swap[a]
                print("Location: "+Room[a])
                AgentFunction(Operationindex=1)
            else:
                AgentFunction(Operationindex=3)
                a=swap[a]
                print("Location: "+Room[a])
                AgentFunction(Operationindex=1)
        else:
            print("Room "+Room[swap[a]]+" is clean.")
            AgentFunction(Operationindex=0)
            
    return a #returning the location for next iteration.


#Main function
    
#Number of times vaccum cleaner works
n=int(input("Enter the number of Cleaning iterations: "))
for i in range(n):
    print("\nIteration "+str(i+1))
    a=AgentProgram(a,Room,Roomstate)
    #Re-initialising states of rooms after an iteration.
    Roomstate[Room[0]]=random.randint(0,1)
    Roomstate[Room[1]]=random.randint(0,1)
    
"""
Output: n=15.

Enter the number of Cleaning iterations: 15

Iteration 1
Location: A
Room A is dirty.
	Operation: Suck.
Room B is clean.
	Operation: None.

Iteration 2
Location: A
Room A is clean.
	Operation: None.
Room B is clean.
	Operation: None.

Iteration 3
Location: A
Room A is clean.
	Operation: None.
Room B is dirty.
	Operation: Move Right.
Location: B
	Operation: Suck.

Iteration 4
Location: B
Room B is dirty.
	Operation: Suck.
Room A is clean.
	Operation: None.

Iteration 5
Location: B
Room B is dirty.
	Operation: Suck.
Room A is clean.
	Operation: None.

Iteration 6
Location: B
Room B is dirty.
	Operation: Suck.
Room A is clean.
	Operation: None.

Iteration 7
Location: B
Room B is dirty.
	Operation: Suck.
Room A is clean.
	Operation: None.

Iteration 8
Location: B
Room B is clean.
	Operation: None.
Room A is dirty.
	Operation: Move Left.
Location: A
	Operation: Suck.

Iteration 9
Location: A
Room A is clean.
	Operation: None.
Room B is dirty.
	Operation: Move Right.
Location: B
	Operation: Suck.

Iteration 10
Location: B
Room B is clean.
	Operation: None.
Room A is clean.
	Operation: None.

Iteration 11
Location: B
Room B is dirty.
	Operation: Suck.
Room A is clean.
	Operation: None.

Iteration 12
Location: B
Room B is dirty.
	Operation: Suck.
Room A is dirty.
	Operation: Move Left.
Location: A
	Operation: Suck.

Iteration 13
Location: A
Room A is clean.
	Operation: None.
Room B is clean.
	Operation: None.

Iteration 14
Location: A
Room A is dirty.
	Operation: Suck.
Room B is clean.
	Operation: None.

Iteration 15
Location: A
Room A is clean.
	Operation: None.
Room B is dirty.
	Operation: Move Right.
Location: B
	Operation: Suck.

"""

    

