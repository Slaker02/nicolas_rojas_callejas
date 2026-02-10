from datetime import datetime

def calcular_antiguedad(fecha_ingreso):
    """
    Calcula la antigüedad en años a partir de la fecha de ingreso.
    :param fecha_ingreso: fecha en formato dd/mm/yyyy
    :return: antigüedad en años (int)
    """
    fecha_actual = datetime.now()
    fecha_ingreso_dt = datetime.strptime(fecha_ingreso, "%d/%m/%Y")
    antiguedad = fecha_actual.year - fecha_ingreso_dt.year

    # Ajuste si aún no cumple aniversario este año
    if (fecha_actual.month, fecha_actual.day) < (fecha_ingreso_dt.month, fecha_ingreso_dt.day):
        antiguedad -= 1
    return antiguedad