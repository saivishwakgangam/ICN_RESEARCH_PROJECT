# This module is to solve the mathematical model developed
import cvxpy as cp
import numpy as np

# Demographics
c = 5
e = 10
v = 20
# creating numpy matrices
# popularity matrix
popularity = np.array([0.1,0.3,0.4,0.1,0.1])
popularity = popularity.reshape(1,5)
print(popularity)
# request matrix
request = np.array([100,50,20,40,30,12,80,30,20,10])
request = request.reshape(10,1)
print(request.shape)
print(request)
# length matrix(km)
coverage_length = np.array([10,20,5,20,10,3,5,5,8,8])
coverage_length = coverage_length.reshape(10,1)
print("coverage length matrix is",coverage_length)
# jam density matrix(vehicles per km)
jam_density = np.array([10,10,18,12,12,8,9,11,11,9])
jam_density = jam_density.reshape(10,1)
print("jam density matrix is",jam_density)
# bandwidth between edge node and vehicles
band_e_v = np.array([100,100,100,100,100,100,100,200,100,200])
band_e_v = band_e_v.reshape(10,1)
print("bandwidth edge node vehicles matrix",band_e_v)
# bandwidth between edge nodes
band_e_e = np.full((10,10),100,dtype=int)
print("bandwidth edge node to edge node",band_e_e)
# bandwidth between edge node and server
band_e_s = np.full((10,1),100,dtype=int)
print("bandwidth edge node to server",band_e_s)
# file size of each content(MB)
size_matrix = np.array([500,1000,1000,2000,1200])
size_matrix = size_matrix.reshape(1,5)
print("file size matrix is",size_matrix)
# transmission delay between edge node and vehicle

# A = np.random.randn(m, n)
# b = np.random.randn(m)

# # Construct the problem.
# x = cp.Variable(n)
# objective = cp.Minimize(cp.sum_squares(A @ x - b))
# constraints = [0 <= x, x <= 1]
# prob = cp.Problem(objective, constraints)

# # The optimal objective value is returned by `prob.solve()`.
# result = prob.solve()
# # The optimal value for x is stored in `x.value`.
# print(x.value)
# # The optimal Lagrange multiplier for a constraint is stored in
# # `constraint.dual_value`.
# print(constraints[0].dual_value)


