def super_funct(*args, **kwargs):
    print(args) # tuple
    print(kwargs) # dictionary
    return sum(args) + sum(kwargs.values())

print(super_funct(1,2,3,4,5, num1=2, num2=6))

# Rule: params, *args, default parameters, **kwargs