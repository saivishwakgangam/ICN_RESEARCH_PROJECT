import numpy as np
import cvxpy as cp
# new file optimization
# let file size is 100 MB and aim is to segment the whole file 
arr1 = np.array([1,2,3])
arr1 = arr1.reshape(3,1)
arr2 = np.array([5,6,7])
arr2 = arr2.reshape(3,1)
arr3 = np.array([9,10,11])
arr3 = arr3.reshape(3,1)
arr1 = np.concatenate((arr1,arr2,arr3))
print(arr1.shape)
id1 = np.identity(3)
id2 = np.ones(shape=(3,3))
id1 = np.concatenate((id1,id2))
print(id1)
print("shape of identity matrix is:",id1)










