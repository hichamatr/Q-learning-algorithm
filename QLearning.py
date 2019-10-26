import numpy as np
import random

#nodes number
N=10

#initialize reward matrix
R = np.zeros((N*N,N*N))

#initialize Q-values
Q = np.zeros((N*N,N*N))

#chech if j is a next element of i
def is_next(i,j):
    if ( j == i+1 or j == i-1 or j == i+N or j==i-N ): 
        return True
    else:
        return False
    
#check if i and j are adjacents
def is_next(i,j):
    if ( j == i+1 or j == i-1 or j == i+N or j==i-N ): 
        return True
    else:
        return False

#fill reward matrix with appropriate values
for src in range(N*N):
    for dest in range(N*N):
        if is_next(src,dest):
            #print("next = (",src,"->",dest,")")
            if dest//N == 0 or dest//N == N-1 or dest%N == 0 or dest%N == N-1 :
                #print(src,"->",dest)
                R[src][dest] = -15
            if dest//N == N-2 and dest%N == N-2:
                #print(src,"->",dest)
                R[src][dest] = 100
                
#we should not forget this       
R[(N*N)-1-(N+1)][(N*N)-1-(N+1)] = 100

#select a random next element
def select_next(s):
    finish = 0

    while finish == 0:
        s2 = random.randint(0,N*N-1)
        if is_next(s,s2): #if it is next
            finish = 1

    return(s2)

def max_value(s):
    maxi = 0

    for i in range(N*N):
        if Q[s][i] >= maxi:
            maxi = Q[s][i]

    return(maxi)

##Q-learning
#run the algorithm 500 time
for i in range(500):

    #select a random node
    s = random.randint(0,N*N-1)
    s2 = -1

    while s2 != (N*N)-(N+1):
        #print(s)
        s2 = select_next(s)
        Q[s][s2] = R[s][s2] + 0.8*max_value(s2)
        s = s2
