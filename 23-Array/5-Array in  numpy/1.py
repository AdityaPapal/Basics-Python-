from numpy import *

arr=array([1,2,3,4,5],int)
print(arr.dtype)
print(arr)

# becouse of 5.0 its covert into float type
arr1=array([1,2,3,4,5.0])
print(arr1.dtype)
print(arr1)

# we can convert  it float by declearing
arr2=array([1,2,3,4,5],float)
print(arr2.dtype)
print(arr2)
