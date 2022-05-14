'''
This file is used for experimentation
'''
import cvxpy as cp
import numpy as np
'''
variables
'''

e_nodes = 3
v = 3
f = 2

'''
initialization of matrices
'''
# popularity matrix
p_matrix = np.array([0.1,0.9])
p_matrix = p_matrix.reshape((1,f))
# request matrix
request = np.array([100,50,20])
request = request.reshape(1,e_nodes)
# Length Matrix(km)
coverage_length = np.array([10,20,5])
coverage_length = coverage_length.reshape(e_nodes,1)
# jam density matrix(vehicles per km)
jam_density = np.array([10,10,18])
jam_density = jam_density.reshape(e_nodes,1)
# bandwidth between edge node and vehicles
band_e_v = np.array([100,200,50])
band_e_v = band_e_v.reshape(e_nodes,1)
# bandwidth between edge nodes
band_e_e = np.full((3,3),100,dtype=int)
# bandwidth between edge node and server
band_e_s = np.full((3,1),100,dtype=int)
print("bandwidth edge node to server",band_e_s)
# file size of each content(MB)
size_matrix = np.array([100,400,600])
size_matrix = size_matrix.reshape(1,3)
print("file size matrix is",size_matrix)
# Transmission Delay between edge node and vehicle
temp_list = list()
for c in range(0,f):
    t_list = list()
    for i in range(0,e_nodes):
        time_req = (size_matrix[0][c]*(jam_density[i][0]*coverage_length[i][0]))/(band_e_v[i][0])
        t_list.append(time_req)
    temp_list.append(t_list)

tr_e_v = np.array(temp_list)
# Transmission Delay Between Two Edge Nodes
temp_list = list()
for c in range(0,f):
    t_list = list()
    for i in range(0,e_nodes):
        time_req = size_matrix[0][c]/100
        t_list.append(time_req)
    
    temp_list.append(t_list)
tr_e_e = np.array(temp_list)
# Transmission Delay Between server and edge node
temp_list = list()
for c in range(0,f):
    time_req = size_matrix[0][c]/100
    temp_list.append(time_req)

tr_e_s = np.array(temp_list)
tr_e_s =tr_e_s.reshape(f,1)
print("contents of array is",tr_e_s)
print("shape of array is",tr_e_s.shape)

# creating a dummy transmission delay of size (e_nodes * 1)
# d_tr_e_v = np.random.randint(1,100,(e_nodes,1))
# print("dummy transmission delay is",d_tr_e_v)
d_tr_e_v = np.array([20,30,40])
d_tr_e_v = d_tr_e_v.reshape(e_nodes,1)
# creating dummy transmission delay between edge nodes shape -> (edge_nodes * 1)
# d_tr_e_e = np.random.randint(1,100,(e_nodes,1))
# print("dummy edge to edge delay",d_tr_e_e)
d_tr_e_e = np.array([2,9,5])
d_tr_e_e = d_tr_e_e.reshape(e_nodes,1)
# creation of total delay matrix
sum = 0
for index in range(0,e_nodes):
    sum = sum + d_tr_e_v[index][0]

t_delay_list = list()
for index in range(0,e_nodes):
    temp_var = (sum-d_tr_e_v[index][0]) + (e_nodes-1)*(d_tr_e_e[index][0])
    t_delay_list.append(temp_var)

total_delay = np.array(t_delay_list)
total_delay = total_delay.reshape(e_nodes,1)
# creation of coverage area matrix shappe (e_nodes * 1)->seconds
c_time = np.array([200,700,500])
c_time = c_time.reshape(e_nodes,1)
print("total_delay shape is",total_delay)
'''
creation of optimization problem
'''
# initialization of optimization variable
X = cp.Variable(shape=(f,e_nodes),boolean=True)
ones = np.full((e_nodes,1),1,dtype=int)
temp_ones = np.full((f,1),1,dtype=int)
objective_function = p_matrix@(X @ d_tr_e_v + X @ total_delay)
print(objective_function.shape)
'''
creation of constraints
'''
constraints = list()
# content is present in exactly one node
constraint1 = cp.matmul(X,ones) == 1
constraints.append(constraint1)
# Add Mobility Constraint
# there will be two constraints
constraint2 = cp.matmul(X,d_tr_e_v) <= 
o_func = cp.Minimize(objective_function)
print("objective_function is dcp or not",o_func.is_dcp())
for c in constraints:
    print("constraint dcp or not",c.is_dcp())
# optimization problem
prob = cp.Problem(cp.Minimize(objective_function),constraints)
prob.solve(solver=cp.GUROBI)
# Print Result
print("\nThe optimal value is", prob.value)
print("A solution x is")
print(X.value)
print("A dual solution is")
print(prob.constraints[0].dual_value)








