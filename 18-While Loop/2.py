# Print all  the value from 1 to 100 except divisible by 3 or 5

a= 1
while a<=100:
    if ((a%5 and a%3) != 0):
        print(a)
    a+=1