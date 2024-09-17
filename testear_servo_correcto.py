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
    #Lado Derecho
    0: 170, #1
    1: 160, #2
    2: 150, #3
    ####################################
    3: 110, #4
    ################################
    4: 140, #5
    5: 130, #6
    #################################
    6: 140, #7
    7: 120, #8

    #Lado Izquierdo
    8: 90, #9
    9: 150, #10
    10: 175, #11
    ###############################
    11: 155, #12
    #############################
    12: 140, #13
    13: 130, #14
    ##############################
    14: 180, #15
    15: 120 #16
}

valores_minimos = {
    #Lado Derecho
    0: 90, #1
    1: 45, #2
    2: 25, #3
    ############################
    3: 25, #4
    ##########################
    4: 30, #5
    5: 40, #6
    #######################
    6: 40, #7
    7: 45, #8

    #Lado Izquierdo
    8: 25, #9
    9: 25, #10
    10: 25, #11
    ###############################
    11: 80, #12
    ###############################
    12: 30, #13
    13: 40, #14
    ###################################
    14: 65, #15
    15: 45 #16
}

for servo_id, angulo in valores_iniciales.items():
    kit.servo[servo_id].angle = angulo

def mover_suave(S1,AI1,AF1,S2,AI2,AF2,duracion):
    pasos=50
    intervalo=duracion/pasos
    PA1=(AF1-AI1)/pasos
    PA2=(AF2-AI2)/pasos

    for i in range(pasos+1):
        ACT1=AI1+(PA1*i)
        ACT2=AI2+(PA2*i)
        kit.servo[S1].angle=ACT1
        kit.servo[S2].angle=ACT2
        time.sleep(intervalo)
mover_suave(2,valores_iniciales[2],valores_maximos[2],10,valores_iniciales[10],valores_maximos[10],5)
mover_suave(2,valores_maximos[2],valores_iniciales[2],10,valores_maximos[10],valores_iniciales[10],5)
mover_suave(2, valores_iniciales[2],valores_minimos[2],10,valores_iniciales[10],valores_minimos[10],5)
mover_suave(2,valores_minimos[2],valores_iniciales[2],10,valores_minimos[10],valores_iniciales[10],5)