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
    2: 150, # Ajustado según tu configuración
    10: 175
}

valores_minimos = {
    2: 25, # Ajustado según tu configuración
    10: 25
}

# Inicializa todos los servos en sus posiciones iniciales
for servo_id, angulo in valores_iniciales.items():
    kit.servo[servo_id].angle = angulo

# Función para mover un servo a través de un rango de manera suave
def mover_servo(servo_id, valor_inicial, valor_final, duracion):
    inicio = time.time()
    while True:
        tiempo_transcurrido = time.time() - inicio
        nuevo_angulo = valor_inicial + (valor_final - valor_inicial) * (tiempo_transcurrido / duracion)
        if valor_final > valor_inicial and nuevo_angulo > valor_final:
            nuevo_angulo = valor_final
        elif valor_final < valor_inicial and nuevo_angulo < valor_final:
            nuevo_angulo = valor_final
        kit.servo[servo_id].angle = nuevo_angulo
        if nuevo_angulo == valor_final:
            break
        time.sleep(0.01)

# Función para mover los servos de regreso a sus ángulos iniciales de manera suave
def mover_servo_a_inicial(servo_id, duracion):
    mover_servo(servo_id, kit.servo[servo_id].angle, valores_iniciales[servo_id], duracion)

# Función principal que ejecuta el movimiento en bucle
def reaccion_en_cadena():
    duracion_total = 5  # Duración total para llegar al valor máximo en segundos
    duracion_regreso = 5  # Duración para regresar a la posición inicial en segundos

    while True:
        # Mueve ambos servos al valor máximo
        inicio = time.time()
        while True:
            tiempo_transcurrido = time.time() - inicio
            if tiempo_transcurrido > duracion_total:
                break
            mover_servo(2, valores_minimos[2], valores_maximos[2], tiempo_transcurrido)
            mover_servo(10, valores_minimos[10], valores_maximos[10], tiempo_transcurrido)
            time.sleep(0.01)

        # Regresa ambos servos a sus ángulos iniciales de manera suave
        mover_servo_a_inicial(2, duracion_regreso)
        mover_servo_a_inicial(10, duracion_regreso)

# Ejecuta la reacción en cadena
reaccion_en_cadena()
