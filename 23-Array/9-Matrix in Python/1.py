from numpy import *
arr1=array([
                    [1,2,3],
                    [4,5,6]
                 ])
print(arr1)
print(arr1.size)
print(arr1.ndim)

#covert 2D array to 1D array

arr2=arr1.flatten()
print(arr2)
print('\n')
arr3=array([
                    [1,2,3,4,5,6],
                    [6,7,8,9,10,11]
                    ])

arr=arr3.reshape(3,4)
print(arr)
print('\n')
arr=arr3.reshape(2,2,3)
print(arr)