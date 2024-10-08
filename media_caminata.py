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
    5: 110,
    6: 95, 
    7: 78, 
    8: 90, 
    9: 100, 
    10: 90, 
    11: 90,
    12: 90, 
    13: 110, 
    14: 90, 
    15: 80
}

valores_maximos = {
    0: 170, 
    1: 160, 
    2: 150, 
    3: 95, 
    4: 110, 
    5: 130, 
    6: 110, 
    7: 90, 
    8: 90, 
    9: 150, 
    10: 175, 
    11: 100, 
    12: 100, 
    13: 120, 
    14: 125, 
    15: 75 
}

valores_minimos = {
    0: 90, 
    1: 45, 
    2: 25, 
    3: 90, 
    4: 55, 
    5: 50, 
    6: 60, 
    7: 90, 
    8: 25, 
    9: 25, 
    10: 25, 
    11: 110, 
    12: 75, 
    13: 60, 
    14: 65, 
    15: 80 
}

valores_temporales_iniciales = {
    1: 45,
    9: 130,
    7:110,
    15:100
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
    #mover_suave(1, valores_iniciales[1], valores_temporales_iniciales[1], 9, valores_iniciales[9], valores_temporales_iniciales[9],0, valores_iniciales[0],valores_iniciales[0],2)
    PIETOB(3,valores_iniciales[3],valores_maximos[3],11,valores_iniciales[11],valores_maximos[11],7,valores_iniciales[7],valores_iniciales[7],15,valores_iniciales[15],valores_maximos[15],5)
    PIETOB(4,valores_iniciales[4],valores_maximos[4],12,valores_iniciales[12],valores_maximos[12],6,valores_iniciales[6],valores_maximos[6],14,valores_iniciales[14],valores_maximos[14],5)
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
    
    PIETOB(4,valores_maximos[4],valores_minimos[4],12,valores_maximos[12],valores_minimos[12],6,valores_maximos[6],valores_minimos[6],14,valores_maximos[14],valores_minimos[14],5)
    PIETOB(4,valores_minimos[4],valores_iniciales[4],12,valores_minimos[12],valores_iniciales[12],6,valores_minimos[6],valores_iniciales[6],14,valores_minimos[14],valores_iniciales[14],5)

    #servos_adelante = [13, 14, 15]
    #servos_atras = [5, 6, 7]
    # Espera para asegurarse de que los servos lleguen a las posiciones temporales
    print("Esperando a que los servos lleguen a posiciones temporales...")
    time.sleep(2)

    print("Moviendo servos de regreso a posiciones iniciales...")
    # Mueve los servos 1 y 9 de regreso a los valores iniciales suavemente
    mover_suave(1, valores_temporales_iniciales[1], valores_iniciales[1], 9, valores_temporales_iniciales[9], valores_iniciales[9],0,valores_iniciales[0],valores_iniciales[0],0.5)

# Ejecuta la función que prepara los servos y luego inicia la animación
preparar_y_animar()

