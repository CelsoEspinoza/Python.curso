
# Square
my_list = [5,4,3]

print(list(map(lambda i: i ** 2, my_list)))

#List sorting
a = [(0,2), (4,3), (9,9), (10,-1)]

sorted_list = sorted(a, key=lambda i: i[1])
print(sorted_list)

print(dict(sorted_list))