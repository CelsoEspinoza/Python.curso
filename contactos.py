

class Contacto:

    def __init__(self, name, phone, email):
        self._name = name
        self._phone = phone
        self._email = email


class Agenda:
    def __init__(self):
        self._contacto = []

    def add(self, name, phone, email):
        contacto = Contacto(name, phone, email)
        self._contacto.append(contacto)

    def show_contact(self):
        for obj in self._contacto:
            self._print_contacto(obj)

    def _print_contacto(self, contacto):
        print("Nombre: {}".format(contacto._name))
        print("Teléfono: {}".format(contacto._phone))
        print("Email: {}".format(contacto._email))
        print("----------------------------------")

    def show_contact_idx(self):
        for obj in self._contacto:
            index = self._contacto.index(obj) + 1
            print("{} ---- {}".format(index, obj._name))

    def delete_contact_selected(self, num):
        idx = num - 1
        self._contacto.remove(self._contacto[idx])

    def modify_contact(self, num):
        idx = num-1
        name = input("Nombre a modificar: ")
        phone = input("Teléfono a modificar: ")
        email = input("Email a modificar: ")
        self._contacto[idx]._name = name
        self._contacto[idx]._phone = phone
        self._contacto[idx]._email = email



def run():
    agenda = Agenda()

    while True:
        command = input('''
        ¿Qué desea hacer?
        [a]gregar contacto
        [e]liminar contacto
        [m]odificar contacto
        [l]istar contactos
        [s]alir

        ''')

        if command.lower() == 'a':
            name = input("Escribe el nombre del contacto: ")
            phone = input("Escribe el teléfono del contacto: ")
            email = input("Escribe el email del contacto: ")
            agenda.add(name, phone, email)

        elif command.lower() == 'e':
            try:
                agenda.show_contact_idx()
                print("Escriba el número de la persona a la cual desea eliminar")
                num = int(input())
                agenda.delete_contact_selected(num)
            except IndexError:
                print("Elige un número correcto")

        elif command.lower() == 'm':
            print("¿A quién modificará?")
            agenda.show_contact_idx()
            num = int(input())
            agenda.modify_contact(num)

        elif command.lower() == 'l':
            agenda.show_contact()

        else:
            break




if __name__ == "__main__":
    run()
