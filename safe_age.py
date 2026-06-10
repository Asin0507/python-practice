try:
    age=int(input("Enter age:"))
    print("Your age is:",age)
except ValueError:
    print("Please enter a valid number!")
    