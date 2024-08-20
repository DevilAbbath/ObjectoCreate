from te import Te

te1 = Te()
te2 = Te()

typeTe1 = type(te1)
typeTe2 = type(te2)

print(f"Tipo de te 1: {typeTe1}")
print(f"Tipo de te 2: {typeTe2}")

if typeTe1 == typeTe2:
    print("Ambos objetos son del mismo tipo")
else:
    print("Los objetos no son del mismo tipo")