

def run():
    print("C A L C U L A D O R A _ D E _ D I V I S A S")
    print("Convierte soles a pesos colombianos")
    print("")

    ammount = float(input("Ingresa la cantidad de Soles a convertir: "))

    foreign_exchange_calculator(ammount)

def foreign_exchange_calculator(ammount):
    colom = 927.24 * ammount
    print("{} soles es {} pesos colombianos ".format(ammount, colom))
    input("")


if __name__ == "__main__":
    run()
    print("C'est fini")
