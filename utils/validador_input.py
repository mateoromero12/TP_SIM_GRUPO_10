def pedir_float(
    mensaje: str,
    condicion=lambda x: True,
    mensaje_error: str = "Valor inválido."
) -> float:
    """
    Solicita al usuario un número flotante por consola, validando la entrada.

    Args:
        mensaje (str): Mensaje a mostrar al usuario.
        condicion (callable, optional): Función que recibe el valor y retorna True si es válido.
        mensaje_error (str, optional): Mensaje a mostrar si la condición no se cumple.

    Returns:
        float: Valor flotante ingresado por el usuario y que cumple la condición.
    """
    while True:
        entrada = input(mensaje)
        try:
            valor = float(entrada)
            if entrada.strip().lower() in ("true", "false") or entrada.strip() == "":
                print("Por favor, ingresa un número válido.")
                continue
            if condicion(valor):
                return valor
            else:
                print(mensaje_error)
        except ValueError:
            print("Por favor, ingresa un número válido.")


def pedir_int(
    mensaje: str,
    condicion=lambda x: True,
    mensaje_error: str = "Valor inválido."
) -> int:
    """
    Solicita al usuario un número entero por consola, validando la entrada.

    Args:
        mensaje (str): Mensaje a mostrar al usuario.
        condicion (callable, optional): Función que recibe el valor y retorna True si es válido.
        mensaje_error (str, optional): Mensaje a mostrar si la condición no se cumple.

    Returns:
        int: Valor entero ingresado por el usuario y que cumple la condición.
    """
    while True:
        entrada = input(mensaje)
        try:
            if (
                entrada.strip().lower() in ("true", "false")
                or entrada.strip() == ""
                or "." in entrada
                or "e" in entrada.lower()
            ):
                print("Por favor, ingresa un número entero válido.")
                continue
            valor = int(entrada)
            if condicion(valor):
                return valor
            else:
                print(mensaje_error)
        except ValueError:
            print("Por favor, ingresa un número entero válido.")
