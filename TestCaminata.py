import time
from adafruit_servokit import ServoKit

# Inicializa el controlador de servos con 16 canales
kit = ServoKit(channels=16)

# Valores iniciales, máximos y mínimos para los servos
valores_iniciales = {
    4: 90, 5: 90, 6: 90, 7: 90, 8: 90, 12: 90, 13: 90, 14: 90, 15: 90, 16: 90
}

valores_maximos = {
    4: 140, 5: 160, 6: 170, 7: 160, 8: 140, 12: 160, 13: 170, 14: 160, 15: 140, 16: 140
}

valores_minimos = {
    4: 40, 5: 20, 6: 10, 7: 20, 8: 40, 12: 20, 13: 10, 14: 20, 15: 40, 16: 40
}

# Inicializa todos los servos en sus posiciones iniciales
for servo_id in valores_iniciales:
    kit.servo[servo_id].angle = valores_iniciales[servo_id]

# Función para mover un servo a través de un rango
def mover_servo(servo_id, min_valor, max_valor, duracion):
    inicio = time.time()
    while True:
        tiempo_transcurrido = time.time() - inicio
        nuevo_angulo = min_valor + (max_valor - min_valor) * (tiempo_transcurrido / duracion)
        if nuevo_angulo > max_valor:
            nuevo_angulo = max_valor
        kit.servo[servo_id].angle = nuevo_angulo
        if nuevo_angulo == max_valor:
            break
        time.sleep(0.01)

# Función para mover un servo de regreso a la posición inicial
def mover_servo_a_inicial(servo_id, duracion):
    inicio = time.time()
    angulo_inicial = valores_iniciales[servo_id]
    while True:
        tiempo_transcurrido = time.time() - inicio
        nuevo_angulo = angulo_inicial - (angulo_inicial - valores_minimos[servo_id]) * (tiempo_transcurrido / duracion)
        if nuevo_angulo < valores_minimos[servo_id]:
            nuevo_angulo = valores_minimos[servo_id]
        kit.servo[servo_id].angle = nuevo_angulo
        if nuevo_angulo == valores_minimos[servo_id]:
            break
        time.sleep(0.01)

# Función para verificar si el servo está en el rango de activación
def servo_en_rango(servo_id, rango_inferior, rango_superior):
    angulo_actual = kit.servo[servo_id].angle
    return rango_inferior <= angulo_actual <= rango_superior

# Función para animar los servos en reacción en cadena
def animacion_bipedo():
    duracion_total = 5  # Duración total para llegar al valor máximo en segundos
    duracion_regreso = 3  # Duración para regresar a la posición inicial en segundos
    rango_inicio = valores_iniciales[4] - 20
    rango_final = valores_iniciales[4] + 20

    # Mueve el primer servo (4) al valor máximo
    mover_servo(4, valores_minimos[4], valores_maximos[4], duracion_total)
    
    # Inicia el movimiento de los otros servos cuando el primer servo esté en el rango especificado
    inicio = time.time()
    servos = [5, 6, 7, 8, 12, 13, 14, 15, 16]
    servos_iniciados = False
    while True:
        if servo_en_rango(4, rango_inicio, rango_final) and not servos_iniciados:
            # Mueve cada servo en forma inversamente proporcional
            for servo_id in servos:
                mover_servo(servo_id, valores_minimos[servo_id], valores_maximos[servo_id], duracion_total)
            servos_iniciados = True
        if not servo_en_rango(4, rango_inicio, rango_final) and servos_iniciados:
            # Asegúrate de que todos los servos regresen a su posición inicial
            for servo_id in servos:
                mover_servo_a_inicial(servo_id, duracion_regreso)
            break
        time.sleep(0.01)

    # Continúa el primer servo hacia el valor mínimo
    mover_servo(4, valores_maximos[4], valores_minimos[4], duracion_total)
    
    # Asegúrate de que todos los servos regresen a su posición inicial
    for servo_id in servos:
        mover_servo_a_inicial(servo_id, duracion_regreso)

# Ejecuta la animación
animacion_bipedo()
