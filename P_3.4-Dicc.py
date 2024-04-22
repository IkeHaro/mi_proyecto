# Creamos un diccionario vacío para almacenar la información de las personas
personas = {}

# Pedimos al usuario que ingrese nombres e identificaciones hasta que decida terminar
while True:
    nombre = input("Ingresa el nombre de la persona (o escribe 'fin' para terminar): ")
    if nombre.lower() == 'fin':
        break
    identificacion = input("Ingresa la identificación de la persona: ")
    personas[nombre] = identificacion

# Mostramos la información almacenada
print("Información de personas ingresadas:")
for nombre, identificacion in personas.items():
    print("Nombre:", nombre, "- Identificación:", identificacion)
