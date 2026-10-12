import random
fruits= ["Apple", "Banna", "Grapes", "Avocado"]

random_num = random.randint(20.40)
print("Random Number Generated", random_num)

random_fruit = random.choices(fruits)
print("Random Fruit Picked", random_fruit)