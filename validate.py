def validador(alternativas, opcion):
    while opcion not in alternativas:
        opcion = input("La opción ingresada no es válida. Por favor, escriba una preferencia válida: ")
    return opcion


if __name__ == '__main__':
    alternativas = ['1', '2', '3']
    opcion = input("Escoja una alternativa: ")

    validador(alternativas, opcion)