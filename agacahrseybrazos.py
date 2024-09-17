import time
from adafruit_servokit import ServoKit

# Inicializa el controlador de servos con 16 canales
kit = ServoKit(channels=16)

# Valores iniciales, máximos y mínimos para los servos
valores_iniciales = {
    0: 90, 
    1: 85, 
    2: 90, 
    3: 85, 
    4: 80, 
    5: 90,
    6: 95, 
    7: 90, 
    8: 90, 
    9: 90, 
    10: 100, 
    11: 90,
    12: 90, 
    13: 90, 
    14: 120, 
    15: 80
}

valores_maximos = {
    0: 170,
    1: 160,
    2: 150,
    3: 110,
    4: 140,
    5: 130,
    6: 140,
    7: 120,
    8: 90,
    9: 150,
    10: 175,
    11: 155,
    12: 140,
    13: 130,
    14: 180,
    15: 120
}

valores_minimos = {
    0: 90,
    1: 45,
    2: 25,
    3: 25,
    4: 30,
    5: 40,
    6: 40,
    7: 45,
    8: 25,
    9: 25,
    10: 25,
    11: 80,
    12: 30,
    13: 40,
    14: 65,
    15: 45
}

valores_temporales_iniciales = {
    1: 45,
    9: 130
}

def mover_suave(S1, AI1, AF1, S2, AI2, AF2, duracion):
    pasos = 50
    intervalo = duracion / pasos
    PA1 = (AF1 - AI1) / pasos
    PA2 = (AF2 - AI2) / pasos

    for i in range(pasos + 1):
        ACT1 = AI1 + (PA1 * i)
        ACT2 = AI2 + (PA2 * i)
        kit.servo[S1].angle = ACT1
        kit.servo[S2].angle = ACT2
        time.sleep(intervalo)

def mover_suave_multiple(servos_angulo, duracion):
    pasos = 50
    intervalo = duracion / pasos

    # Calcular la diferencia de ángulo y el paso para cada servo
    diferencias = {}
    pasos_angular = {}
    for servo, (inicio, fin) in servos_angulo.items():
        diferencias[servo] = (fin - inicio) / pasos
        pasos_angular[servo] = inicio

    for i in range(pasos + 1):
        for servo in servos_angulo:
            kit.servo[servo].angle = pasos_angular[servo] + (diferencias[servo] * i)
        time.sleep(intervalo)

def agacharse(duracion):
    # Ángulos finales para cada servo durante el agachamiento
    angulos_finales = {
        12: 60,
        13: 55,
        15: 91,
        4: 60,
        5: 55,
        7: 91
    }
    
    servos_angulo = {}
    for servo in angulos_finales:
        servos_angulo[servo] = (valores_iniciales[servo], angulos_finales[servo])
    
    # Mueve los servos a los ángulos especificados suavemente
    mover_suave_multiple(servos_angulo, duracion)

def animaciones():
    print("Iniciando animaciones...")

    # Secuencia de animación
    mover_suave(2, valores_iniciales[2], valores_maximos[2], 10, valores_iniciales[10], valores_maximos[10], 5)
    mover_suave(2, valores_maximos[2], valores_iniciales[2], 10, valores_maximos[10], valores_iniciales[10], 5)
    mover_suave(2, valores_iniciales[2], valores_minimos[2], 10, valores_iniciales[10], valores_minimos[10], 5)
    mover_suave(2, valores_minimos[2], valores_iniciales[2], 10, valores_minimos[10], valores_iniciales[10], 5)

    print("Animaciones completadas.")

def preparar_y_animar():
    print("Moviendo servos a posiciones temporales...")
    # Mueve los servos 1 y 9 a los valores temporales iniciales suavemente
    mover_suave(1, valores_iniciales[1], valores_temporales_iniciales[1], 9, valores_iniciales[9], valores_temporales_iniciales[9], 2)
    
    # Espera para asegurarse de que los servos lleguen a las posiciones temporales
    print("Esperando a que los servos lleguen a posiciones temporales...")
    time.sleep(2)

    # Inicia las animaciones
    animaciones()

    print("Moviendo servos de regreso a posiciones iniciales...")
    # Mueve los servos 1 y 9 de regreso a los valores iniciales suavemente
    mover_suave(1, valores_temporales_iniciales[1], valores_iniciales[1], 9, valores_temporales_iniciales[9], valores_iniciales[9], 2)

# Ejecuta la función que prepara los servos y luego inicia la animación
preparar_y_animar()

# Llama a la función agacharse después de completar las animaciones
print("Iniciando agachamiento...")
agacharse(duracion=3)
print("Agachamiento completado.")
