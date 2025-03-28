import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#1st Option
names = random.choice(friends)
print(f"The {names} pay the bill")

#2nd Option
random_index = random.randint(0, 4)
print(friends[random_index])