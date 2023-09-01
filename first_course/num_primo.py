
def main():
    num = int(input("Escribe el número a evaluar: "))
    show_result(is_primo(num))
    input("")

def is_primo(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False

    return True

def show_result(cond):
    if cond is True:
        print("El número es primo")
    elif cond is False:
        print("El número no es primo")
    else:
        print("Error")


if __name__ == "__main__":
    main()
