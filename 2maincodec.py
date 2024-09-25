import time
from adafruit_servokit import ServoKit

mover = ServoKit(channels=16)

inicial = {
    0: 90, 1: 110, 2: 90, 3: 100, 4: 100,
    5: 85, 6: 90, 7: 90, 8: 90, 9: 115,
    10: 80, 11: 90, 12: 100, 13: 90, 14: 90, 15: 90
}

def start():
    print("Iniciando Programa...")
    srv(range(16), [inicial[i] for i in range(16)], [inicial[i] for i in range(16)], 5)

def srv(servos, ai, af, duracion):
    pasos = 30
    intervalo = duracion / pasos
    cambios = [(ang_f - ang_i) / pasos for ang_i, ang_f in zip(ai, af)]
    for i in range(pasos + 1):
        for j, servo in enumerate(servos):
            mover.servo[servo].angle = ai[j] + (cambios[j] * i)
        time.sleep(intervalo)

def caminar():
    start()
    print("Iniciando caminata..")
    max_cam = {
        13: 133, 12: 90, 11: 120, 10: 115, 9: 110, 8: 90,
        2: 133, 3: 110, 4: 120, 5: 120, 6: 110, 7: 90
    }
    min_cam = {
        13: 47, 12: 80, 11: 60, 10: 60, 9: 75, 8: 85,
        2: 47, 3: 95, 4: 70, 5: 60, 6: 75, 7: 100
    }

    srv([3, 12, 7, 8], [inicial[3], inicial[12], inicial[7], inicial[8]], [max_cam[3], max_cam[12], min_cam[7], max_cam[8]], 0.5)
    print("Caderas Finalizadas")

    srv([3, 4, 5, 6, 9, 10, 11, 12, 7, 2, 13],
        [inicial[3], inicial[4], inicial[5], inicial[6], inicial[9], inicial[10], inicial[11], inicial[12], inicial[7], inicial[2], inicial[13]],
        [max_cam[3], max_cam[4], max_cam[5], max_cam[6], max_cam[9], max_cam[10], max_cam[11], max_cam[12], max_cam[7], min_cam[2], max_cam[13]], 1.5)

    srv([3, 4, 5, 6, 9, 10, 11, 12, 8, 2, 13],
        [max_cam[3], max_cam[4], max_cam[5], max_cam[6], max_cam[9], max_cam[10], max_cam[11], max_cam[12], inicial[8], min_cam[2], max_cam[13]],
        [min_cam[3], min_cam[4], min_cam[5], min_cam[6], min_cam[9], min_cam[10], min_cam[11], min_cam[12], min_cam[8], max_cam[2], min_cam[13]], 1.5)

    srv([3, 4, 5, 6, 9, 10, 11, 12, 8, 2, 13],
        [min_cam[3], min_cam[4], min_cam[5], min_cam[6], min_cam[9], min_cam[10], min_cam[11], min_cam[12], min_cam[8], max_cam[2], min_cam[13]],
        [inicial[3], inicial[4], inicial[5], inicial[6], inicial[9], inicial[10], inicial[11], inicial[12], inicial[8], inicial[2], inicial[13]], 1.5)

def grulla():
    start()
    print("Iniciando Grulla.. ")
    max_grl = {
        5: 135, 6: 150, 8: 60, 7: 150  # Ajusta según tu configuración
    }
    min_grl = {
        5: 90, 6: 100, 8: 90, 7: 90  # Ajusta según tu configuración
    }
    srv([5, 6, 7, 8],
        [inicial[5], inicial[6], inicial[7], inicial[8]],
        [max_grl[5], max_grl[6], max_grl[7], max_grl[8]], 1)
    srv([5, 6, 7, 8],
        [max_grl[5], max_grl[6], max_grl[7], max_grl[8]],
        [min_grl[5], min_grl[6], min_grl[7], min_grl[8]], 1)

def corazon():
    start()
    print("Iniciando Corazon..")
    max_cor = {
        1: 160, 2: 70, 10: 120  # Ajusta según tu configuración
    }
    min_cor = {
        1: 100, 2: 90, 10: 80  # Ajusta según tu configuración
    }
    srv([1, 2, 10],
        [inicial[1], inicial[2], inicial[10]],
        [max_cor[1], max_cor[2], max_cor[10]], 1)
    srv([1, 2, 10],
        [max_cor[1], max_cor[2], max_cor[10]],
        [min_cor[1], min_cor[2], min_cor[10]], 1)

def zombie():
    start()
    print("Iniciando Zombie..")
    max_zom = {
        3: 130, 4: 130, 5: 150, 6: 150  # Ajusta según tu configuración
    }
    min_zom = {
        3: 90, 4: 90, 5: 110, 6: 110  # Ajusta según tu configuración
    }
    srv([3, 4, 5, 6],
        [inicial[3], inicial[4], inicial[5], inicial[6]],
        [max_zom[3], max_zom[4], max_zom[5], max_zom[6]], 1)
    srv([3, 4, 5, 6],
        [max_zom[3], max_zom[4], max_zom[5], max_zom[6]],
        [min_zom[3], min_zom[4], min_zom[5], min_zom[6]], 1)

# Bucle para ejecutar las funciones
try:
    while True:
        caminar()
        time.sleep(10)  # Espera antes de comenzar de nuevo
        grulla()
        time.sleep(10)
        corazon()
        time.sleep(10)
        zombie()
        time.sleep(10)  # Espera antes de volver a empezar
except KeyboardInterrupt:
    print("Programa finalizado.")
