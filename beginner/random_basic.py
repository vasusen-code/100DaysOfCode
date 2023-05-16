# Random module
import random #inbuilt module

# Choose a random integer btw 1 and 10 (including 1 and 10)
random_int = random.randint(1, 10)
print(random_int)

# choose a random float (decimal) btw o to 1 (0.000000... to 0.999999...)
random_float = random.random()
print(random_float)

# choose a random float btw 1 to 5 (0.000.. to 4.99999....)
print(random_int * random_float)

# Make a choice of random of item from a list
random_item = random.choice(["Mahesh", "maahi", "Vasusen", "karn"])
print(random_item)
