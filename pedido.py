from te import Te

sabor = int(input("Ingrese el sabor del té (1: Té negro, 2: Té verde, 3: Agua de hierbas): "))
formato = int(input("Ingrese el formato del té (1: Formato pequeño, 2: Formato mediano, 3: Formato grande): "))

tiempo, recomendacion = Te.tiempo_preparacion_y_recomendacion(sabor)
precio = Te.precio_por_formato(formato)

if sabor == 1:
    nombre_sabor = "Té negro"
elif sabor == 2:
    nombre_sabor = "Té verde"
elif sabor == 3:
    nombre_sabor = "Agua de hierbas"
else:
    nombre_sabor = "Desconocido"

print("\n--- Detalle del Pedido ---")
print(f"Sabor del tipo de té: {nombre_sabor}")
print(f"Formato: {formato}")
print(f"Precio: ${precio}")
print(f"Tiempo de preparación: {tiempo} minutos")
print(f"Recomendación: {recomendacion}")
