a = int(input("Please enter your age: "))
b = input("What is your sex?(M/F/L): ")

if a > 18 and a < 22 and b == 'M':
    print("You can enter, but you cannot smoke in here.")

elif a > 18 and a < 22 and b == 'F':
    print("You can enter and get a VIP membership.")

elif a > 18 and a < 22 and b == 'L':
    print("You can enter. Please enjoy your time!")

elif a >= 22 and b == 'M':
    print("You can enter, have two free drinks but you cannot smoke in here!")

elif a >= 22 and b == 'F':
    print("You can enter, have two free drinks and get a VIP membership!")

elif a >= 22 and b == 'L':
    print("You can enter, have two free drinks! Please enjoy your time!")

else:
    print("You cannot enter.You must be 19.")
