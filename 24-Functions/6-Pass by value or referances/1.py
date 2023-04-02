def ubdate(x):
    print(id(x))
    x=20
    print(x)
    print(id(x))

ubdate(10) # this is pass by value becouse we direct call the value in function
a = 25
print(id(a))
ubdate(a) # this is pass by referance becouse we can pass address of variable in function