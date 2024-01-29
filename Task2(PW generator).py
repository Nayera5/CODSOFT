import random
import string
l=int(input("Enter the desired length of the password : \n"))
#join the characters into one string with '' _no space_
password =''.join(random.choices(string.ascii_letters + string.digits + string.punctuation ,k=l))
print("Here's your strong password : " + str(password))
