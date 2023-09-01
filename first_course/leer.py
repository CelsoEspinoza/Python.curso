


def main():
    cont = 0
    word = input("Escribe qué palabra deseas buscar en el cuento: ")
    with open("cuento.txt","r") as f:
        for line in f:
            cont += line.count(word)
    print("La palabra '{}' es mencionada {} veces en el cuento.".format(word,cont))


if __name__ == "__main__":
    main()
