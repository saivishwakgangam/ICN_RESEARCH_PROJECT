import cvxpy as cp
import numpy as np
'''
Initilization
'''
edge_nodes = 3
files = 1
# considering popularity of files
f_pop = np.array([1])
f_pop = f_pop.reshape(1,files)
# size of file matrix(MB)
matrix_size = np.array([500])
matrix_size = matrix_size.reshape(files,1)
# edge to edge transmission delay
tr_e_e = np.array([2,3,4])
tr_e_e = tr_e_e.reshape(edge_nodes,1)
# prepare total delay matrix
sum_list = list()
for c in range(0,files):
    sum = 0
    for i in range(0,edge_nodes):
        sum = sum + tr_e_v[i][c]
    sum_list.append(sum)

total_delay = np.zeros((edge_nodes,files))
for c in range(0,files):
    for i in range(0,edge_nodes):
        temp_val = sum_list[c]-tr_e_v[i][c]
        temp_val = temp_val + (edge_nodes - 1) * tr_e_e[i][c]
        total_delay[i][c] = temp_val

print("total delay is",total_delay)
# initializing ones matrix
one_matrix = np.ones(shape=(edge_nodes,1)) 
# optimization function
X = cp.Variable(shape=(files,edge_nodes))
print("shape of cp variable is",X.shape)
expr1 = X @ tr_e_v
expr2 = X @ total_delay
o_func = f_pop @ (expr1 + expr2)
print("shape of min_function",o_func.shape)
# Adding sum of file segments should be total size
constraints = list()
constraint1 = X @ one_matrix == matrix_size
constraints.append(constraint1)
# constraint on value of matrix
constraint2 = X >= 0
constraints.append(constraint2)
# Adding Mobility and Bandwidth Constraint

# checking whether dcp or not
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


