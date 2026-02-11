def leer_entero(prompt):
    while True:
        try:
            valor = input(prompt)
            cantidad = int(valor)
            return cantidad
        except ValueError:
            print("Error: debe ingresar un número entero. Intente nuevamente.")

def main():
    print("Librería Hogwarts - Gestión de inventario")
    while True:
        existencia = leer_entero("Ingrese la cantidad actual de libros en existencia: ")
        vendidos = leer_entero("Ingrese la cantidad de libros vendidos durante el día: ")

        if existencia < 0 or vendidos < 0:
            print("Error: las cantidades no pueden ser negativas. Vuelva a ingresar los valores.")
            continue

        if vendidos > existencia:
            print("Error: la cantidad vendida no puede exceder la cantidad en inventario. Vuelva a ingresar los valores.")
            continue

        disponibles = existencia - vendidos
        print("Datos válidos.")
        print(f"Libros disponibles después de las ventas: {disponibles}")
        break

if __name__ == "__main__":
    main()