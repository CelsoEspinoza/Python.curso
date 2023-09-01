import turtle

def main():
    window = turtle.Screen()
    celso = turtle.Turtle()

    make_square(celso)

    turtle.mainloop()

def make_square(cels):
    lenght = int(input("Tamaño del cuadrado: "))

    for i in range(4):
        make_line_and_turn(cels, lenght)

def make_line_and_turn(cel, lenght):
    cel.forward(lenght)
    cel.left(90)


if __name__ == "__main__":
    main()
