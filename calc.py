class Bateria:
    def __init__(self, nombre, voltaje, capacidad, peso, dimensiones):
        self.nombre = nombre
        self.voltaje = voltaje  # Voltios (V)
        self.capacidad = capacidad  # Capacidad en kWh
        self.peso = peso  # Peso en kg
        self.dimensiones = dimensiones  # Dimensiones en mm (largo, ancho, alto)

# Lista de baterías reutilizadas de coches eléctricos con datos actualizados
baterias = [
    Bateria("Tesla Model S", 400, 85, 540, (2100, 1500, 100)),  # Datos aproximados
    Bateria("Nissan Leaf", 360, 24, 294, (1575, 1100, 300)),  # Datos aproximados
    Bateria("Chevy Bolt", 350, 60, 430, (1600, 1100, 300)),  # Datos aproximados
    Bateria("BMW i3", 360, 33, 278, (1400, 1000, 250)),  # Datos aproximados
]

# Mostrar opciones de batería
print("Seleccione el tipo de batería:")
for i, bateria in enumerate(baterias):
    print(f"{i + 1}. {bateria.nombre} - Voltaje: {bateria.voltaje}V, Capacidad: {bateria.capacidad}kWh, Peso: {bateria.peso}kg, Dimensiones: {bateria.dimensiones}mm")

# Solicitar al usuario la selección y cantidad
opcion = int(input("Ingrese el número de la batería deseada: ")) - 1
cantidad = int(input("Ingrese la cantidad de baterías: "))

# Calcular peso total y dimensiones del sistema
bateria_seleccionada = baterias[opcion]
peso_total = bateria_seleccionada.peso * cantidad
capacidad_total = bateria_seleccionada.capacidad * cantidad
dimensiones_totales = (
    bateria_seleccionada.dimensiones[0] * cantidad,
    bateria_seleccionada.dimensiones[1],
    bateria_seleccionada.dimensiones[2]
)

# Mostrar resultados
print("\n--- Características del sistema de almacenamiento ---")
print(f"Tipo de batería: {bateria_seleccionada.nombre}")
print(f"Cantidad: {cantidad}")
print(f"Voltaje por batería: {bateria_seleccionada.voltaje}V")
print(f"Capacidad por batería: {bateria_seleccionada.capacidad}kWh")
print(f"Capacidad total del sistema: {capacidad_total}KWh")
print(f"Peso total del sistema: {peso_total}kg")
print(f"Dimensiones totales del sistema (LxAxH): {dimensiones_totales[0]}mm x {dimensiones_totales[1]}mm x {dimensiones_totales[2]}mm")
