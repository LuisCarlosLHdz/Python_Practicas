message = "------Python Course------" #Variable String -> texto
print(message)
university = "Benemérita Universidad\nAutónoma de Puebla\n" #Nueva línea o punto y aparte
print(university)
university = "\"Benemérita Universidad Autónoma de Puebla\"\n" #Indicar dobles comillas como texto
print(university)
name = "Luis Carlos"
print(name + " is cool") #Concatenar Strings
print(name.lower()) #Imprimir en minúsculas
print(name.upper()) #Imprimir en mayúsculas
print(name.isupper()) #Hace una pregunta si el texto es en mayusculas y responde en boolean
print(name.upper().isupper()) #Pasa el texto en Mayusculas y pregunta si esta en mayusculas; Responde en boolean
print(len(name)) #Longitud de la variable name
print(name[0]) #Character específico en la posición cero 0
print(name[5:]) #Characters desde la posición 6 para adelante
print(name[0:4]) #Characters desde la posición 0 hasta la posición 4
print(name.index("u")) #Posición o index del character "u"
print(name.index("Carlos")) #Posición o index inicial de los characters "Carlos"
print(name.replace("Luis","Supper")) #Reemplazar un conjunto de characters por "Supper"
print("Puedes buscar en Google las funciones que puedes usar en Python con variables String")