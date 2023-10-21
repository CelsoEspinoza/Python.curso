# assigns values to variables as part of a larger expression

a = 'heelloooooooo'

# if (len(a) > 10):
#     print(f'too long, {len(a)} chars')

if (n := len(a)) > 10:
    print(f'too long, {n} chars')

while (n := len(a)) > 1:
    print(n)
    a = a[:-1]

print(a)