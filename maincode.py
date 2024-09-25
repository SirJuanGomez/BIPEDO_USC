import time 
from adafruit_servokit import ServoKit

mover = ServoKit(channels=16)

inicial = {
    0:90,
    1:110,
    2:90,
    3:100,
    4:100,
    5:85,
    6:85,
    7:90,
    8:75,
    9:100,
    10:80,
    11:90,
    12:100,
    13:90,
    14:90,
    15:90
}

def start():
    print("Iniciando Programa...")
    srv(range(16),[inicial[i] for i in range(16)],[inicial[i] for i in range(16)],5)

def srv(servos,ai,af,duracion):
    pasos = 30
    intervalo = duracion/pasos
    
    cambios = [(ang_f - ang_i)/ pasos for ang_i,ang_f in zip(ai,af)]
    for i in range(pasos+1):
        for j, servo in enumerate(servos):
            mover.servo[servo].angle= ai[j] + (cambios[j]*i)
        time.sleep(intervalo)

def caminar():
    start()

    print("Iniciando caminata..")

    max_cam={

        12:90,11:120,10:115,9:110,8:90, #Maximos D

        3:110,4:110,5:120,6:95,7:90 #MaximosI
    }

    min_cam={
        
        12:80,11:60,10:60,9:80,8:85, #Minimos D
        
        3:95,4:70,5:60,6:85,7:100 #Minimos I
    }

    srv([3,12,7,8],[inicial[3],inicial[12],inicial[7],inicial[8]],[max_cam[3],max_cam[12],min_cam[7],max_cam[8]])
    
    print("Caderas Finalizadas")

    srv([3,4,5,6,9,10,11,12],[inicial[3],inicial[4],inicial[5],inicial[6],inicial[9],inicial[10],inicial[11],inicial[12]],[max_cam[3],max_cam[4],max_cam[5],max_cam[6],min_cam[9],min_cam[10],min_cam[11],min_cam[12]])

caminar()