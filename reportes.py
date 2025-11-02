import json
from datetime import datetime

def cargar_datos():
    """Carga los datos desde el archivo JSON"""
    try:
        with open('datos.json', 'r') as archivo:
            return json.load(archivo)
    except:
        return {"mesas": [], "horarios": {}, "ocupacion": []}

def generar_reporte():
    """Genera un reporte estadístico del restaurante"""
    datos = cargar_datos()
    
    print("\n" + "="*50)
    print("  REPORTE DE ESTADÍSTICAS DEL RESTAURANTE")
    print("="*50)
    
    # Estadísticas de mesas
    total_mesas = len(datos["mesas"])
    if total_mesas == 0:
        print("\n⚠ No hay mesas registradas en el sistema.")
        return
    
    mesas_disponibles = sum(1 for mesa in datos["mesas"] if mesa["estado"] == "disponible")
    mesas_ocupadas = total_mesas - mesas_disponibles
    capacidad_total = sum(mesa["capacidad"] for mesa in datos["mesas"])
    capacidad_disponible = sum(mesa["capacidad"] for mesa in datos["mesas"] if mesa["estado"] == "disponible")
    
    # Mostrar estadísticas
    print("\n📊 ESTADÍSTICAS DE MESAS:")
    print(f"   • Total de mesas: {total_mesas}")
    print(f"   • Mesas disponibles: {mesas_disponibles} ({mesas_disponibles/total_mesas*100:.1f}%)")
    print(f"   • Mesas ocupadas: {mesas_ocupadas} ({mesas_ocupadas/total_mesas*100:.1f}%)")
    
    print("\n👥 CAPACIDAD:")
    print(f"   • Capacidad total: {capacidad_total} personas")
    print(f"   • Capacidad disponible: {capacidad_disponible} personas")
    print(f"   • Capacidad ocupada: {capacidad_total - capacidad_disponible} personas")
    
    # Horarios
    horarios = datos.get("horarios", {})
    if horarios.get("hora_apertura"):
        print("\n🕐 HORARIOS:")
        print(f"   • Horario: {horarios['hora_apertura']} - {horarios['hora_cierre']}")
        print(f"   • Días: {len(horarios['dias_operacion'])} días/semana")
    
    print("\n" + "="*50)
    print(f"  Reporte generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*50)

def menu_reportes():
    """Menú de reportes"""
    while True:
        print("\n--- REPORTES Y ESTADÍSTICAS ---")
        print("1. Generar reporte")
        print("2. Volver al menú principal")
        
        opcion = input("\nSelecciona una opción: ")
        
        if opcion == "1":
            generar_reporte()
        elif opcion == "2":
            break
        else:
            print("Opción inválida")