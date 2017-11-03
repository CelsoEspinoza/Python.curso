
def main():
    num = int(input("Escribe el número: "))
    result = factorial(num)
    print("El factorial es {}".format(result))
    input("")

def factorial(num):
    if num >= 1:
        fac = num * factorial(num-1)
    else:
        return 1

    return fac

if __name__ == "__main__":
    main()
