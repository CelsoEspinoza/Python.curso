
#Algoritmo para hallar cualquier valor de la ecuación formada por la regresión
#lineal.

def main():
    contador = 0
    listax = []
    listay = []
    agrega_valores(listax, listay, contador)
    b = pendiente(listax,listay)
    a = valor_a(listax,listay, b)
    R2 = valor_R2(listax,listay)
    print("El valor del R2 es {}".format(R2))
    pronostico_lineal(a,b)


def agrega_valores(listax, listay, contador):
    print("Para dejar de agregar valores, escribir en X: -99.99")
    while True:
        contador += 1
        x = float(input("Agrega la abscisa número {} : ".format(contador)))
        if x == -99.99:
            break
        y = float(input("Agrega la ordenada número {} : ".format(contador)))
        listax.append(x)
        listay.append(y)

def pendiente(listax, listay):
    sumax = 0
    sumay = 0
    suma_qx = 0
    sum_productoxy = 0
    n = len(listax)
    for i in range(n):
        sumax += listax[i-1]
        sumay += listay[i-1]
        suma_qx += listax[i-1]**2
        sum_productoxy += listax[i-1] * listay[i-1]
    b = float(((n*sum_productoxy)-(sumax*sumay))/((n*suma_qx) - sumax**2))
    return b


def valor_a(listax, listay, b):
    sumax = 0
    sumay = 0
    n = len(listax)
    for i in range(n):
        sumax += listax[i-1]
        sumay += listay[i-1]
    a = float((sumay - (b*sumax))/(n))
    return a

def valor_R2(listax,listay):
    sumax = 0
    sumay = 0
    suma_qx = 0
    suma_qy = 0
    sum_productoxy = 0
    n = len(listax)
    for i in range(n):
        sumax += listax[i-1]
        sumay += listay[i-1]
        suma_qx += listax[i-1]**2
        suma_qy += listay[i-1]**2
        sum_productoxy += listax[i-1] * listay[i-1]
    R2 = float((n*sum_productoxy-sumax*sumay)**2/((n*suma_qx-sumax**2)*(n*suma_qy-sumay**2)))
    return R2


def pronostico_lineal(a, b):
    while True:
        x_y = float(input("Elije qué deseas obtener de la regresión: X=0 o Y=1:  "))
        print("Escribe 9 para salir")
        if x_y == 0:
            y = float(input("Escribe el valor de la ordenada(Y): "))
            if b != 0:
                res_x = (y-a)/b
                print("El valor es {}".format(res_x))

        elif x_y == 1:
            x = float(input("Escribe el valor de la abscisa(X): "))
            res_y = a + b*x
            print("El valor es {}".format(res_y))

        elif x_y == 9:
            break
        else:
            print("")
            print("Debes escribir (0 para X) o (1 para Y)")


if __name__ == "__main__":
    main()
