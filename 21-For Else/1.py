# for else
num_list=[12,23,35,67,88,80]

for num in num_list:
    if num% 5==0:
        print(num)
        break
else:
    print("not found")