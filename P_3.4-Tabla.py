# Creamos una lista vacía para almacenar la información de las personas
personas = []

# Pedimos al usuario que ingrese nombres e identificaciones hasta que decida terminar
while True:
    nombre = input("Ingresa el nombre de la persona (o escribe 'fin' para terminar): ")
    if nombre.lower() == 'fin':
        break
    identificacion = input("Ingresa la identificación de la persona: ")
    personas.append([nombre, identificacion])

# Mostramos la información almacenada
print("Información de personas ingresadas:")
for persona in personas:
    print("Nombre:", persona[0], "- Identificación:", persona[1])
