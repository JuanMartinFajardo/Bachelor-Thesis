#simplices are tuples (sorted)
#N=list of simplices
N = [(1,),(2,),(3,),(4,),(1,2),(1,3),(2,3),(2,4),(3,4),(2,3,4)]

import numpy as np

def dimension(N):
	out = 0
	for s in N:
		if len(s)>out: out = len(s)
	return out-1

def sorter1(N):
	d = dimension(N)
	Simplices = {}
	for i in range(0,d+1):
		i_simplices = []
		for s in N:
			if len(s)==i+1: i_simplices.append(s)
		Simplices[i]=sorted(i_simplices)
	return Simplices

simplices=sorter1(N)
print(simplices)

def dk_matrix(k,N):
	M=np.zeros((len(simplices[k+1]),len(simplices[k])),dtype=int)
	for i in range(0,len(simplices[k])):
		for j in range(0,len(simplices[k+1])):
			if set(simplices[k][i]).issubset(set(simplices[k+1][j])):
				for p in range(0, len(simplices[k+1][j])):
					if simplices[k+1][j][p] not in simplices[k][i]:
						M[j,i] = (-1)**p
						break
			else: M[j,i]=0
	return M
		
M1= dk_matrix(1,N)
M2= dk_matrix(0,N)
