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
    mover.servo[HOMBROD].angle = 180
    mover.servo[CODOD].angle = 90
    mover.servo[HOMBROD].angle = 180
    mover.servo[CADERAD].angle = 110
    mover.servo[PIED].angle = 90
    mover.servo[RODILLAD].angle = 90
    mover.servo[TOBILLOD].angle = 90
    mover.servo[PIED].angle = 72
    
    # SERVOS LADO IZQUIERDO
    mover.servo[MANOI].angle = 90
    mover.servo[CODOI].angle = 90
    mover.servo[HOMBROI].angle = 90
    mover.servo[CADERAI].angle = 90
    mover.servo[PIEI].angle = 90
    mover.servo[RODILLAI].angle = 90
    mover.servo[TOBILLOI].angle = 90
    mover.servo[PIEI].angle = 90

def mover_pied_adelante():
    angulo_inicial_pied = mover.servo[PIED].angle
    angulo_final_pied = 65  # Ángulo objetivo para el pie

    # Mueve el pie hacia adelante de manera suave
    mover_servo_suavemente(PIED, angulo_inicial_pied, angulo_final_pied, paso=2, retraso=0.05)
    
    # Calcula el ángulo del 10% de la pierna
    angulo_inicial_pierna = mover.servo[PIERNAD].angle
    angulo_10_por_ciento = angulo_inicial_pierna * 0.10
    angulo_final_pierna = angulo_inicial_pierna - 65  # Ángulo final para la pierna

    # Mueve la pierna hacia adelante suavemente hasta el 10% de su ángulo inicial
    mover_servo_suavemente(PIERNAD, angulo_inicial_pierna, angulo_10_por_ciento, paso=2, retraso=0.05)
    
    # Espera a que la pierna alcance el 10% antes de continuar
    while mover.servo[PIERNAD].angle > angulo_10_por_ciento:
        time.sleep(0.01)  # Espera breve para evitar un bucle demasiado rápido
    
    # Continúa el movimiento del pie y la pierna
    mover_servo_suavemente(PIERNAD, angulo_10_por_ciento, angulo_final_pierna, paso=2, retraso=0.05)
    mover_servo_suavemente(PIED, angulo_final_pied, 90, paso=2, retraso=0.05)

def mover_piei_adelante():
    angulo_inicial_piei = mover.servo[PIEI].angle
    angulo_final_piei = 90  # Ángulo objetivo para el pie izquierdo

    # Mueve el pie izquierdo hacia adelante de manera suave
    mover_servo_suavemente(PIEI, angulo_inicial_piei, angulo_final_piei, paso=2, retraso=0.05)
    
    # Calcula el ángulo del 10% de la pierna
    angulo_inicial_pierna = mover.servo[PIERNAI].angle
    angulo_10_por_ciento = angulo_inicial_pierna * 0.10
    angulo_final_pierna = angulo_inicial_pierna - 65  # Ángulo final para la pierna

    # Mueve la pierna izquierda hacia adelante suavemente hasta el 10% de su ángulo inicial
    mover_servo_suavemente(PIERNAI, angulo_inicial_pierna, angulo_10_por_ciento, paso=2, retraso=0.05)
    
    # Espera a que la pierna alcance el 10% antes de continuar
    while mover.servo[PIERNAI].angle > angulo_10_por_ciento:
        time.sleep(0.01)  # Espera breve para evitar un bucle demasiado rápido
    
    # Continúa el movimiento del pie y la pierna
    mover_servo_suavemente(PIERNAI, angulo_10_por_ciento, angulo_final_pierna, paso=2, retraso=0.05)
    mover_servo_suavemente(PIEI, angulo_final_piei, 90, paso=2, retraso=0.05)

def inclinar_pied120_fuera():
    mover_servo_suavemente(PIERNAD, mover.servo[PIERNAD].angle, 90, paso=2, retraso=0.05)
    mover_servo_suavemente(RODILLAD, mover.servo[RODILLAD].angle, 90, paso=2, retraso=0.05)
    mover_servo_suavemente(PIED, mover.servo[PIED].angle, 105, paso=2, retraso=0.05)
    mover_servo_suavemente(PIEI, mover.servo[PIEI].angle, 105, paso=2, retraso=0.05)

def inclinar_piei120_fuera():
    mover_servo_suavemente(PIERNAI, mover.servo[PIERNAI].angle, 90, paso=2, retraso=0.05)
    mover_servo_suavemente(RODILLAI, mover.servo[RODILLAI].angle, 90, paso=2, retraso=0.05)
    mover_servo_suavemente(PIEI, mover.servo[PIEI].angle, 75, paso=2, retraso=0.05)
    mover_servo_suavemente(PIED, mover.servo[PIED].angle, 75, paso=2, retraso=0.05)

def mover_pied_atras():
    angulo_inicial_pied = mover.servo[PIED].angle
    angulo_final_pied = 120  # Ángulo objetivo para el pie

    # Mueve el pie hacia atrás de manera suave
    mover_servo_suavemente(PIED, angulo_inicial_pied, angulo_final_pied, paso=2, retraso=0.05)
    
    # Calcula el ángulo del 10% de la pierna
    angulo_inicial_pierna = mover.servo[PIERNAD].angle
    angulo_10_por_ciento = angulo_inicial_pierna * 0.10
    angulo_final_pierna = angulo_inicial_pierna + 65  # Ángulo final para la pierna

    # Mueve la pierna hacia atrás suavemente hasta el 10% de su ángulo inicial
    mover_servo_suavemente(PIERNAD, angulo_inicial_pierna, angulo_10_por_ciento, paso=2, retraso=0.05)
    
    # Espera a que la pierna alcance el 10% antes de continuar
    while mover.servo[PIERNAD].angle < angulo_10_por_ciento:
        time.sleep(0.01)  # Espera breve para evitar un bucle demasiado rápido
    
    # Continúa el movimiento del pie y la pierna
    mover_servo_suavemente(PIERNAD, angulo_10_por_ciento, angulo_final_pierna, paso=2, retraso=0.05)
    mover_servo_suavemente(PIED, angulo_final_pied, 90, paso=2, retraso=0.05)

def caminar_frente():
    inclinar_piei120_fuera()
    mover_pied_adelante()
    mover_piei_centro90()
    inclinar_pied120_fuera()
    mover_piei_adelante()
    mover_pied_centro90()

def mover_piei_centro90():
    mover_servo_suavemente(PIEI, mover.servo[PIEI].angle, 90, paso=2, retraso=0.05)

def mover_pied_centro90():
    mover_servo_suavemente(PIED, mover.servo[PIED].angle, 90, paso=2, retraso=0.05)

# Llama a la función de configuración al iniciar el programa
configuracion_inicio()

# Ejecuta el ciclo de caminar
while True:
    caminar_frente()
    time.sleep(1)  # Espera entre pasos para evitar que el ciclo sea demasiado rápido
