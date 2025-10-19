import json

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

def agregar_mesa():
    """Permite agregar una nueva mesa"""
    datos = cargar_datos()
    
    print("\n=== AGREGAR NUEVA MESA ===")
    numero_mesa = input("Número de mesa: ")
    capacidad = input("Capacidad (número de personas): ")
    
    # Crear la mesa
    mesa = {
        "numero": numero_mesa,
        "capacidad": int(capacidad),
        "estado": "disponible"
    }
    
    # Agregar a la lista
    datos["mesas"].append(mesa)
    guardar_datos(datos)
    
    print(f"✓ Mesa {numero_mesa} agregada exitosamente")

def ver_mesas():
    """Muestra todas las mesas registradas"""
    datos = cargar_datos()
    
    print("\n=== MESAS REGISTRADAS ===")
    if len(datos["mesas"]) == 0:
        print("No hay mesas registradas aún.")
    else:
        for mesa in datos["mesas"]:
            print(f"Mesa {mesa['numero']} - Capacidad: {mesa['capacidad']} personas - Estado: {mesa['estado']}")

def menu_mesas():
    """Menú principal de gestión de mesas"""
    while True:
        print("\n--- GESTIÓN DE MESAS ---")
        print("1. Agregar mesa")
        print("2. Ver mesas")
        print("3. Volver al menú principal")
        
        opcion = input("\nSelecciona una opción: ")
        
        if opcion == "1":
            agregar_mesa()
        elif opcion == "2":
            ver_mesas()
        elif opcion == "3":
            break
        else:
            print("Opción inválida")