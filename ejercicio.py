Datos_Basico = {"Nombres": "juan Carlos",
                "Apellidos": "Perez Garcia",
                "Dui": "01025487-9",
                "Fecha_Nacimiento": "26/04/2006",
                "Lugar_Nacimiento0": "San Miguel",
                "Nacionalidad": "Salvadoreña",
                "Estado_Civil": "Complicado" 
            }

print("\nDetalle del diccionario")
print("============================")

print("\nClaves del diccionario: ",Datos_Basico.keys())
print("\nValores del diccionario: ",Datos_Basico.values())
print("\nElementos del diccionario: ",Datos_Basico.items())

print("\nInscripcion del curso")
print("============================")

print("\nDatos del participante")
print("============================")

print("Dui:",Datos_Basico["Dui"])
print("Nombre Completo: ",Datos_Basico["Nombres"]+" "+Datos_Basico["Apellidos"])


