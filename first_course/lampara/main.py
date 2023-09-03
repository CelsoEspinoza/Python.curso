
from lamp import Lamp

def main():
    lamp = Lamp(is_turned_on=False)
    while True:
        command = input('''
            ¿Qué deseas hacer?

            [p]render
            [a]pagar
            [s]alir
        ''')
        if command.upper() == 'P':
            lamp.turn_on()
        elif command.upper() == 'A':
            lamp.turn_off()
        else:
            break


if __name__ == "__main__":
    main()
