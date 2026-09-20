# Plo

App móvil para registrar entrenamientos de gym de forma simple y rápida.

## El problema

Anotar pesos y series durante el entrenamiento es tedioso. Las plantillas 
de Excel son confusas y las apps existentes son demasiado complejas para 
usuarios sin experiencia técnica.

## La solución

Plo es un anotador offline-first diseñado para ser usado durante el 
entrenamiento. Interfaz simple, modo oscuro/claro, y sincronización 
futura con entrenadores.

## Features

### Fase 1 (Actual)
- Registro rápido de series (peso + reps)
- Lista de ejercicios base + personalizados
- Historial de entrenamientos por día
- Modo oscuro/claro con azul eléctrico
- Funciona sin internet

### Fase 2 (Futuro)
- Crear y exportar planes de entrenamiento
- Unirse a crews (gimnasios)
- Profesores asignan rutinas
- Sincronización online

## Stack

- **Frontend**: Flet 1.0+ (Python)
- **DB**: SQLite (local, offline-first)
- **Backend**: FastAPI (futuro - sync profesor/alumno)
- **Testing**: pytest

## Desarrollo

### Requisitos
- Python 3.13+
- pip

### Instalación
```bash
# Clonar repositorio
git clone https://github.com/MatBustos/Plo.git
cd Plo

# Crear entorno virtual
python -m venv venv

# Activar (Windows)
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar
python main.py
Estructura del Proyecto
Plo/
├── main.py              # Entry point
├── database/            # Conexión y modelos SQLite
├── screens/             # Pantallas de la app
└── components/          # Componentes reutilizables
