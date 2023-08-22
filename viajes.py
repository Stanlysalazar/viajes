destinos_precios = {
    "Guajira": {"adultos": 1450000, "niños": 870000},
    "Cañón del Chicamocha": {"adultos": 1600000, "niños": 960000},
    "Llanos Orientales": {"adultos": 1200000, "niños": 720000}
}

total_personas_guajira = 0
total_personas_canon_chicamocha = 0
total_personas_llanos_orientales = 0
total_dinero_guajira = 0
total_dinero_canon_chicamocha = 0
total_dinero_llanos_orientales = 0
total_personas_adultas = 0
total_niños = 0
total_dinero_total = 0

while True:
    nombre_cliente = input("Nombre del cliente (o 'fin' para terminar): ")
    if nombre_cliente.lower() == "fin":
        break
    
    destino = input("Nombre del destino: ")
    adultos = int(input("Número de personas adultas: "))
    niños = int(input("Número de niños: "))
    
    subtotal = (destinos_precios[destino]["adultos"] * adultos) + (destinos_precios[destino]["niños"] * niños)
    
    print("\nNombre Cliente:", nombre_cliente)
    print("Nombre del destino:", destino)
    print("Nro Personas Adultas:", adultos)
    print("Nro Niños:", niños)
    print("Subtotal:", subtotal, "\n")
    
    if destino == "Guajira":
        total_personas_guajira += adultos + niños
        total_dinero_guajira += subtotal
    elif destino == "Cañón del Chicamocha":
        total_personas_canon_chicamocha += adultos + niños
        total_dinero_canon_chicamocha += subtotal
    elif destino == "Llanos Orientales":
        total_personas_llanos_orientales += adultos + niños
        total_dinero_llanos_orientales += subtotal
        
    total_personas_adultas += adultos
    total_niños += niños
    total_dinero_total += subtotal

print("Cantidad de personas que viajan para la Guajira:", total_personas_guajira)
print("Cantidad de personas que viajan para Cañón del Chicamocha:", total_personas_canon_chicamocha)
print("Cantidad de personas que viajan para los llanos orientales:", total_personas_llanos_orientales)
print("Total de dinero de los viajes para la Guajira:", total_dinero_guajira)
print("Total de dinero de los viajes para Cañón del Chicamocha:", total_dinero_canon_chicamocha)
print("Total de dinero de los viajes para los llanos orientales:", total_dinero_llanos_orientales)
print("Total de personas Adultas:", total_personas_adultas)
print("Total de niños:", total_niños)
print("Total de dinero de todos los destinos:", total_dinero_total)
