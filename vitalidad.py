# Programa de facturación para la frutería "Vitalidad"

# Entrada de datos
kilos = float(input("Ingrese la cantidad de kilos de mandarinas: "))
precio_por_kilo = float(input("Ingrese el precio por kilo: "))

# Determinar el descuento según la tabla
if kilos <= 2:
    descuento = 0.10
elif kilos <= 5:
    descuento = 0.20
elif kilos <= 10:
    descuento = 0.30
else:
    descuento = 0.40

# Calcular monto total
subtotal = kilos * precio_por_kilo
monto_descuento = subtotal * descuento
total = subtotal - monto_descuento

# Salida de resultados
print("\n--- FACTURA ---")
print(f"Kilos comprados: {kilos}")
print(f"Precio por kilo: ${precio_por_kilo:.2f}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Descuento aplicado: {descuento*100:.0f}%")
print(f"Monto de descuento: ${monto_descuento:.2f}")
print(f"TOTAL A PAGAR: ${total:.2f}")
