

def main():

    countries = {
        "mexico":122,
        "colombia":49,
        "argentina":43,
        "chile":18,
        "peru":31
    }

    while True:
        country = input("Escribe el nombre de un país: ").lower()
        try:
            print("La población de {} es {} millones".format(country, countries[country]))
        except KeyError:
            print("El país no se encuentra en nuestra base de datos")
        

if __name__ == "__main__":
    main()
