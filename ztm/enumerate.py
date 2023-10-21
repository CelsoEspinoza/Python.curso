index_of_fifty = None
for i, char in enumerate(list(range(100))):
    if char == 50:
        index_of_fifty = i
        break

print(f'the index of 50 is {index_of_fifty}')