from functools import reduce

#1 Capitalize all of the pet names and print the list
def capitalize(value):
    return value.upper()

my_pets = ['sisi', 'bibi', 'titi', 'carla']
my_pets_cap = list(map(capitalize, my_pets))
print(my_pets_cap)

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]
my_numbers_sorted = list(zip(sorted(my_numbers), my_strings))
print(my_numbers_sorted)

#3 Filter the scores that pass over 50%
def only_over_50(value):
    return value > 50

scores = [73, 20, 65, 19, 76, 100, 88]
scores_over_50 = list(filter(only_over_50, scores))
print(scores_over_50)

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

def accumulator(acc, item):
    return acc + item

all_combined = reduce(accumulator, my_numbers + scores, 0)
print(all_combined)

