#se crea un diccionario  de datos para promediar las calificaciones de los alumnos
# el nombre del alumno es empleado como clave, mientras que todas las calificaciones asociadas 
# son almacenadas en una tupla (la tupla puede ser el valor de un diccionario, esto no es un problema)
grupo = {}

#se ingresa a un bucle "infinito" se incluye el exit para salir del bucle
while True:
    nombre = input("Ingresa el nombre del estudiante (o exit para detenerse): ")
    if nombre == 'exit':
        break
    
    calif = int(input("Ingresa la calificación del alumno (0-10): "))
# si el nombre del estudiante ya se encuentra en el diccionario solo se actualiza, 
# se alarga la tupla asociada con la nueva calificación (observa el operador +=)
# si el nombre no existe en el diccionario se agrega como una entrada nueva con un nuevo valor  
    if nombre in grupo:
        grupo[nombre] += (calif,)
    else:
        grupo[nombre] = (calif,)
#Se itera a través de la tupla, tomado todas las calificaciones subsecuentes 
# y actualizando la suma junto con el contador      
for nombre in sorted(grupo.keys()):
    sum = 0
    contador = 0
    for calif in grupo[nombre]:
        sum += calif
        contador += 1
    print(nombre, ":", sum / contador)
