def calcular_descuento(cantidad, precio_unitario=40.0):
    """
    Devuelve tupla: (porcentaje_descuento, precio_unitario_con_descuento, total_sin_descuento, total_con_descuento, ahorro)
    """
    if cantidad >= 20:
        pct = 0.25
    elif cantidad >= 10:
        pct = 0.15
    else:
        pct = 0.0

    precio_desc = precio_unitario * (1 - pct)
    total_sin = precio_unitario * cantidad
    total_con = precio_desc * cantidad
    ahorro = total_sin - total_con
    return pct, round(precio_desc, 2), round(total_sin, 2), round(total_con, 2), round(ahorro, 2)


def area_lateral_cilindro(radio, altura, pi=3.1416):
    """
    Calcula y devuelve el área lateral del cilindro usando la fórmula:
    arealc = 2 * pi * radio * altura
    """
    return 2 * pi * radio * altura


def leer_entero(prompt, minimo=None):
    while True:
        try:
            v = int(input(prompt))
            if minimo is not None and v < minimo:
                print(f"Error: el valor debe ser >= {minimo}. Intente nuevamente.")
                continue
            return v
        except ValueError:
            print("Entrada inválida: ingrese un número entero.")


def leer_flotante(prompt, minimo=None):
    while True:
        try:
            v = float(input(prompt))
            if minimo is not None and v < minimo:
                print(f"Error: el valor debe ser >= {minimo}. Intente nuevamente.")
                continue
            return v
        except ValueError:
            print("Entrada inválida: ingrese un número (puede usar decimales).")


def mostrar_menu():
    print("\n--- Menú de la tienda ---")
    print("1. Calcular descuento por compra mayorista")
    print("2. Calcular área lateral de un cilindro")
    print("3. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1, 2 o 3): ").strip()
        if opcion not in ("1", "2", "3"):
            print("Opción inválida. Debe ingresar 1, 2 o 3.")
            continue

        if opcion == "1":
            cantidad = leer_entero("Ingrese la cantidad de unidades del mismo artículo (entero >= 1): ", minimo=1)
            pct, precio_desc, total_sin, total_con, ahorro = calcular_descuento(cantidad)
            pct_por = int(pct * 100)
            print(f"\nResultado del descuento:")
            print(f"- Precio base por prenda: $40.00")
            print(f"- Descuento aplicado: {pct_por}%")
            print(f"- Precio por prenda con descuento: ${precio_desc:.2f}")
            print(f"- Total sin descuento: ${total_sin:.2f}")
            print(f"- Total con descuento: ${total_con:.2f}")
            print(f"- Ahorro total: ${ahorro:.2f}")

        elif opcion == "2":
            radio = leer_flotante("Ingrese el radio de la base (ej. 2.5): ", minimo=0.0)
            altura = leer_flotante("Ingrese la altura del cilindro (ej. 5.0): ", minimo=0.0)
            area = area_lateral_cilindro(radio, altura)
            print(f"\nÁrea lateral del cilindro: {area:.4f} unidades cuadradas (usando pi = 3.1416)")

        else:  # opcion == "3"
            print("Saliendo del programa. ¡Hasta luego!")
            break


if __name__ == "__main__":
    main()