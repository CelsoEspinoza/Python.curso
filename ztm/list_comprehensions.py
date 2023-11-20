

my_list = [char for char in 'Hello Celestial']
my_list2 = [num for num in range(0,100)]
my_list3 = [num**2 for num in range(0,100)]
my_list4 = [num*2 for num in range(0,100) if num % 2 != 0]

# print(my_list4)

# set conprehension. Same as list

my_list5 = {char for char in 'Hello Celestial'}

# print(my_list5)

# dictionary conprehension.

simple_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}

my_dict = { key:value**2 for key,value in simple_dict.items() if value % 2 != 0 }
my_dict2 = { num:num**2 for num in [1,2,3,4] }

print(my_dict2)
