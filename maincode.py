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
    6:90,
    7:90,
    8:90,
    9:115,
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

        13:133,12:90,11:120,10:115,9:110,8:90, #Maximos D

        2:133,3:110,4:120,5:120,6:110,7:90 #MaximosI
    }

    min_cam={
        
        13:47,12:80,11:60,10:60,9:75,8:85, #Minimos D
        
        2:47,3:95,4:70,5:60,6:75,7:100 #Minimos I
    }

    srv([3,12,7,8],[inicial[3],inicial[12],inicial[7],inicial[8]],[max_cam[3],max_cam[12],min_cam[7],max_cam[8]],0.5)
    
    print("Caderas Finalizadas")

    srv([3,4,5,6,9,10,11,12,7,2,13],[inicial[3],inicial[4],inicial[5],inicial[6],inicial[9],inicial[10],inicial[11],inicial[12],inicial[7],inicial[2],inicial[13]],[max_cam[3],max_cam[4],max_cam[5],max_cam[6],max_cam[9],max_cam[10],max_cam[11],max_cam[12],max_cam[7],min_cam[2],max_cam[13]],1.5)
    
    srv([3,4,5,6,9,10,11,12,8,2,13],[max_cam[3],max_cam[4],max_cam[5],max_cam[6],max_cam[9],max_cam[10],max_cam[11],max_cam[12],inicial[8],min_cam[2],max_cam[13]],[min_cam[3],min_cam[4],min_cam[5],min_cam[6],min_cam[9],min_cam[10],min_cam[11],min_cam[12],min_cam[8],max_cam[2],min_cam[13]],1.5)
    
    srv([3,4,5,6,9,10,11,12,8,2,13],[min_cam[3],min_cam[4],min_cam[5],min_cam[6],min_cam[9],min_cam[10],min_cam[11],min_cam[12],min_cam[8],max_cam[2],min_cam[13]],[inicial[3],inicial[4],inicial[5],inicial[6],inicial[9],inicial[10],inicial[11],inicial[12],inicial[8],inicial[2],inicial[13]],1.5)
  
caminar()
start()