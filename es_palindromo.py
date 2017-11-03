

def main():
    palabra = input("Escribe la palabra a evaluar: ")
    reversa = palabra[::-1]
    if palabra == reversa:
        print("La palabra {} es palíndroma".format(palabra))
    else:
        print("La palabra no es palíndroma")

    input("")

if __name__ == "__main__":
    main()
