# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 

num = int(input("Pick a number buckaroo: "))

if num % 4 == 0:
    print("Giddyup")
elif num % 2 == 0:
    print("Yee Haw")
else:
    print("ACAB")

