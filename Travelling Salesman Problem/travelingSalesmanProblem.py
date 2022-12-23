import numpy as np
def NN(A, start):
	path = [start]
	cost = 0
	N = A.shape[0]
	visited = np.ones(N,dtype = bool)
	visited[start] = False
	
	for i in range(N-1):
		last = path[-1]
		nextDist = np.argmin(A[last][visited])
		nextNode = np.arange(N)[visited][nextDist]
		path.append(nextNode)
		visited[nextNode] = False
		cost += A[last, nextNode]
	return path, cost
	     
A = np.array([
	[0, 2, 1, 3],
	[2, 0, 3, 4],
	[1, 3, 0, 3],
	[3, 4, 2, 0]])

print(NN(A,0))

	

