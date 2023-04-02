# Find greatest value from  the user
# method 1
# a= int(input('Enter the value for a : '))
# b = int(input('Enter the value for b : '))
# c= int(input('Enter the value for c : '))
# method 2
a,b,c=input("Enter the 3 values : ").split()
print('a = ',a,'b = ',b ,'c = ',c)

if(a > b and a>c):
    print('The value a is greater')
elif(b>a and b>c):
    print('The value  b is greater ')
elif(c>a and c>b) :
    print( 'The value of c in greater')
else :
    print('Number is invalid')