def is_palindrome(text):
    text = text.lower().replace(" ", "")
    inverted_text = text[::-1]
    return inverted_text == text


def main():
    palabra = input("Escribe el texto a evaluar: ")
    es_palindromo = is_palindrome(palabra)
    if es_palindromo:
        print("El texto \"{}\" es palíndromo".format(palabra))
    else:
        print("El texto \"{}\" NO es palíndromo".format(palabra))

    input("")

if __name__ == "__main__":
    main()
