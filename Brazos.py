import time
from adafruit_servokit import ServoKit

# Inicialización del controlador de servos
mover = ServoKit(channels=16)

# Definición de los canales de los servos
MANOD = 0
CODOD = 1
HOMBROD = 2
CADERAD = 3
MUSLOD = 4
RODILLAD = 5
TOBILLOD = 6
PIED = 7
MANOI = 8
CODOI = 9
HOMBROI = 10
CADERAI = 11
MUSLOI = 12
RODILLAI = 13
TOBILLOI = 14
PIEI = 15

def mover_servo_suavemente(servo, angulo_inicial, angulo_final, paso=1, retraso=0.02):
    """
    Mueve un servo suavemente de angulo_inicial a angulo_final en pequeños pasos.
    Parámetros:
        servo (int): El canal del servo a mover.
        angulo_inicial (int): El ángulo inicial del servo.
        angulo_final (int): El ángulo objetivo a alcanzar.
        paso (int): El tamaño del paso en grados. Positivo para aumentar, negativo para disminuir.
        retraso (float): El tiempo a esperar entre pasos (controla la velocidad del movimiento).
    """
    if angulo_inicial < angulo_final:
        paso = abs(paso)  # Asegura que el paso sea positivo
    else:
        paso = -abs(paso)  # Asegura que el paso sea negativo para movimiento inverso
    
    for angulo in range(angulo_inicial, angulo_final, paso):
        mover.servo[servo].angle = angulo
        time.sleep(retraso)
    
    # Asegura que el servo llegue al ángulo objetivo exacto
    mover.servo[servo].angle = angulo_final
    time.sleep(retraso)

def configuracion_inicio():
    # SERVOS LADO DERECHO
    mover.servo[HOMBROD].angle = 90
    mover.servo[CODOD].angle = 90
    
    # SERVOS LADO IZQUIERDO
    mover.servo[HOMBROI].angle = 90
    mover.servo[CODOI].angle = 90

def mover_brazo_derecho_adelante():
    angulo_inicial_hombro = mover.servo[HOMBROD].angle
    angulo_final_hombro = 70  # Ángulo objetivo para el hombro derecho
    angulo_final_codo = 60    # Ángulo objetivo para el codo derecho

    # Mueve el hombro derecho hacia adelante de manera suave
    for angulo in range(angulo_inicial_hombro, angulo_final_hombro, 2):
        mover.servo[HOMBROD].angle = angulo
        if angulo >= (angulo_inicial_hombro + angulo_final_hombro) / 2:
            # Mueve el codo derecho cuando el hombro llega al 50%
            mover_servo_suavemente(CODOD, mover.servo[CODOD].angle, angulo_final_codo, paso=2, retraso=0.05)
        time.sleep(0.05)
    
    mover.servo[HOMBROD].angle = angulo_final_hombro
    mover_servo_suavemente(CODOD, mover.servo[CODOD].angle, angulo_final_codo, paso=2, retraso=0.05)

def mover_brazo_izquierdo_adelante():
    angulo_inicial_hombro = mover.servo[HOMBROI].angle
    angulo_final_hombro = 70  # Ángulo objetivo para el hombro izquierdo
    angulo_final_codo = 60    # Ángulo objetivo para el codo izquierdo

    # Mueve el hombro izquierdo hacia adelante de manera suave
    for angulo in range(angulo_inicial_hombro, angulo_final_hombro, 2):
        mover.servo[HOMBROI].angle = angulo
        if angulo >= (angulo_inicial_hombro + angulo_final_hombro) / 2:
            # Mueve el codo izquierdo cuando el hombro llega al 50%
            mover_servo_suavemente(CODOI, mover.servo[CODOI].angle, angulo_final_codo, paso=2, retraso=0.05)
        time.sleep(0.05)
    
    mover.servo[HOMBROI].angle = angulo_final_hombro
    mover_servo_suavemente(CODOI, mover.servo[CODOI].angle, angulo_final_codo, paso=2, retraso=0.05)

def mover_brazo_derecho_atras():
    angulo_inicial_hombro = mover.servo[HOMBROD].angle
    angulo_final_hombro = 90  # Ángulo inicial para el hombro derecho
    angulo_final_codo = 90    # Ángulo inicial para el codo derecho

    # Mueve el hombro derecho hacia atrás de manera suave
    for angulo in range(angulo_inicial_hombro, angulo_final_hombro, 2):
        mover.servo[HOMBROD].angle = angulo
        if angulo <= (angulo_inicial_hombro + angulo_final_hombro) / 2:
            # Mueve el codo derecho cuando el hombro llega al 50%
            mover_servo_suavemente(CODOD, mover.servo[CODOD].angle, angulo_final_codo, paso=-2, retraso=0.05)
        time.sleep(0.05)
    
    mover.servo[HOMBROD].angle = angulo_final_hombro
    mover_servo_suavemente(CODOD, mover.servo[CODOD].angle, angulo_final_codo, paso=-2, retraso=0.05)

def mover_brazo_izquierdo_atras():
    angulo_inicial_hombro = mover.servo[HOMBROI].angle
    angulo_final_hombro = 90  # Ángulo inicial para el hombro izquierdo
    angulo_final_codo = 90    # Ángulo inicial para el codo izquierdo

    # Mueve el hombro izquierdo hacia atrás de manera suave
    for angulo in range(angulo_inicial_hombro, angulo_final_hombro, 2):
        mover.servo[HOMBROI].angle = angulo
        if angulo <= (angulo_inicial_hombro + angulo_final_hombro) / 2:
            # Mueve el codo izquierdo cuando el hombro llega al 50%
            mover_servo_suavemente(CODOI, mover.servo[CODOI].angle, angulo_final_codo, paso=-2, retraso=0.05)
        time.sleep(0.05)
    
    mover.servo[HOMBROI].angle = angulo_final_hombro
    mover_servo_suavemente(CODOI, mover.servo[CODOI].angle, angulo_final_codo, paso=-2, retraso=0.05)

def caminar_brazos():
    mover_brazo_derecho_adelante()
    mover_brazo_izquierdo_atras()
    time.sleep(0.5)  # Espera para coordinar el movimiento
    mover_brazo_izquierdo_adelante()
    mover_brazo_derecho_atras()
    time.sleep(0.5)  # Espera entre ciclos de movimiento

# Llama a la función de configuración al iniciar el programa
configuracion_inicio()

# Ejecuta el ciclo de caminata de los brazos
while True:
    caminar_brazos()
    time.sleep(1)  # Espera entre ciclos para evitar que el ciclo sea demasiado rápido
