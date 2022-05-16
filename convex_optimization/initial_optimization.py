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
f = 1
'''
initialization of matrices
'''
# popularity matrix
p_matrix = np.array([1])
p_matrix = p_matrix.reshape((1,f))
# creating a dummy transmission delay of size (e_nodes * 1)
d_tr_e_v = np.array([20,30,40])
d_tr_e_v = d_tr_e_v.reshape(e_nodes,1)
# creating dummy transmission delay between edge nodes shape -> (edge_nodes * 1)
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
c_time = np.array([200,33,500])
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
# # Add Mobility Constraint
# # there will be two constraints
# constraint2 = X @ d_tr_e_v <= X @ c_time
# constraints.append(constraint2)
# # Adding Second Constraint
# temp_arr = np.zeros((e_nodes,e_nodes))
# for i in range(0,e_nodes):
#     temp_arr[i][i] = d_tr_e_v[i][0]


# right_temp = np.zeros((f,e_nodes))
# for i in range(0,f):
#     for j in range(0,e_nodes):
#         right_temp[i][j] = c_time[j][0]

# print("temp_matrix is",temp_arr)
# print("right_temp matrix is",right_temp)
# expr1 = (1-X) @ temp_arr
# expr2 = (X) @ d_tr_e_e
# final_expr = expr1 + expr2
# print("final expression shape is",final_expr.shape)
# # Constraint 3 
# constraint3 = X @ d_tr_e_e <= X @ c_time
# constraints.append(constraint3)
# # Constraint 4

# constraint4 = final_expr <= right_temp
# constraints.append(constraint4)
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