import cvxpy as cp
import numpy as np
import cvxpy.atoms.affine as af
'''
Initialisation Of Variables
'''
e_nodes = 3
f = 2
'''
Initialisation Of Matrices
'''
# popularity matrix
p_matrix = np.array([0.5,0.5])
p_matrix = p_matrix.reshape((1,f))
# request matrix
request = np.array([100,50,20])
request = request.reshape(1,e_nodes)
# Length Matrix(km)
coverage_length = np.array([1,2,5])
coverage_length = coverage_length.reshape(e_nodes,1)
# jam density matrix(vehicles per km)
jam_density = np.array([100,100,18])
jam_density = jam_density.reshape(e_nodes,1)
# bandwidth between edge node and vehicles
band_e_v = np.array([100,200,50])
band_e_v = band_e_v.reshape(e_nodes,1)
# bandwidth between edge nodes
band_e_e = np.array([25,50,40])
band_e_e = band_e_e.reshape(e_nodes,1)
# file size of each content(MB)
size_matrix = np.array([100,100])
size_matrix = size_matrix.reshape(1,f)
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
tr_e_v = tr_e_v.reshape(e_nodes,f)
print("edge to vehicles shape is",tr_e_v.shape)
print("edge to vehicle",tr_e_v)
# Transmission Delay Between Two Edge Nodes
temp_list = list()
for c in range(0,f):
    t_list = list()
    for i in range(0,e_nodes):
        time_req = size_matrix[0][c]/band_e_e[i][0]
        t_list.append(time_req)
    
    temp_list.append(t_list)
tr_e_e = np.array(temp_list)
tr_e_e = tr_e_e.reshape(e_nodes,f)
print("edge to edge shape is",tr_e_e.shape)
print("edge to edge",tr_e_e)
# Constructing Total Delay
# creation of sum list
sum_list = list()
for c in range(0,f):
    sum = 0
    for i in range(0,e_nodes):
        sum = sum + tr_e_v[i][c]
    sum_list.append(sum)

total_delay = np.zeros((e_nodes,f))
for c in range(0,f):
    for i in range(0,e_nodes):
        temp_val = sum_list[c]-tr_e_v[i][c]
        temp_val = temp_val + (e_nodes - 1) * tr_e_e[i][c]
        total_delay[i][c] = temp_val

print("total delay is",total_delay)
# Construction Of Coverage Area Matrix (e * 1)
# c_time = np.zeros((e_nodes,1))
# for i in range(0,e_nodes):
#     c_time[i][0] = (coverage_length[i][0]*1000)/17
c_time = np.array([300,300,294.11])
c_time = c_time.reshape(e_nodes,1)
print("coverage area time is",c_time)
# Add Maximum Size of each node constraint -> Mb
max_size = np.array([300,200,400])
max_size = max_size.reshape((1,e_nodes))
# Construct Minimum Data Node can serve
min_data_served = np.zeros((e_nodes,1))
for i in range(0,e_nodes):
    # Assume each vehicle velocity is 17m/sec
    min_data = band_e_v[i][0]/((jam_density[i][0]/1000)*(17))
    min_data_served[i][0]= min_data

min_data_served = min_data_served.reshape((1,e_nodes))

'''
Construction Of Optimization Problem
'''

X = cp.Variable(shape=(f,e_nodes),boolean=True)
ones = np.full((e_nodes,1),1,dtype=int)
expr1 = cp.diag(X @ tr_e_v)
expr2 = cp.diag(X @ total_delay)
print("expr1 shape is",expr1.shape)
print("expr2 shape is",expr2.shape)
o_func = p_matrix @ (expr1 + expr2)
print("objective function shape is",o_func.shape)

'''
Construction Of Constraints
'''
constraints = list()
# content is present in exactly one node
constraint1 = cp.matmul(X,ones) == 1
constraints.append(constraint1)
# Adding Mobility Constraint
# Adding edge to vehicle constraint
expr3 = cp.diag(X @ tr_e_v)
expr4 = X @ c_time
expr3 = cp.reshape(expr3, (f,1))
constraint2 = expr3 <= expr4
constraints.append(constraint2)
# Adding edge to edge constraint
expr5 = cp.diag(X @ tr_e_e)
expr5 = cp.reshape(expr5,(f,1))
constraint3 = expr5 <= expr4
constraints.append(constraint3)
# Adding another constraint for every file
# Prepare right matrix
right_matrix = cp.diag(X @ tr_e_e)
right_matrix = cp.reshape(right_matrix,(f,1))
temp_var = (1-X)[0]
temp_var = cp.reshape(temp_var,(1,e_nodes))
print("content elements are",temp_var)
print("indexing shape is",temp_var.shape)
for c in range(0,f):
    # extract row from 1-X
    temp_var1 = (1-X)[c]
    temp_var1 = cp.reshape(temp_var1,(1,e_nodes))
    # preparation of right matrix from tr_e_v -> shape e_nodes * f
    zero_matrix = np.zeros((e_nodes,e_nodes))
    for i in range(0,e_nodes):
        zero_matrix[i][i] = tr_e_v[i][c]
    
    expr6 = temp_var1 @ zero_matrix
    # preparation of edge to edge delay matrix
    e_e_matrix = np.zeros((e_nodes,1))
    for i in range(0,e_nodes):
        e_e_matrix[i][0] = tr_e_e[i][c]
    
    temp_var2 = X[c]
    temp_var2 = cp.reshape(temp_var2, (1,e_nodes))
    epxr7 = temp_var2 @ e_e_matrix
    expr8 = expr6 + epxr7
    expr8 = cp.reshape(expr8,(e_nodes,1))
    constraint = expr8 <= c_time
    constraints.append(constraint)

# Add Maximum Size Constraint
constraint = size_matrix @ X <= max_size
constraints.append(constraint)
# Add Bandwidth Constraint
constraint = size_matrix @ X <= min_data_served
# checking for dcp
objective_function = cp.Minimize(o_func)
print("objective_function is dcp or not",objective_function.is_dcp())
for c in constraints:
    print("constraint dcp or not",c.is_dcp())

# solve the problem
prob = cp.Problem(objective_function,constraints)
prob.solve(solver=cp.GUROBI)

# Print Result
print("\nThe optimal value is", prob.value)
print("A solution x is")
print(X.value)
print("A dual solution is")
print(prob.constraints[0].dual_value)


    








    
    
















