username = input('Write your username: ')
password = input('Write your password: ')

length_pass = len(password)
hidden_pass = '*' * length_pass

print(f'{username}, your password {hidden_pass} is {length_pass} letters long')
