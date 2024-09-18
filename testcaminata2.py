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
    6: 130, 
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
    6: 30, 
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

def mover_pierna_adelante_y_atras(S1,AI1,AF1,S2,AI2,AF2,duracion):
    pasos=50
    intervalo=duracion/pasos
    PA1 = (AF1-AI1)/pasos
    PA2 = (AF2-AI2)/pasos

    for i in range(pasos+1):
        kit.servo[S1].angle = AI1 + (PA1*i)
        kit.servo[S2].angle = AI2 + (PA2*i)
        time.sleep(intervalo)

def PIETOB(S1,AI1,AF1,S2,AI2,AF2,S3,AI3,AF3,S4,AI4,AF4,duracion):
    pasos = 50
    intervalo = duracion / pasos
    
    PA1 = (AF1 - AI1) / pasos
    PA2 = (AF2 - AI2) / pasos
    PA3 = (AF3 - AI3) / pasos
    PA4 = (AF4 - AI4) / pasos

    for i in range(pasos + 1):
        kit.servo[S1].angle = AI1 + (PA1 * i)
        kit.servo[S2].angle = AI2 + (PA2 * i)
        kit.servo[S3].angle = AI3 + (PA3 * i)
        kit.servo[S4].angle = AI4 + (PA4 * i)
        time.sleep(intervalo)

def preparar_y_animar():
    print("Moviendo servos a posiciones temporales...")
    # Mueve los servos 1 y 9 a los valores temporales iniciales suavemente
    mover_suave(1, valores_iniciales[1], valores_temporales_iniciales[1], 9, valores_iniciales[9], valores_temporales_iniciales[9],0, valores_iniciales[0],valores_iniciales[0],2)
    PIETOB(4,valores_iniciales[4],valores_maximos[4],12,valores_iniciales[12],valores_maximos[12],6,valores_iniciales[6],valores_maximos[6],14,valores_iniciales[14],valores_maximos[14],2)
    print("1-hecho")
    time.sleep(0.5)
    #mover_pierna_adelante_y_atras(6,valores_iniciales[6],valores_maximos[6],13,valores_iniciales[13],valores_maximos[13],0.5)
    #mover_suave(5,valores_iniciales[5],valores_maximos[5],13,valores_minimos[13],valores_maximos[13],6,valores_iniciales[6],valores_maximos[6],2)
    print("2-hecho")
    #mover_pierna_adelante_y_atras(5,valores_maximos[5],valores_iniciales[5],13, valores_maximos[13],valores_iniciales[13],3)
    print("3-hecho")
    #time.sleep(1)
    #mover_suave(4,valores_maximos[4],valores_iniciales[4],12, valores_maximos[12],valores_iniciales[12],6,valores_maximos[6],valores_iniciales[6],3)
    print("4-hecho")
    
    PIETOB(4,valores_maximos[4],valores_iniciales[4],12,valores_maximos[12],valores_iniciales[12],6,valores_maximos[6],valores_iniciales[6],14,valores_maximos[14],valores_iniciales[14],2)

    #servos_adelante = [13, 14, 15]
    #servos_atras = [5, 6, 7]
    # Espera para asegurarse de que los servos lleguen a las posiciones temporales
    print("Esperando a que los servos lleguen a posiciones temporales...")
    time.sleep(2)

    print("Moviendo servos de regreso a posiciones iniciales...")
    # Mueve los servos 1 y 9 de regreso a los valores iniciales suavemente
    mover_suave(1, valores_temporales_iniciales[1], valores_iniciales[1], 9, valores_temporales_iniciales[9], valores_iniciales[9],0,valores_iniciales[0],valores_iniciales[0],2)

# Ejecuta la función que prepara los servos y luego inicia la animación
preparar_y_animar()
