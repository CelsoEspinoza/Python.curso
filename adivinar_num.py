
import random
import os

def main():
    condition = False
    num_random = 0
    while not condition:
        os.system("cls")
        number_found = False
        begining()
        count = 0
        nivel = int(input("¿Qué nivel elegirá usted? "))
        if nivel == 1:
            print("Rango: 1 - 5")
            print("Hello little boy...")
            num_random = random.randint(1,5)
        elif nivel == 2:
            print("Rango: 1 - 20")
            print("Está bien para iniciar")
            num_random = random.randint(1,20)
        elif nivel == 3:
            print("Rango: 1 - 100")
            print("Good luck...")
            num_random = random.randint(1,100)
        elif nivel == 4:
            print("Rango: WHO KNOWS")
            print("You must be stupid!")
            num_random = random.randint(-999999999,999999999)
        elif nivel == 0:
            break
        else:
            print("Debes elegir uno de los indicados DUMBASS!! ")
            break
            input("")
        while not number_found:
            number = int(input("Intenta un número: "))
            if nivel == 1:
                if number == num_random:
                    print("¡Felicidades bebé, te mereces una palmada en la nalga izquierda!")
                    input("")
                    number_found = True

                elif number > num_random:
                    print("El número es más pequeño")
                else:
                    print("El número es más grande")
            elif nivel == 2:
                if number == num_random:
                    print("¡Bien jugado!")
                    input("")
                    number_found = True

                elif number > num_random:
                    print("El número es más pequeño")
                else:
                    print("El número es más grande")
            elif nivel == 3:
                if number == num_random:
                    print("WOW, you are good!")
                    input("")
                    number_found = True
                else:
                    count += 1
                    print("Intento {} fallidooo...".format(count))
                    if count == 4:
                        print("Last chance")
                    elif count == 5:
                        print("No sirves para esto :C")
                        print("El número era {}".format(num_random))
                        input("")
                        break
            elif nivel == 4:
                if number == num_random:
                    print("ERES MI DIOS... ¡Alabado seas!")
                    input("")
                    number_found = True
                else:
                    count +=1
                    print("Intento {} fallidooo...".format(count))
                    if count == 5:
                        print("Date por vencido!!")
                    elif count == 15:
                        print("No entiendo tu terquedad...")
                    elif count == 50:
                        print("Seguro que eres un idiota, no lo dudo...")
                    elif count == 200:
                        print("Wow... te has ganado mis respetos")
                        print("Te regalaré el número: {}".format(num_random))
                        number_found = True
                        input("")
            else:
                print("")
    print("Gracias por jugar")
    input("")


def begining():
    print("==================================")
    print("...LET THE GAME BEGINS...")
    print("==================================")
    print("Niveles: 1:pollito 2:básico 3:difícil 4:IMPOSIBLE 0:Salir")

if __name__ == "__main__":
    main()
