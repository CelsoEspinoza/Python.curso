def highest_even(li):
    if len(li) == 0:
        print('There is no numbers is list')
        return

    highest_num = None
    for item in li:
        is_even_number = is_even(item)
        if is_even_number:
            if highest_num is None:
                highest_num = item
                continue
            highest_num = get_greater(highest_num, item)
    
    print(f'The highest numer is {highest_num}')
    return highest_num

def is_even(num):
    return num % 2 == 0

def get_greater(num1, num2):
    if (num1 > num2):
        return num1
    else:
        return num2

# highest_even([])
highest_even([9,122,3,56,1,22,1,25])