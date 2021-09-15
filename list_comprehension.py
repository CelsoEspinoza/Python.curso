
def main():
    numbers_string = input("Escribe los numeros multiplos separados por comas que deseas ver (ej: 4,6,9): ")
    strip_numbers = numbers_string.split(',')
    strip_numbers = [int(num.strip()) for num in strip_numbers]
    list = [i for i in range(1, 100000) if repeat_conditions(i, strip_numbers)]
    print(list)


def is_multiple_by(num, multiple):
    return num % multiple == 0


def repeat_conditions(i, mult_numbers):
    if len(mult_numbers) == 0:
        return True
    first_multiple = mult_numbers[0]
    return is_multiple_by(i, first_multiple) & repeat_conditions(i, mult_numbers[1:])


if __name__ == '__main__':
    main()