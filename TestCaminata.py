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
    0: 170, #1
    1: 160, #2
    2: 150, #3
    #######################
    3: 100, #4
    ##################
    4: 130, #5
    5: 130, #6
    6: 90, #7
    7: 90, #8
    ###################
    8: 90, #9
    9: 150, #10
    10: 175, #11
    ########################
    11: 100, #12
    ########################
    12: 130, #13
    13: 120, #14
    14: 100, #15
    15: 75 #16
}

valores_minimos = {
    0: 90, #1
    1: 45, #2
    2: 25, #3
    ##############################
    3: 110, #4
    #################
    4: 50, #5
    5: 50, #6
    6: 90, #7
    7: 90, #8
    ####################
    8: 25, #9
    9: 25, #10
    10: 25, #11
    #######################
    11: 110, #12
    #####################
    12: 50, #13
    13: 60, #14
    14: 80, #15
    15: 80 #16
}

valores_temporales_iniciales = {
    1: 45,
    9: 130
}

def mover_pierna_adelante(S1, AI1, AF1, S2, AI2, AF2, S3, AI3, AF3, S4, AI4, AF4,duracion):
    pasos = 50
    intervalo = duracion / pasos
    PA1 = (AF1 - AI1) / pasos
    PA2 = (AF2 - AI2) / pasos
    PA3 = (AF3-AI3)/pasos
    PA4 = (AF4-AI4)/pasos

    for i in range(pasos + 1):
        ACT1 = AI1 + (PA1 * i)
        ACT2 = AI2 + (PA2 * i)
        ACT3 = AI3 + (PA3 * i)
        ACT4 = AI4 + (PA4 * i)
        kit.servo[S1].angle = ACT1
        kit.servo[S2].angle = ACT2
        kit.servo[S3].angle = ACT3
        kit.servo[S4].angle = ACT4
        time.sleep(intervalo)

def mover_pierna_atras(S1, AI1, AF1, S2, AI2, AF2, S3, AI3, AF3, S4, AI4, AF4,duracion):
    pasos = 50
    intervalo = duracion / pasos
    PA1 = (AF1 - AI1) / pasos
    PA2 = (AF2 - AI2) / pasos
    PA3 = (AF3-AI3)/pasos
    PA4 = (AF4-AI4)/pasos

    for i in range(pasos + 1):
        ACT1 = AI1 + (PA1 * i)
        ACT2 = AI2 + (PA2 * i)
        ACT3 = AI3 + (PA3 * i)
        ACT4 = AI4 + (PA4 * i)
        kit.servo[S1].angle = ACT1
        kit.servo[S2].angle = ACT2
        kit.servo[S3].angle = ACT3
        kit.servo[S4].angle = ACT4
        time.sleep(intervalo)

def pie_adelante(S1, AI1, AF1, S2, AI2, AF2,duracion):
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

def pie_atras(S1, AI1, AF1, S2, AI2, AF2, S3, AI3, AF3, S4, AI4, AF4,duracion):
    pasos = 50
    intervalo = duracion / pasos
    PA1 = (AF1 - AI1) / pasos
    PA2 = (AF2 - AI2) / pasos
    PA3 = (AF3-AI3)/pasos
    PA4 = (AF4-AI4)/pasos

    for i in range(pasos + 1):
        ACT1 = AI1 + (PA1 * i)
        ACT2 = AI2 + (PA2 * i)
        ACT3 = AI3 + (PA3 * i)
        ACT4 = AI4 + (PA4 * i)
        kit.servo[S1].angle = ACT1
        kit.servo[S2].angle = ACT2
        kit.servo[S3].angle = ACT3
        kit.servo[S4].angle = ACT4
        time.sleep(intervalo)



def mover_suave(S1, AI1, AF1, S2, AI2, AF2, S3, AI3, AF3, S4, AI4, AF4,duracion):
    pasos = 50
    intervalo = duracion / pasos
    PA1 = (AF1 - AI1) / pasos
    PA2 = (AF2 - AI2) / pasos
    PA3 = (AF3-AI3)/pasos
    PA4 = (AF4-AI4)/pasos

    for i in range(pasos + 1):
        ACT1 = AI1 + (PA1 * i)
        ACT2 = AI2 + (PA2 * i)
        ACT3 = AI3 + (PA3 * i)
        ACT4 = AI4 + (PA4 * i)
        kit.servo[S1].angle = ACT1
        kit.servo[S2].angle = ACT2
        kit.servo[S3].angle = ACT3
        kit.servo[S4].angle = ACT4
        time.sleep(intervalo)

def animaciones():
    print("Iniciando animaciones...")
    
    # Secuencia de animación
    mover_suave(5, valores_iniciales[5], valores_maximos[5], 6, valores_iniciales[6], valores_maximos[6], 7, valores_iniciales[7], valores_maximos[7], 13, valores_iniciales[13], valores_maximos[13], 14, valores_iniciales[14], valores_maximos[14], 15, valores_iniciales[15], valores_maximos[15],5)
    mover_suave(8, valores_iniciales[8], valores_maximos[8], 16, valores_iniciales[16], valores_maximos[16], 5)
    mover_suave(5, valores_maximos[5], valores_minimos[5], 6, valores_maximos[6], valores_minimos[6], 7, valores_maximos[7], valores_minimos[7], 13, valores_maximos[13], valores_minimos[13], 14, valores_maximos[14], valores_minimos[14], 15, valores_maximos[15], valores_minimos[15], 5)
    mover_suave(8, valores_iniciales[8], valores_maximos[8], 16, valores_iniciales[16], valores_maximos[16], 5)
    
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
