import random
import string
pool = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
length = int (input("Enter the password length: "))
password = "".join(random.sample(pool, length))
print("your password", password)
