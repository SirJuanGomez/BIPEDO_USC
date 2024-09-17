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
    #Lado Derecho
    0: 170, #1
    1: 160, #2
    2: 150, #3
    ####################################
    3: 110, #4
    ################################
    4: 140, #5
    5: 130, #6
    #################################
    6: 140, #7
    7: 120, #8

    #Lado Izquierdo
    8: 90, #9
    9: 150, #10
    10: 175, #11
    ###############################
    11: 155, #12
    #############################
    12: 140, #13
    13: 130, #14
    ##############################
    14: 180, #15
    15: 120 #16
}

valores_minimos = {
    #Lado Derecho
    0: 90, #1
    1: 45, #2
    2: 25, #3
    ############################
    3: 25, #4
    ##########################
    4: 30, #5
    5: 40, #6
    #######################
    6: 40, #7
    7: 45, #8

    #Lado Izquierdo
    8: 25, #9
    9: 25, #10
    10: 25, #11
    ###############################
    11: 80, #12
    ###############################
    12: 30, #13
    13: 40, #14
    ###################################
    14: 65, #15
    15: 45 #16
}

# Inicializa todos los servos en sus posiciones iniciales
for servo_id, angulo in valores_iniciales.items():
    kit.servo[servo_id].angle = angulo

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

# Función para verificar el rango de un servo
def servo_en_rango(servo_id, rango_inferior, rango_superior):
    angulo_actual = kit.servo[servo_id].angle
    return rango_inferior <= angulo_actual <= rango_superior

# Función para ejecutar la reacción en cadena
def reaccion_en_cadena():
    duracion_total = 5  # Duración total para llegar al valor máximo en segundos
    duracion_regreso = 3  # Duración para regresar a la posición inicial en segundos
    rango_inicio = valores_iniciales[0] - 20
    rango_final = valores_iniciales[0] + 20

    # Mueve el primer servo al valor máximo
    mover_servo(3, valores_minimos[3], valores_maximos[3], duracion_total)
    
    # Inicia el movimiento del segundo servo cuando el primer servo esté en el rango especificado
    inicio = time.time()
    segundo_servo_comenzado = False
    while True:
        if servo_en_rango(3, rango_inicio, rango_final) and not segundo_servo_comenzado:
            mover_servo(1, valores_minimos[1], valores_maximos[1], duracion_total)
            segundo_servo_comenzado = True
        if not servo_en_rango(3, rango_inicio, rango_final) and segundo_servo_comenzado:
            mover_servo_a_inicial(1, duracion_regreso)
            break
        time.sleep(0.01)

    # Continúa el primer servo hacia el valor mínimo
    mover_servo(3, valores_maximos[3], valores_minimos[3], duracion_total)
    
    # Asegúrate de que el segundo servo regrese a su posición inicial antes de finalizar
    mover_servo_a_inicial(1, duracion_regreso)

# Ejecuta la reacción en cadena
reaccion_en_cadena()
