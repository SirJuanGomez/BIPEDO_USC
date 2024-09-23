import time
from adafruit_servokit import ServoKit

# Inicializa el controlador de servos con 16 canales
kit = ServoKit(channels=16)

# Valores iniciales, máximos y mínimos para los servos
inicial = {0: 90, 1: 85, 2: 90, 3: 100, 4: 85, 5: 120, 
           6: 75,7: 85, 8: 90, 9: 100, 10: 90, 11: 120, 
           12: 90, 13: 90, 14: 90, 15: 100}

maximos= {0: 99.0, 1: 93.5, 2: 99.0, 3: 110.0, 4: 93.5, 5: 132.0,
          6: 82.5, 7: 93.5, 8: 99.0, 9: 110.0, 10: 99.0, 11: 132.0,
          12: 99.0, 13: 99.0, 14: 99.0, 15: 110.0}

minimos= {0: 81.0, 1: 76.5, 2: 81.0, 3: 90.0, 4: 76.5, 5: 108.0,
          6: 67.5, 7: 76.5, 8: 81.0, 9: 90.0, 10: 81.0, 11: 108.0,
          12: 81.0, 13: 81.0, 14: 81.0, 15: 90.0}


maximo_tmp = {13: 85,
              7:100,
              3:110}

def start():
    print("Servos en posicion inicial..")
    mover_servos(range(16),[inicial[i] 
                            for i in range(16)],2
                            )

def mover_servos(servos, AI, AF, duracion):
    pasos = 30
    intervalo = duracion / pasos
    
    cambios = [(ang_final - ang_inicial) / pasos for ang_inicial, ang_final in zip(AI, AF)]
    
    for i in range(pasos + 1):
        for j, servo in enumerate(servos):
            kit.servo[servo].angle = AI[j] + (cambios[j] * i)
        time.sleep(intervalo)

def caminata():
    start()
    print("Iniciando caminata...")
    mover_servos([3,11,15], [inicial[3],inicial[11],inicial[15]],[maximos[3],maximos[11],maximos[15]],5)
    mover_servos([2,3,4,6,7,10,12,14], [inicial[2],inicial[4],inicial[3],inicial[6],inicial[7],inicial[10],inicial[12],inicial[14]],[maximos[2],maximo_tmp[3],maximos[4],maximos[6],maximo_tmp[7],maximos[10],maximos[12],maximos[14]],5)
    print("Parte 1- Hecho...")
    time.sleep(3)
    mover_servos([3,11,15],[maximos[3],maximos[11],inicial[15]],[minimos[3],minimos[11],inicial[15]],3)
    print("Cadera Corregida..")
    time.sleep(1)
    mover_servos([2,4,6,7,10,12,14],[maximos[2],maximos[4],maximos[6],maximo_tmp[7],maximos[10],maximos[12],maximos[14]],[minimos[2],minimos[4],minimos[6],minimos[7],minimos[10],minimos[12],minimos[14]],10)
    print("Parte 2- Hecho..")
    time.sleep(1)
    mover_servos([2,4,6,7,10,12,14],[minimos[2],minimos[4],minimos[6],minimos[7],minimos[10],minimos[12],minimos[14]],[inicial[2],inicial[4],inicial[6],inicial[7],inicial[10],inicial[12],inicial[14]],2)
    print("Parte 3- Hecho..")
    time.sleep(0.1)
    print("Finalizando..")
caminata()
