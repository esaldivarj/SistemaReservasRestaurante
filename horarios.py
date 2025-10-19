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

def configurar_horarios():
    """Permite configurar los horarios de operación"""
    datos = cargar_datos()
    
    print("\n=== CONFIGURAR HORARIOS ===")
    hora_apertura = input("Hora de apertura (formato 24h, ej: 09:00): ")
    hora_cierre = input("Hora de cierre (formato 24h, ej: 22:00): ")
    
    print("\nDías de operación (escribe los números separados por comas)")
    print("1=Lunes, 2=Martes, 3=Miércoles, 4=Jueves, 5=Viernes, 6=Sábado, 7=Domingo")
    dias_input = input("Ejemplo: 1,2,3,4,5 para Lunes a Viernes: ")
    
    # Convertir a lista de números
    dias = [int(d.strip()) for d in dias_input.split(",")]
    
    # Nombres de días
    nombres_dias = {1: "Lunes", 2: "Martes", 3: "Miércoles", 4: "Jueves", 
                    5: "Viernes", 6: "Sábado", 7: "Domingo"}
    
    dias_nombres = [nombres_dias[d] for d in dias]
    
    # Guardar horarios
    datos["horarios"] = {
        "hora_apertura": hora_apertura,
        "hora_cierre": hora_cierre,
        "dias_operacion": dias_nombres
    }
    
    guardar_datos(datos)
    print("✓ Horarios configurados exitosamente")

def ver_horarios():
    """Muestra los horarios configurados"""
    datos = cargar_datos()
    
    print("\n=== HORARIOS DE OPERACIÓN ===")
    horarios = datos.get("horarios", {})
    
    if not horarios.get("hora_apertura"):
        print("No hay horarios configurados aún.")
    else:
        print(f"Horario: {horarios['hora_apertura']} - {horarios['hora_cierre']}")
        print(f"Días de operación: {', '.join(horarios['dias_operacion'])}")

def menu_horarios():
    """Menú principal de gestión de horarios"""
    while True:
        print("\n--- GESTIÓN DE HORARIOS ---")
        print("1. Configurar horarios")
        print("2. Ver horarios")
        print("3. Volver al menú principal")
        
        opcion = input("\nSelecciona una opción: ")
        
        if opcion == "1":
            configurar_horarios()
        elif opcion == "2":
            ver_horarios()
        elif opcion == "3":
            break
        else:
            print("Opción inválida")