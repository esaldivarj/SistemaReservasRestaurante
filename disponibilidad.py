import json
from datetime import datetime

def cargar_datos():
    """Carga los datos desde el archivo JSON"""
    try:
        with open('datos.json', 'r') as archivo:
            return json.load(archivo)
    except:
        return {"mesas": [], "horarios": {}, "ocupacion": []}

def guardar_datos(datos):
    """Guarda los datos en el archivo JSON"""
    with open('datos.json', 'w') as archivo:
        json.dump(datos, archivo, indent=2)

def ver_disponibilidad():
    """Muestra la disponibilidad actual de todas las mesas"""
    datos = cargar_datos()
    
    print("\n=== DISPONIBILIDAD DE MESAS ===")
    
    if len(datos["mesas"]) == 0:
        print("No hay mesas registradas. Por favor, agrega mesas primero.")
        return
    
    mesas_disponibles = 0
    mesas_ocupadas = 0
    
    for mesa in datos["mesas"]:
        if mesa["estado"] == "disponible":
            print(f"✓ Mesa {mesa['numero']} - DISPONIBLE - Capacidad: {mesa['capacidad']} personas")
            mesas_disponibles += 1
        else:
            print(f"✗ Mesa {mesa['numero']} - OCUPADA - Capacidad: {mesa['capacidad']} personas")
            mesas_ocupadas += 1
    
    print(f"\nResumen: {mesas_disponibles} disponibles | {mesas_ocupadas} ocupadas")

def ocupar_mesa():
    """Marca una mesa como ocupada"""
    datos = cargar_datos()
    
    print("\n=== OCUPAR MESA ===")
    ver_disponibilidad()
    
    numero_mesa = input("\n¿Qué mesa deseas ocupar?: ")
    
    # Buscar la mesa
    for mesa in datos["mesas"]:
        if mesa["numero"] == numero_mesa:
            if mesa["estado"] == "ocupada":
                print(f"✗ La mesa {numero_mesa} ya está ocupada")
            else:
                mesa["estado"] = "ocupada"
                guardar_datos(datos)
                print(f"✓ Mesa {numero_mesa} marcada como OCUPADA")
            return
    
    print(f"✗ No se encontró la mesa {numero_mesa}")

def liberar_mesa():
    """Marca una mesa como disponible"""
    datos = cargar_datos()
    
    print("\n=== LIBERAR MESA ===")
    ver_disponibilidad()
    
    numero_mesa = input("\n¿Qué mesa deseas liberar?: ")
    
    # Buscar la mesa
    for mesa in datos["mesas"]:
        if mesa["numero"] == numero_mesa:
            if mesa["estado"] == "disponible":
                print(f"✗ La mesa {numero_mesa} ya está disponible")
            else:
                mesa["estado"] = "disponible"
                guardar_datos(datos)
                print(f"✓ Mesa {numero_mesa} marcada como DISPONIBLE")
            return
    
    print(f"✗ No se encontró la mesa {numero_mesa}")

def menu_disponibilidad():
    """Menú principal de gestión de disponibilidad"""
    while True:
        print("\n--- GESTIÓN DE DISPONIBILIDAD ---")
        print("1. Ver disponibilidad")
        print("2. Ocupar mesa")
        print("3. Liberar mesa")
        print("4. Volver al menú principal")
        
        opcion = input("\nSelecciona una opción: ")
        
        if opcion == "1":
            ver_disponibilidad()
        elif opcion == "2":
            ocupar_mesa()
        elif opcion == "3":
            liberar_mesa()
        elif opcion == "4":
            break
        else:
            print("Opción inválida")