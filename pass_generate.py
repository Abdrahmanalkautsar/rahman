import random

nama = input("Masukkan nama kamu: ")
print("berikut password yang cocok: ")

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "@#$%&*/\?"

use_for = lower_case+upper_case+number+symbols
lenght_for_pass = 8

password1 = "".join(random.sample(use_for, lenght_for_pass))

password2 = "".join(random.sample(use_for, lenght_for_pass))

password3 = "".join(random.sample(use_for, lenght_for_pass))

password4 = "".join(random.sample(use_for, lenght_for_pass))

password5 = "".join(random.sample(use_for, lenght_for_pass))

print(password1)
print(password2)
print(password3)
print(password4)
print(password5)
