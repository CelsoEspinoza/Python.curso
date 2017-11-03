
import random
import os

IMAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def main():
    print(IMAGES[0])
    print("")
    frase_juego = frases_para_jugar()
    print("LA FRASE CON LA QUE JUGAMOS ES:")
    frase_tapada = tapando_frase(frase_juego)
    print(frase_tapada)
    contador = 0
    choose_char(frase_juego, frase_tapada, contador)

def cabecera_juego():
    print("==================================================================")
    print("              J U G U E M O S _ A H O R C A D O S              ")
    print("==================================================================")
    print("Elije la letra que creas conveniente para completar la frase...  ")
    print("")



def frases_para_jugar():
    lista_frases = ["La vida es bella",
                    "El princio del fin",
                    "Por fin pude terminar el programa",
                    "Los ojos azules de mi amor",
                    "A palazos aprendi, mi labor de colegial",
                    "Como cuando no se te ocurre que frase poner",
                    "Parangaracutilimicuaron",
                    "Y asi fue la historia de mi vida",
                    "You have to go home to study all day",
                    "Practice makes perfect"]
    num_random = random.randint(0,len(lista_frases)-1)
    frase_elegida = lista_frases[num_random]
    return frase_elegida


def choose_char(frase_juego, frase_tapada, contador):
    cond = False
    frase_juego_lista = list(frase_juego)
    frase_tapada_lista = list(frase_tapada)
    frase_actualizada = frase_tapada
    while not cond:
        cont = 0
        letra_elegida = input("Elige una letra: ")
        for char in frase_juego_lista:
            if char.upper() == letra_elegida.upper():
                frase_tapada_lista[frase_juego_lista.index(char)] = char
                frase_juego_lista[frase_juego_lista.index(char)] = "*"
                cont += 1

        if cont == 0:
            contador += 1
            if contador == 7:
                os.system("cls")
                cabecera_juego()
                print("¡Fuiste ahorcado! Perdiste el juego...")
                print("La frase era :")
                print(frase_juego)
                print(IMAGES[contador-1])
                input("")
                break
            else:
                os.system("cls")
                cabecera_juego()
                print(IMAGES[contador])
                print("")
                print(frase_actualizada)
                print("Intendo {} fallido ".format(contador))
                print("")
        else:
            os.system("cls")
            cabecera_juego()
            print(IMAGES[contador])
            print(frase_actualizada)
            print("La letra ({}) es correcta".format(letra_elegida))
            frase_actualizada = "".join(frase_tapada_lista)
            print(frase_actualizada)
            print("")
        if frase_juego.upper() == frase_actualizada.upper():
            print("FELICIDADES... ¡¡¡FRASE COMPLETADA!!!")
            input("")
            cond = True



def tapando_frase(frase):
    frase_list = list(frase)
    lenght = len(frase)
    trescuatros = int(3*lenght/4)
    medio = int(lenght/2)
    cantidad_tapados = random.randint(medio, trescuatros)
    for i in range(cantidad_tapados):
        index_tapados = random.randint(0,lenght-1)
        if (frase_list[index_tapados] != " "
                    and frase_list[index_tapados] != ","
                    and frase_list[index_tapados] != "."
                    and frase_list[index_tapados] != "*"):
            letra = frase_list[index_tapados]
            for char in frase_list:
                if char.upper() == letra.upper():
                    frase_list[frase_list.index(char)] = "*"

    frase_tapada = "".join(frase_list)
    return frase_tapada

if __name__ == "__main__":
    cabecera_juego()
    main()
