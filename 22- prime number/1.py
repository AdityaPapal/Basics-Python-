num = int(input('Enter the Number : '))
for i in range(2,num):
    if num % i ==0:
        print("Its not a Prime Number!")
        break
else:
    print("Its a Prime number! ")
