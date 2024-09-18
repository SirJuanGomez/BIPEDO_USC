import time
from adafruit_servokit import ServoKit

# Inicializa el controlador de servos con 16 canales
kit = ServoKit(channels=16)

# Valores iniciales, máximos y mínimos para los servos
valores_iniciales = {
    0: 90, 
    1: 85, 
    2: 90, 
    3: 90, 
    4: 85, 
    5: 90,
    6: 95, 
    7: 90, 
    8: 90, 
    9: 100, 
    10: 90, 
    11: 90,
    12: 90, 
    13: 90, 
    14: 90, 
    15: 80
}

valores_maximos = {
    0: 170, 
    1: 160, 
    2: 150, 
    3: 100, 
    4: 130, 
    5: 130, 
    6: 90, 
    7: 90, 
    8: 90, 
    9: 150, 
    10: 175, 
    11: 100, 
    12: 130, 
    13: 120, 
    14: 100, 
    15: 75 
}

valores_minimos = {
    0: 90, 
    1: 45, 
    2: 25, 
    3: 110, 
    4: 50, 
    5: 50, 
    6: 90, 
    7: 90, 
    8: 25, 
    9: 25, 
    10: 25, 
    11: 110, 
    12: 50, 
    13: 60, 
    14: 80, 
    15: 80 
}

valores_temporales_iniciales = {
    1: 45,
    9: 130
}

def mover_suave(S1, AI1, AF1, S2, AI2, AF2, S3, AI3, AF3, duracion):
    pasos = 50
    intervalo = duracion / pasos
    PA1 = (AF1 - AI1) / pasos
    PA2 = (AF2 - AI2) / pasos
    PA3 = (AF3 - AI3) / pasos

    for i in range(pasos + 1):
        kit.servo[S1].angle = AI1 + (PA1 * i)
        kit.servo[S2].angle = AI2 + (PA2 * i)
        kit.servo[S3].angle = AI3 + (PA3 * i)
        time.sleep(intervalo)

def mover_pierna_adelante_y_atras(duracion):
    # Definición de servos
    servos_adelante = [13, 14, 15]
    servos_atras = [5, 6, 7]
    
    # Ángulos iniciales
    AI_adelante = [valores_iniciales[s] for s in servos_adelante]
    AI_atras = [valores_iniciales[s] for s in servos_atras]
    
    # Ángulos máximos
    AF_adelante = [valores_maximos[s] for s in servos_adelante]
    AF_atras = [valores_maximos[s] for s in servos_atras]
    
    # Ángulos mínimos
    AM_adelante = [valores_minimos[s] for s in servos_adelante]
    AM_atras = [valores_minimos[s] for s in servos_atras]

    # Mover ambos grupos a sus ángulos máximos
    mover_suave(servos_adelante[0], AI_adelante[0], AF_adelante[0], 
                 servos_adelante[1], AI_adelante[1], AF_adelante[1], 
                 servos_adelante[2], AI_adelante[2], AF_adelante[2], 
                 duracion)

    mover_suave(servos_atras[0], AI_atras[0], AF_atras[0], 
                 servos_atras[1], AI_atras[1], AF_atras[1], 
                 servos_atras[2], AI_atras[2], AF_atras[2], 
                 duracion)

    # Volver al ángulo inicial
    mover_suave(servos_adelante[0], AF_adelante[0], AI_adelante[0], 
                 servos_adelante[1], AF_adelante[1], AI_adelante[1], 
                 servos_adelante[2], AF_adelante[2], AI_adelante[2], 
                 duracion)

    mover_suave(servos_atras[0], AF_atras[0], AI_atras[0], 
                 servos_atras[1], AF_atras[1], AI_atras[1], 
                 servos_atras[2], AF_atras[2], AI_atras[2], 
                 duracion)

    # Mover a ángulos mínimos
    mover_suave(servos_adelante[0], AI_adelante[0], AM_adelante[0], 
                 servos_adelante[1], AI_adelante[1], AM_adelante[1], 
                 servos_adelante[2], AI_adelante[2], AM_adelante[2], 
                 duracion)

    mover_suave(servos_atras[0], AI_atras[0], AM_atras[0], 
                 servos_atras[1], AI_atras[1], AM_atras[1], 
                 servos_atras[2], AI_atras[2], AM_atras[2], 
                 duracion)

def animaciones():
    print("Iniciando animaciones...")
    mover_pierna_adelante_y_atras(5)
    print("Animaciones completadas.")

def preparar_y_animar():
    print("Moviendo servos a posiciones temporales...")
    # Mueve los servos 1 y 9 a los valores temporales iniciales suavemente
    mover_suave(1, valores_iniciales[1], valores_temporales_iniciales[1], 
                 9, valores_iniciales[9], valores_temporales_iniciales[9], 
                 2)

    # Espera para asegurarse de que los servos lleguen a las posiciones temporales
    print("Esperando a que los servos lleguen a posiciones temporales...")
    time.sleep(2)

    # Inicia las animaciones
    animaciones()

    print("Moviendo servos de regreso a posiciones iniciales...")
    # Mueve los servos 1 y 9 de regreso a los valores iniciales suavemente
    mover_suave(1, valores_temporales_iniciales[1], valores_iniciales[1], 
                 9, valores_temporales_iniciales[9], valores_iniciales[9], 
                 2)

# Ejecuta la función que prepara los servos y luego inicia la animación
preparar_y_animar()
