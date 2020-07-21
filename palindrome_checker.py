#Ask the user for a string and print out whether this string is a palindrome or not. 
#(A palindrome is a string that reads the same forwards and backwards.)

user_string = input("Hit me with a word homie: ")

reversed_user_string = user_string[::-1]

if user_string == reversed_user_string:
    print("that there is a proper Sarah Palindrome my guy.")
else: 
    print("More like Palin-dumb, amirite?")
    