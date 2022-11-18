import random

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special_chars = "!@#$%^&*()|?\/"

Use_for = lowercase + uppercase + numbers + special_chars
pass_len = 8

password = "".join(random.sample(Use_for, pass_len))

print("Your generated password is: " + password)