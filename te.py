class Te:
    kind = 'Infusion'

    @staticmethod
    def tiempo_preparacion_y_recomendacion(sabor):
        if sabor == 1:
            return 5, "Té negro: Dejar reposar 5 minutos antes de beber."
        elif sabor == 2:
            return 3, "Té verde: Dejar reposar 3 minutos para obtener mejor sabor."
        elif sabor == 3:
            return 4, "Agua de hierbas: Reposar 4 minutos para un sabor óptimo."
        else:
            return 0, "Sabor no reconocido."

    @staticmethod
    def precio_por_formato(formato):
        if formato == 1:
            return 1000
        elif formato == 2:
            return 1500
        elif formato == 3:
            return 2000
        else:
            return 0


if __name__ == "__main__":
    tiempo, recomendacion = Te.tiempo_preparacion_y_recomendacion(1)
    print(f"Tiempo de preparación: {tiempo} minutos.")
    print(recomendacion)

    precio = Te.precio_por_formato(2)
    print(f"Precio: ${precio}")
