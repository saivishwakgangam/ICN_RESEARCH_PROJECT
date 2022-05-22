import numpy as np
# from cvxopt import matrix, solvers
import cvxpy as cp
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
A = np.ones(shape=(1,edge_nodes))
b = file_size
'''
Adding maximum cacheable size at each edge node constraint(MB)
'''
max_cache_size = np.array([20.0,30.0,50.0])
max_cache_size = max_cache_size.reshape(edge_nodes,1)
# add cache size to h
h = np.concatenate((h,max_cache_size))
# add necessary matrix to G
id = np.identity(edge_nodes)
G = np.concatenate((G,id))

'''
Performing Optimization
'''
X = cp.Variable(shape=(edge_nodes,files))
obj_function = cp.Minimize((1/2)*cp.quad_form(X, P) + q.T @ X)
constraint_list = list()
constraint1 = G @ X <= h
constraint_list.append(constraint1)
constraint2 = A @ X == b
constraint_list.append(constraint2)

'''
checking for dcp
'''
print("objective_function is dcp or not",obj_function.is_dcp())
for c in constraint_list:
    print("constraint dcp or not",c.is_dcp())

'''
solving the problem
'''
prob = cp.Problem(obj_function,constraint_list)
prob.solve()
# Print result.
print("\nThe optimal value is", prob.value)
print("A solution x is")
print(X.value)
print("A dual solution corresponding to the inequality constraints is")
print(prob.constraints[0].dual_value)

# checking the sum of obtained X value
float_matrix = X.value
rows = float_matrix.shape[0]
cols = float_matrix.shape[1]
int_matrix = np.zeros(shape=(rows,cols))
for i in range(0,rows):
    for j in range(0,cols):
        val = float_matrix[i][j]
        int_value = int(val)+(1 if (val - int(val)) >0.9 else 0)
        int_matrix[i][j] = int_value


print("integer matrix is:",int_matrix)