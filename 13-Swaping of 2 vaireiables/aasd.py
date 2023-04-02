# Method 1
a=5
b=6

temp = a
a=b
b=temp

print ("a =",a,"\nb =",b)

# Method 2
x= 5
y= 6

x=x+y # 5+6 = 11
y=x-y # 11-6 = 5
x=x-y # 11-5 = 6

print('x =',x,'\ny =',y)

# Method 3
m=5
n=6

m,n=n,m

print('m =',m,'\nn =',n)