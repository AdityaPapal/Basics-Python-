from array import *
arr= array('i',[])
n=int(input('Enter the length of the Array : '))
for i in range(n):
    i =int(input("Enter the integer value for Array : "))
    arr.append(i)
print(arr)

val=int(input("Enter the num for searching index num : "))
# check Index number maually
k=0
for e in arr:
    if val==e:
        print('The Index num of ',val,'is ',k)
        break
    k+=1

# method using inbluid Function
print('Index using inbluid function',arr.index(val))