
import random

def main():
    print("Escribe el mensaje a encriptar")
    mensaje = input("")
    dic = diccionario(mensaje)
    men_encrip = encriptar(dic)
    print(men_encrip)


def diccionario(mensaje):
    lenght = len(mensaje)
    lista_mensaje = list(mensaje)
    dic_mensaje = {}
    for key in range(lenght):
        dic_mensaje[key] = lista_mensaje[key]
    return dic_mensaje

def encriptar(diccionario):
    lista_mezclada = []
    lista = range(len(diccionario))
    lista_desordenada = random.sample(lista,len(lista))
    for key in lista_desordenada:
        lista_mezclada.append(diccionario[key])
    mensaje_encriptado = "".join(lista_mezclada)
    return mensaje_encriptado


if __name__ == "__main__":
    main()
