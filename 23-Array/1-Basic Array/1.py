import array as arr

vals =arr.array('i',(1,3,4,5))
print(vals.typecode,"Type code !")

for i in range(len(vals)):
    print(vals[i])

x=10
vals.append(x)
print(vals )

