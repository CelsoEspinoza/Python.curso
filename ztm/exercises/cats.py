#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 1 Instantiate the Cat object with 3 cats
shushu = Cat('Shushu', 4)
chicky = Cat('Chiky', 7)
luna = Cat('Luna', 1)


# 2 Create a function that finds the oldest cat

def oldest(cats):
    oldest = None
    for cat in cats:
        if (oldest == None):
            oldest = cat
        oldest = cat if (cat.age > oldest.age) else oldest

    return oldest

oldest_cat = oldest([shushu, chicky, luna])

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

print(f'The oldest cat({oldest_cat.name}) is {oldest_cat.age} years old.')