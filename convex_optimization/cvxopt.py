import numpy as np
from cvxopt import matrix, solvers
'''
variable initialization
'''
edge_nodes = 3
files = 1
# file size matrix(Assume 100MB)
file_size = np.array([50.0])
file_size= file_size.reshape(1,files)
# Length Matrix(km)
coverage_length = np.array([1,2,5])
coverage_length = coverage_length.reshape(edge_nodes,1)
# jam density matrix(vehicles per km)
jam_density = np.array([100,100,18])
jam_density = jam_density.reshape(edge_nodes,1)
# bandwidth between edge node and vehicles
band_e_v = np.array([100,200,50])
band_e_v = band_e_v.reshape(edge_nodes,1)
# bandwidth between edge nodes
band_e_e = np.array([25,50,40])
band_e_e = band_e_e.reshape(edge_nodes,1)
# preparation of coefficients
c_list = list()
for e in range(0,edge_nodes):
    c_val = band_e_v[e][0]/(jam_density[e][0]*coverage_length[e][0])
    c_list.append(c_val)

'''
Preparation of matrices
'''
P = np.zeros(shape=(edge_nodes,edge_nodes))
for i in range(0,edge_nodes):
    for j in range(0,edge_nodes):
        if i == j:
            # diagonal element
            P[i][j] = (1/c_list[i])+(1/50)
        
        else:
            P[i][j] = ((1/c_list[i])+(1/c_list[j]))/2
        

P = 2*P
print("matrix p is:",P)
q = np.zeros(shape=(edge_nodes,1))
# Preparing Constraint Matrices
G = np.identity(edge_nodes)
for i in range(0,edge_nodes):
    for j in range(0,edge_nodes):
        if i == j:
            G[i][j] = -1
h = np.zeros(shape=(edge_nodes,1))
for i in range(0,edge_nodes):
    h[i][0] = 0.0000000000000001
A = np.ones(shape=(1,edge_nodes))
b = file_size
