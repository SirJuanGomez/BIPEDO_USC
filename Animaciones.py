import time
from adafruit_servokit import ServoKit

# Inicializa el controlador de servos con 16 canales
kit = ServoKit(channels=16)

# Valores iniciales, máximos y mínimos para los servos
inicial = {
    0: 90, #codod
    1: 85, #brazod
    2: 90, #hombrod
    3: 90, #caderad
    4: 85, #piernad
    5: 90, #rodillad
    6: 95, #tobilld
    7: 90, #pied
    8: 90, #codoi
    9: 100, #brazoi
    10: 90, #hombri
    11: 90, #cadei
    12: 90, #pierni
    13: 90, #rodilli
    14: 90, #tobili
    15: 80 #piei
}

maximos = {
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

minimos = {
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

maximo_tmp ={
    13:85
}
def SRV2(S1,AI1,AF1,S2,AI2,AF2,D):
    pasos=30
    intervalo=D/pasos
    
    PA1=(AF1-AI1)/pasos
    PA2=(AF2-AI2)/pasos
    for i in (pasos+1):
        kit.servo[S1].angle=AI1+(PA1*i)
        kit.servo[S2].angle=AI2+(PA2*i)
        time.sleep(intervalo)

def SRV3(S1,AI1,AF1,S2,AI2,AF2,S3,AI3,AF3,D):
    pasos=30
    intervalo=D/pasos
    
    PA1=(AF1-AI1)/pasos
    PA2=(AF2-AI2)/pasos
    PA3=(AF3-AI3)/pasos
    for i in (pasos+1):
        kit.servo[S1].angle=AI1+(PA1*i)
        kit.servo[S2].angle=AI2+(PA2*i)
        kit.servo[S3].angle=AI3+(PA3*i)
        time.sleep(intervalo)

def SRV4(S1,AI1,AF1,S2,AI2,AF2,S3,AI3,AF3,S4,AI4,AF4,D):
    pasos=30
    intervalo=D/pasos
    
    PA1=(AF1-AI1)/pasos
    PA2=(AF2-AI2)/pasos
    PA3=(AF3-AI3)/pasos
    PA4=(AF4-AI4)/pasos

    for i in (pasos+1):
        kit.servo[S1].angle=AI1+(PA1*i)
        kit.servo[S2].angle=AI2+(PA2*i)
        kit.servo[S3].angle=AI3+(PA3*i)
        kit.servo[S4].angle=AI4+(PA4*i)
        time.sleep(intervalo)

def YOGA():
    print("Iniciando YOGA...")
    SRV2(1,inicial[1],maximos[1],9,inicial[9],maximos[9],2)
    SRV3(11,inicial[11],maximos[11],15,inicial[15],maximos[15],13,inicial[13],maximo_tmp[13],5)
    SRV3(11,maximos[13],inicial[13],15,maximos[15],inicial[15],13,maximo_tmp[13],inicial[13],5)

YOGA()