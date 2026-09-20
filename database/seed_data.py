from database.connection import get_connection

EXERCISES_BASE = [
    ("Press Banca", "Pecho"),
    ("Sentadilla", "Piernas"),
    ("Peso Muerto", "Espalda"),
    ("Press Militar", "Hombros"),
    ("Remo con Barra", "Espalda"),
    ("Curl de Bíceps", "Bíceps"),
    ("Extensiones de Tríceps", "Tríceps"),
    ("Leg Press", "Piernas"),
    ("Jalón al Pecho", "Espalda"),
    ("Elevaciones Laterales", "Hombros"),
    ("Fondos en Paralelas", "Pecho"),
    ("Curl de Piernas", "Piernas"),
    ("Press de Hombros con Mancuernas", "Hombros"),
    ("Remo con Mancuernas", "Espalda"),
    ("Curl de Bíceps con Mancuernas", "Bíceps"),
    ("Extensiones de Tríceps con Mancuernas", "Tríceps"),
    ("Sentadilla Frontal", "Piernas"),
    ("Press de Banca Inclinado", "Pecho"),
    ("Jalón Trasnuca", "Espalda"),
    ("Elevaciones Frontales", "Hombros"),
    ("Curl de Bíceps con Barra", "Bíceps"),
    ("Extensiones de Tríceps en Polea", "Tríceps"),
    ("Peso Muerto Rumano", "Espalda"),
    ("Press de Hombros con Barra", "Hombros"),
    ("Remo en Polea Baja", "Espalda"),
    ("Curl de Bíceps en Polea", "Bíceps"),
    ("Extensiones de Tríceps en Polea Alta", "Tríceps"),
    ("Sentadilla Hack", "Piernas"),
    ("Press de Banca Declinado", "Pecho"),
    ("Jalón al Pecho con Agarre Cerrado", "Espalda"),
    ("Elevaciones Laterales con Mancuernas", "Hombros"),
    ("Curl de Bíceps Concentrado", "Bíceps"),
    ("Extensiones de Tríceps con Cuerda", "Tríceps"),
    ("Peso Muerto Sumo", "Espalda"),
    ("Press de Hombros con Mancuernas Alterno", "Hombros"),
    ("Remo con Mancuernas Alternas", "Espalda"),
    ("Curl de Bíceps con Mancuernas Alternas", "Bíceps"),
    ("Extensiones de Tríceps con Mancuernas Alternas", "Tríceps"),
    ("Sentadilla Búlgara", "Piernas"),
    ("Press de Banca con Mancuernas", "Pecho"),
    ("Jalón al Pecho con Agarre Amplio", "Espalda"),
    ("Elevaciones Laterales con Polea", "Hombros"),
    ("Curl de Bíceps en Banco Scott", "Bíceps"),
    ("Extensiones de Tríceps en Banco Plano", "Tríceps"),
    ("Peso Muerto con Mancuernas", "Espalda"),
    ("Press de Hombros con Barra", "Hombros"),
]

def seed_exercises():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM exercises")
    count = cursor.fetchone()[0]
    
    if count == 0:
        cursor.executemany("INSERT INTO exercises (name, muscle_group) VALUES (?, ?)", EXERCISES_BASE)
        conn.commit()
        print(f"Insertados {len(EXERCISES_BASE)} ejercicios en la base de datos.")
    else:
        print(f"Ya existen {count} ejercicios en la base de datos.")
    
    cursor.close()
    conn.close()
    
    
