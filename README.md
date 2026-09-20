# Plo

App móvil para registrar entrenamientos de gimnasio de forma rápida y sencilla.

## El problema

Anotar pesos y series en el celular mientras entrenás es tedioso. Las plantillas de Excel son incómodas y las apps existentes son demasiado complejas.

## La solución

Plo es un anotador rápido y offline-first para que puedas registrar tus entrenamientos sin fricciones.

## Features (Fase 1)

- Registro rápido de series (peso + reps)
- Lista de ejercicios base + personalizados
- Historial de entrenamientos por día
- Funciona sin internet
- Notas libres por serie

## Stack

- **Frontend**: Flet (Python)
- **DB**: SQLite (local)
- **Backend**: FastAPI (futuro - para conexión profesor/alumno)

## Desarrollo

```bash
# Crear entorno virtual
python -m venv venv

# Activar (Windows)
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar
python main.py
```

## License

MIT
