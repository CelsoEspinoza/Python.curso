
from functools import reduce

def accumulator(acc, item):
    print(acc, item)
    return acc + item

my_list = [1,2,3,4, 5]
print(list(map(lambda i: i*2, my_list)))
print(list(filter(lambda i: i % 2 != 0, my_list)))
# print(my_list)

# list2= [5,6,7, 6, 3]
# print(list(zip(my_list, list2)))

print(reduce(lambda acc, item: acc + item, my_list, 0))
