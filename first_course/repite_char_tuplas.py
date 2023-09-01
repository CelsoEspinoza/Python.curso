

def main():
    char_sequence = input("Escribe una secuencia de caracteres: ")
    char_choisen = not_repited(char_sequence)
    if char_choisen == "_":
        print("Todas la letras se repitan más de una vez")
    else:
        print("La primera letra que NO se repite es: {}".format(char_choisen))




def not_repited(sequence):
    letras_vistas = {}

    for idx, letter in enumerate(sequence):
        if letter not in letras_vistas:
            letras_vistas[letter] = (idx, 1)
        else:
            letras_vistas[letter] = ( letras_vistas[letter][0], letras_vistas[letter][1] +1)
    lista_vista = []
    for key, value in letras_vistas.items():
        if value[1] == 1:
            lista_vista.append((key,value[0]))

    sorted_lista = sorted(lista_vista, key = lambda value: value[1])

    if sorted_lista:
        return sorted_lista[0][0]
    else:
        return "_"


if __name__ == "__main__":
    main()
