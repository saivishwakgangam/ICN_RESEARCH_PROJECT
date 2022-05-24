import cvxpy as cp
import numpy as np

'''
Variables Initialization
'''
e_nodes = 3
files = 3

'''
Assume edge nodes are in a straight line (e1-----e2------e3)
Assume equal share of bandwidth between all vehicles in an edge node
Assume 
'''

# popularity matrix
p_matrix = np.array([0.2,0.5,0.3])
p_matrix = p_matrix.reshape((1,files))

# Length Matrix(km)
coverage_length = np.array([1,2,4])
coverage_length = coverage_length.reshape(e_nodes,1)

# jam density matrix(vehicles per km)
jam_density = np.array([20,20,18])
jam_density = jam_density.reshape(e_nodes,1)

# bandwidth(Mbps) between edge node and vehicles
band_e_v = np.array([100,200,50])
band_e_v = band_e_v.reshape(e_nodes,1)

# bandwidth(Mbps) between edge nodes -> shape(edge_nodes,edge_nodes)
band_e_e = np.array([[0,50,70],[50,0,100],[40,60,0]])
print("band_e_e shape is:",band_e_e.shape)
print("band_e_e is ",band_e_e)

# size matrix -> size of each file -> shape (files,1)
size_matrix = np.array([300,400,200])
size_matrix = size_matrix.reshape(files,1)

# maximum size matrix -> maximum size at each node
max_size_matrix = np.array([1200,1200,1100])
max_size_matrix = max_size_matrix.reshape(1,e_nodes)


# preparation of constant denominator
val_sum = 0
for e in range(0,e_nodes):
    c_val = band_e_v[e][0]/(jam_density[e][0]*coverage_length[e][0])
    val_sum = val_sum + (1/c_val)


provide_delay = np.zeros(shape=(e_nodes,1))
# accessing band_e_e matrix
for i in range(0,e_nodes):
    temp_sum = 0
    for j in range(0,e_nodes):
        if i != j:
            temp_sum = temp_sum + (1/band_e_e[i][j])
    
    provide_delay[i][0] = val_sum+temp_sum


'''
Performing Optimization
'''
X = cp.Variable(shape=(files,e_nodes))
obj_function = cp.Minimize(p_matrix@(X@provide_delay))

# Constraints 
constraint_list = list()

# Sum constraint
one_matrix = np.ones(shape=(e_nodes,1))
constraint1 = X @ one_matrix == size_matrix  
constraint_list.append(constraint1)

# Maximum Cacheable Size Node constraint
temp_ones = np.ones(shape=(1,files))
constraint2 = temp_ones @ X == max_size_matrix
constraint_list.append(constraint2)

# perform optimization
print("objective_function is dcp or not",obj_function.is_dcp())
for c in constraint_list:
    print("constraint dcp or not",c.is_dcp())

# optimization problem
prob = cp.Problem(obj_function,constraint_list)
prob.solve()

# Print Result
print("\nThe optimal value is", prob.value)
print("A solution x is")
print(X.value)
print("A dual solution is")
print(prob.constraints[0].dual_value)


   