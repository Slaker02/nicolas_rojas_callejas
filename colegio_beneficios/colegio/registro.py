def agregar_empleado(empleados, nombre, salario, fecha_ingreso):
    """
    Agrega un nuevo empleado al diccionario.
    :param empleados: diccionario general de empleados
    :param nombre: nombre del empleado
    :param salario: salario del empleado
    :param fecha_ingreso: fecha de ingreso en formato dd/mm/yyyy
    """
    empleados[nombre] = {
        "salario": salario,
        "fecha_ingreso": fecha_ingreso
    }
    return empleados