from colegio import registro, antiguedad, beneficios

def mostrar_informacion_empleado(empleados, nombre):
    """
    Muestra en pantalla la información completa de un empleado.
    """
    salario = empleados[nombre]["salario"]
    fecha_ingreso = empleados[nombre]["fecha_ingreso"]
    antiguedad_empleado = antiguedad.calcular_antiguedad(fecha_ingreso)
    beneficios_empleado = beneficios.asignar_beneficios(antiguedad_empleado)

    print("\n--- Información del empleado ---")
    print(f"Nombre: {nombre}")
    print(f"Salario: ${salario}")
    print(f"Fecha de ingreso: {fecha_ingreso}")
    print(f"Antigüedad: {antiguedad_empleado} años")
    print("Beneficios asignados:", ", ".join(beneficios_empleado))
    print("--------------------------------\n")


def menu():
    empleados = {}
    while True:
        print("=== Sistema de Registro de Empleados ===")
        print("1. Agregar empleado")
        print("2. Mostrar información de un empleado")
        print("3. Listar todos los empleados")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del empleado: ")
            salario = float(input("Ingrese el salario: "))
            fecha_ingreso = input("Ingrese la fecha de ingreso (dd/mm/yyyy): ")
            registro.agregar_empleado(empleados, nombre, salario, fecha_ingreso)
            print(f"Empleado {nombre} agregado correctamente.\n")

        elif opcion == "2":
            nombre = input("Ingrese el nombre del empleado: ")
            if nombre in empleados:
                mostrar_informacion_empleado(empleados, nombre)
            else:
                print("Empleado no encontrado.\n")

        elif opcion == "3":
            if empleados:
                print("\nLista de empleados registrados:")
                for nombre in empleados.keys():
                    print("-", nombre)
                print()
            else:
                print("No hay empleados registrados.\n")

        elif opcion == "4":
            print("Saliendo del sistema... ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intente nuevamente.\n")


if __name__ == "__main__":
    menu()