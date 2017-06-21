import random

NOMBRES = [
    'Ana',
    'Pedro',
    'Pablo',
    'Ernesto',
    'Ariel',
    'Carlos',
    'Luis',
    'Oscar',
    'Alicia',
    'Maria',
    'Brenda'
]

CIUDADES = [
    'Managua',
    'Masaya',
    'Matagalpa',
    'Chinandega',
    'Somoto',
    'Rivas'
]

def generar_diccionario_estudiantes():
    estudiantes = {}

    for nombre in NOMBRES:
        estudiantes= {
            
            'C De edad': random.randrange(16, 30),
            'A El nombre del estudiante es': random.choice(NOMBRES),
            'D y cursa el anio': random.randrange(1, 5),
            'B es de la cuidad': random.choice(CIUDADES)
        }
        return estudiantes

print generar_diccionario_estudiantes()