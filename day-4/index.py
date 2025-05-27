# import random
#
# fruits = ["apple", "banana", "cherry", "orange", "strawberry", "mango"]
# print(f"random fruit:>> {random.choice(fruits)}")
# print(f"random shuffle:>> {random.shuffle(fruits)}")
# print(f"random current state:>> {random.getstate()}")
# print(f"random current shuffle:>> {random.shuffle(fruits)}")
# print(f"random integer:>> {random.randint(1, 100)}")
import random

# Class 2: List
number_list = [1, 2, 3, 4, "Hi", 6, 7, 8, True]
print(number_list)

#Friends
friends = ["Alice", "Bob", "Charlie", "Josh", "Luke", "Bao"]
otherFriends = ["Quang"]
randomNumber = random.uniform(0, len(friends))
print(friends[int(randomNumber)])
print(random.choice(friends))