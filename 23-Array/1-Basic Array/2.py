import array as arr

data =arr.array('i',(1,2,3,4,5))
print(data)
newData=arr.array(data.typecode,(a*a for a in data))
print(newData)