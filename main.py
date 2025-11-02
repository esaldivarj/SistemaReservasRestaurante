import mesas
import horarios
import disponibilidad
import reportes

def mostrar_menu_principal():
    """Muestra el menú principal del sistema"""
    print("\n" + "="*50)
    print("  SISTEMA DE GESTIÓN DE RESTAURANTE")
    print("  Horarios y Disponibilidad de Mesas")
    print("="*50)
    print("\n1. Gestión de Mesas")
    print("2. Gestión de Horarios")
    print("3. Gestión de Disponibilidad")
    print("4. Reportes y Estadísticas")
    print("5. Salir")
    print("-"*50)

def main():
    """Función principal del programa"""
    print("\n¡Bienvenido al Sistema de Gestión de Restaurante!")
    
    while True:
        mostrar_menu_principal()
        opcion = input("\nSelecciona una opción (1-5): ")
        
        if opcion == "1":
            mesas.menu_mesas()
        elif opcion == "2":
            horarios.menu_horarios()
        elif opcion == "3":
            disponibilidad.menu_disponibilidad()
        elif opcion == "4":
            reportes.menu_reportes()
        elif opcion == "5":
            print("\n¡Gracias por usar el sistema! Hasta pronto.")
            break
        else:
            print("\n✗ Opción inválida. Por favor selecciona un número del 1 al 5.")

if __name__ == "__main__":
    main()