import turtle

def main():
    window = turtle.Screen()
    figura = turtle.Turtle()

    hacer_figura(figura)

    turtle.mainloop()

def hacer_figura(fig):
    lados = int(input("Colocar la cantidad de lados: "))
    lenght = int(input("Colocar la longitud: "))
    angulo = 180 - (180 * (lados-2)) / lados
    for i in range(lados):
        dibujar_lineas_y_girar(fig, lenght, angulo)

def dibujar_lineas_y_girar(fig, lenght, angulo):
    fig.forward(lenght)
    fig.left(angulo)


if __name__ == "__main__":
  main()
