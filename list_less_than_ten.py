mylist = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

user_number = int(input("Hit me with a number my guy: "))
my_revised_list = []

for num in mylist:
    if num < user_number:
        my_revised_list.append(num)
    else:
        pass
    
print(my_revised_list)