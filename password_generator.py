import random
# passowrd generator
letters = ["A", "B", "C", "D", "E"]
figures = ["1", "2", "3", "4","5"]
symbols =  ["*", "&", "$","(", ")"]
print("Welcome to the password generator ")
user_name = input("the user name is required here!")
nr_letters = int(input("enter the numbers you want in your password"))
nr_numbers = int(input("enter the numbers you want in your password"))
nr_Symbol = int(input("enter the numbers you want in your password"))

# getting the number of letters in a password for a user 4
password = ""
for x in range(1, len(letters)):
    password_1 = random.choice(letters)
    password +=password_1 
    # print(password)

# now getting the numbers of figures to be used in password for a user 4
password_figure = ""
for y in range(1, len(figures)):
    password_2 = random.choice(figures)
    password_figure += password_2
    # print(password_figure)


# now getting the numbers of symbols to be used in password for a user 4
password_symbols = ""
for z in range(1, len(symbols)):
    password_3 = random.choice(symbols)
    password_symbols += password_3
# Now generating the password for the username
Real_password = password +password_figure+password_symbols
print(f"The username:{user_name} has the password {Real_password}")
# print(Numbers)
# print(Symbol)



                                                                                                                                                                      








