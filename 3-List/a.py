# list in python
num = [25,34,54,56,10]
print(num[0])
print(num[2:])

names=['aditya','vitthal','papal']

all=[num,names]

print(all)

num.insert(2,20)
print(num)

del num[3:]
print(num)

num.extend([1,2,3,4,5])
print(num)

print('Max :',max(num))
print('Min :',min(num))
print('Sum :',sum(num))

num.sort()
print(num)

