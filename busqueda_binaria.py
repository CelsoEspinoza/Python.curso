
import random

def main():
    num_find = int(input("Ingresa un numero: "))
    lista_random = lista_random_ordenada()
    cond = False
    result = busqueda_binaria(num_find, lista_random, 0, len(lista_random)-1)
    if result is True:
        print("Sí está el número")
    else:
        print("NO está el número")

def lista_random_ordenada():
    list_random = []
    cantidad = random.randint(1,99)
    for i in range(cantidad):
        num = random.randint(1,99)
        list_random.append(num)
    lista_ordenada = sorted(list_random)
    return lista_ordenada

def busqueda_binaria(num_find, lista, low, high):
    if low > high:
        return False
    mid = int((low + high)/2)
    if lista[mid] == num_find:
        return True
    elif lista[mid] > num_find:
        return busqueda_binaria(num_find, lista, low, mid-1)
    else:
        return busqueda_binaria(num_find, lista, mid+1, high)


if __name__ == "__main__":
    main()
