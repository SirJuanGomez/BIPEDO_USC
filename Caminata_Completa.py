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
    mover.servo[CADERAD].angle = 90
    mover.servo[RODILLAD].angle = 90
    mover.servo[TOBILLOD].angle = 90
    mover.servo[PIED].angle = 90

    # SERVOS LADO IZQUIERDO
    mover.servo[HOMBROI].angle = 90
    mover.servo[CODOI].angle = 90
    mover.servo[CADERAI].angle = 90
    mover.servo[RODILLAI].angle = 90
    mover.servo[TOBILLOI].angle = 90
    mover.servo[PIEI].angle = 90

def mover_pierna_derecha_adelante():
    # Movimiento de la pierna derecha hacia adelante
    mover_servo_suavemente(CADERAD, mover.servo[CADERAD].angle, 110, paso=2, retraso=0.05)
    mover_servo_suavemente(PIED, mover.servo[PIED].angle, 72, paso=2, retraso=0.05)
    mover_servo_suavemente(RODILLAD, mover.servo[RODILLAD].angle, 60, paso=2, retraso=0.05)

def mover_pierna_izquierda_adelante():
    # Movimiento de la pierna izquierda hacia adelante
    mover_servo_suavemente(CADERAI, mover.servo[CADERAI].angle, 110, paso=2, retraso=0.05)
    mover_servo_suavemente(PIEI, mover.servo[PIEI].angle, 72, paso=2, retraso=0.05)
    mover_servo_suavemente(RODILLAI, mover.servo[RODILLAI].angle, 60, paso=2, retraso=0.05)

def mover_pierna_derecha_atras():
    # Movimiento de la pierna derecha hacia atrás
    mover_servo_suavemente(CADERAD, mover.servo[CADERAD].angle, 90, paso=-2, retraso=0.05)
    mover_servo_suavemente(PIED, mover.servo[PIED].angle, 90, paso=-2, retraso=0.05)
    mover_servo_suavemente(RODILLAD, mover.servo[RODILLAD].angle, 90, paso=-2, retraso=0.05)

def mover_pierna_izquierda_atras():
    # Movimiento de la pierna izquierda hacia atrás
    mover_servo_suavemente(CADERAI, mover.servo[CADERAI].angle, 90, paso=-2, retraso=0.05)
    mover_servo_suavemente(PIEI, mover.servo[PIEI].angle, 90, paso=-2, retraso=0.05)
    mover_servo_suavemente(RODILLAI, mover.servo[RODILLAI].angle, 90, paso=-2, retraso=0.05)

def mover_brazo_derecho_adelante():
    angulo_inicial_hombro = mover.servo[HOMBROD].angle
    angulo_final_hombro = 70
    angulo_final_codo = 60

    for angulo in range(angulo_inicial_hombro, angulo_final_hombro, 2):
        mover.servo[HOMBROD].angle = angulo
        if angulo >= (angulo_inicial_hombro + angulo_final_hombro) / 2:
            mover_servo_suavemente(CODOD, mover.servo[CODOD].angle, angulo_final_codo, paso=2, retraso=0.05)
        time.sleep(0.05)
    
    mover.servo[HOMBROD].angle = angulo_final_hombro
    mover_servo_suavemente(CODOD, mover.servo[CODOD].angle, angulo_final_codo, paso=2, retraso=0.05)

def mover_brazo_izquierdo_adelante():
    angulo_inicial_hombro = mover.servo[HOMBROI].angle
    angulo_final_hombro = 70
    angulo_final_codo = 60

    for angulo in range(angulo_inicial_hombro, angulo_final_hombro, 2):
        mover.servo[HOMBROI].angle = angulo
        if angulo >= (angulo_inicial_hombro + angulo_final_hombro) / 2:
            mover_servo_suavemente(CODOI, mover.servo[CODOI].angle, angulo_final_codo, paso=2, retraso=0.05)
        time.sleep(0.05)
    
    mover.servo[HOMBROI].angle = angulo_final_hombro
    mover_servo_suavemente(CODOI, mover.servo[CODOI].angle, angulo_final_codo, paso=2, retraso=0.05)

def mover_brazo_derecho_atras():
    angulo_inicial_hombro = mover.servo[HOMBROD].angle
    angulo_final_hombro = 90
    angulo_final_codo = 90

    for angulo in range(angulo_inicial_hombro, angulo_final_hombro, 2):
        mover.servo[HOMBROD].angle = angulo
        if angulo <= (angulo_inicial_hombro + angulo_final_hombro) / 2:
            mover_servo_suavemente(CODOD, mover.servo[CODOD].angle, angulo_final_codo, paso=-2, retraso=0.05)
        time.sleep(0.05)
    
    mover.servo[HOMBROD].angle = angulo_final_hombro
    mover_servo_suavemente(CODOD, mover.servo[CODOD].angle, angulo_final_codo, paso=-2, retraso=0.05)

def mover_brazo_izquierdo_atras():
    angulo_inicial_hombro = mover.servo[HOMBROI].angle
    angulo_final_hombro = 90
    angulo_final_codo = 90

    for angulo in range(angulo_inicial_hombro, angulo_final_hombro, 2):
        mover.servo[HOMBROI].angle = angulo
        if angulo <= (angulo_inicial_hombro + angulo_final_hombro) / 2:
            mover_servo_suavemente(CODOI, mover.servo[CODOI].angle, angulo_final_codo, paso=-2, retraso=0.05)
        time.sleep(0.05)
    
    mover.servo[HOMBROI].angle = angulo_final_hombro
    mover_servo_suavemente(CODOI, mover.servo[CODOI].angle, angulo_final_codo, paso=-2, retraso=0.05)

def caminar_y_mover_brazos():
    configuracion_inicio()
    
    for _ in range(2):  # Número de ciclos para caminar
        # Mover pierna derecha hacia adelante
        mover_pierna_derecha_adelante()
        mover_pierna_izquierda_atras()
        mover_pierna_derecha_atras()
        mover_pierna_izquierda_adelante()

        # Mover brazos adelante
        mover_brazo_derecho_adelante()
        mover_brazo_izquierdo_adelante()

        # Mover pierna izquierda hacia adelante
        mover_pierna_izquierda_adelante()
        mover_pierna_derecha_atras()
        mover_pierna_izquierda_atras()
        mover_pierna_derecha_adelante()

        # Mover brazos atrás
        mover_brazo_derecho_atras()
        mover_brazo_izquierdo_atras()

# Llamar a la función para iniciar la animación
caminar_y_mover_brazos()
