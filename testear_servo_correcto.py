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
    #####################################
    3: 110, #4
    #####################################
    4: 140, #5
    5: 130, #6
    #####################################
    6: 140, #7
    7: 120, #8

    #Lado Izquierdo
    8: 90, #9
    9: 150, #10
    10: 175, #11
    ###############################
    11: 155, #12
    ###############################
    12: 140, #13
    13: 130, #14
    ###############################
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

# Función para verificar el rango de un servo
def servo_en_rango(servo_id, rango_inferior, rango_superior):
    angulo_actual = kit.servo[servo_id].angle
    return rango_inferior <= angulo_actual <= rango_superior

# Función para mover el servo a una posición específica y esperar confirmación
def mover_y_confirmar(servo_id, angulo, mensaje_confirmacion):
    print(f"Moviendo el servo {servo_id} a {angulo} grados.")
    kit.servo[servo_id].angle = angulo
    input(mensaje_confirmacion)

# Función para ejecutar la reacción en cadena
def reaccion_en_cadena():
    duracion_total = 5  # Duración total para llegar al valor máximo en segundos
    duracion_regreso = 5  # Duración para regresar a la posición inicial en segundos

    # Verifica el movimiento de los servos 2 y 10
    servos_a_verificar = [2, 10]  # Lista de servos que deben ser verificados
    angulos_a_verificar = {2: 90, 10: 90}  # Ángulos a los que deben ser movidos

    for servo_id in servos_a_verificar:
        mover_y_confirmar(servo_id, angulos_a_verificar[servo_id],
                          f"Confirme que el servo {servo_id} se movió a {angulos_a_verificar[servo_id]} grados (presione Enter para continuar).")

    # Mueve los servos 2 y 10 al valor máximo
    inicio = time.time()
    duracion_maximo = duracion_total  # Duración para mover al valor máximo
    while True:
        tiempo_transcurrido = time.time() - inicio
        if tiempo_transcurrido > duracion_maximo:
            break
        kit.servo[2].angle = valores_minimos[2] + (valores_maximos[2] - valores_minimos[2]) * (tiempo_transcurrido / duracion_maximo)
        kit.servo[10].angle = valores_minimos[10] + (valores_maximos[10] - valores_minimos[10]) * (tiempo_transcurrido / duracion_maximo)
        time.sleep(0.01)

    # Regresa los servos 2 y 10 a sus ángulos iniciales de forma suave
    mover_servo(2, valores_maximos[2], valores_iniciales[2], duracion_regreso)
    mover_servo(10, valores_maximos[10], valores_iniciales[10], duracion_regreso)

# Ejecuta la reacción en cadena
reaccion_en_cadena()
