def asignar_beneficios(antiguedad):
    """
    Asigna beneficios según la antigüedad.
    :param antiguedad: años de antigüedad del empleado
    :return: lista de beneficios
    """
    beneficios = []
    if antiguedad > 3:
        beneficios.append("Bono anual")
    if antiguedad > 5:
        beneficios.append("Días adicionales de vacaciones")
    if not beneficios:
        beneficios.append("Sin beneficios adicionales")
    return beneficios