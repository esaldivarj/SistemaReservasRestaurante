# Sistema de Gestión de Restaurante
## Gestión de Horarios y Disponibilidad de Mesas

### 📋 Descripción
Sistema desarrollado como proyecto final de la materia de Ingeniería de Software. Permite gestionar mesas, horarios de operación, disponibilidad en tiempo real y generar reportes estadísticos para restaurantes.

### 🎯 Funcionalidades
- ✅ Gestión de mesas (agregar, visualizar)
- ✅ Configuración de horarios de operación
- ✅ Control de disponibilidad en tiempo real
- ✅ Ocupación y liberación de mesas
- ✅ **NUEVO:** Reportes y estadísticas del restaurante
- ✅ Persistencia de datos en JSON

### 🛠️ Tecnologías
- **Lenguaje:** Python 3.13.5
- **Almacenamiento:** JSON
- **Metodología:** Ágil (Scrum)

### 🚀 Instalación y Uso

1. Clonar el repositorio:
```bash
git clone https://github.com/esaldivarj/SistemaReservasRestaurante.git
cd SistemaReservasRestaurante
```

2. Ejecutar el programa:
```bash
python3 main.py
```

### 📁 Estructura del Proyecto
```
SistemaReservasRestaurante/
├── main.py              # Menú principal
├── mesas.py            # Gestión de mesas
├── horarios.py         # Gestión de horarios
├── disponibilidad.py   # Control de disponibilidad
├── reportes.py         # Reportes y estadísticas (NUEVO)
└── datos.json          # Base de datos
```

### 📊 Módulo de Reportes (Nueva Funcionalidad)
El sistema ahora incluye un módulo de reportes que genera estadísticas en tiempo real:
- Total de mesas y estado (disponibles/ocupadas)
- Porcentajes de ocupación
- Capacidad total, disponible y ocupada
- Información de horarios configurados
- Fecha y hora de generación del reporte

### 👨‍💻 Autor
Eduardo Iván Saldívar Jaramillo (@esaldivarj)

### 📝 Proyecto Académico
Ingeniería de Software - 2025