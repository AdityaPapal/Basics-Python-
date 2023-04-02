# collect all even num from list
def Num_list(n_list):
    Even_number_list=[]
    for num in n_list:
        if num%2==0:
            Even_number_list.append(num)
        else :
            pass
    result= print(Even_number_list)
    return result

user_list=[]
for num in range(1,6):
    n=int(input("Enter the number for list: "))
    user_list.append(n)

Num_list(user_list)