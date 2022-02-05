def validador(alternativas: list, opcion: str):
    """
    alternativas: estructura de datos con opciones consideradas válidas.
    opcion: la alternativa a evaluar si está dentro de "alternativas".\n
    Si el valor de "opcion" no está en "alternativas", solicita que sea ingresado uno nuevo.
    La evaluación continúa hasta que se ingresa un valor de "opcion" válida.\n
    Retorna el valor de "opción".
    """
    while opcion not in alternativas:
        opcion = input("La opción ingresada no es válida. Por favor, escriba una preferencia válida: ")
    return opcion


if __name__ == '__main__':
    alternativas = ['1', '2', '3']
    opcion = input("Escoja una alternativa: ")

    validador(alternativas, opcion)