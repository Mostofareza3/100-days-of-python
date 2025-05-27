import random

letters = ["A", "B", "C", "D", "E", "F"]
small_letters = ["a", "b", "c", "d", "e", "f"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
special_char = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


all_chars = letters + small_letters + numbers + special_char


pass_len = int(input("Enter password length: "))

password = ""
for i in range(pass_len):
    password += random.choice(all_chars)

print(password)
print(random.shuffle(all_chars))

# import the random module
import random

# declare a list
sample_list = ['A', 'B', 'C', 'D', 'E']

print("Original list : ")
print(sample_list)

# first shuffle
random.shuffle(sample_list)
print("\nAfter the first shuffle : ")
print(sample_list)

# second shuffle
random.shuffle(sample_list)
print("\nAfter the second shuffle : ")
print(sample_list)