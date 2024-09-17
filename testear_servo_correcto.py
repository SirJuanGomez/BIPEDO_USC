import time
import threading
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
    0: 170, #1
    1: 160, #2
    2: 150, #3
    3: 110, #4
    4: 140, #5
    5: 130, #6
    6: 140, #7
    7: 120, #8
    8: 90, #9
    9: 150, #10
    10: 175, #11
    11: 155, #12
    12: 140, #13
    13: 130, #14
    14: 180, #15
    15: 120 #16
}

valores_minimos = {
    0: 90, #1
    1: 45, #2
    2: 25, #3
    3: 25, #4
    4: 30, #5
    5: 40, #6
    6: 40, #7
    7: 45, #8
    8: 25, #9
    9: 25, #10
    10: 25, #11
    11: 80, #12
    12: 30, #13
    13: 40, #14
    14: 65, #15
    15: 45 #16
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

def animaciones():
    # Definir los movimientos de animación
    threads = [
        threading.Thread(target=mover_suave, args=(2, valores_iniciales[2], valores_maximos[2], 10, valores_iniciales[10], valores_maximos[10], 5)),
        threading.Thread(target=mover_suave, args=(2, valores_maximos[2], valores_iniciales[2], 10, valores_maximos[10], valores_iniciales[10], 5)),
        threading.Thread(target=mover_suave, args=(2, valores_iniciales[2], valores_minimos[2], 10, valores_iniciales[10], valores_minimos[10], 5)),
        threading.Thread(target=mover_suave, args=(2, valores_minimos[2], valores_iniciales[2], 10, valores_minimos[10], valores_iniciales[10], 5))
    ]
    
    # Inicia los hilos de animación
    for thread in threads:
        thread.start()

    # Espera a que todos los hilos de animación terminen
    for thread in threads:
        thread.join()

def preparar_y_animar():
    # Mueve los servos 1 y 9 a los valores temporales iniciales suavemente
    mover_suave(1, valores_iniciales[1], valores_temporales_iniciales[1], 9, valores_iniciales[9], valores_temporales_iniciales[9], 2)
    
    # Espera para asegurarse de que los servos lleguen a las posiciones temporales
    time.sleep(2)

    # Inicia las animaciones
    animaciones()

    # Mueve los servos 1 y 9 de regreso a los valores iniciales suavemente
    mover_suave(1, valores_temporales_iniciales[1], valores_iniciales[1], 9, valores_temporales_iniciales[9], valores_iniciales[9], 2)

# Ejecuta la función que prepara los servos y luego inicia la animación
preparar_y_animar()
