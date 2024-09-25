import time
from adafruit_servokit import ServoKit

# Inicializar el controlador de servos
mover = ServoKit(channels=16)

# Mapeo de índices de servos a nombres
servo_names = {
    0: 'CODOI',  # 0
    1: 'BRAZOI',  # 1
    2: 'HOMBROI',  # 2
    3: 'CADERAI',  # 3
    4: 'PIERNAI',  # 4
    5: 'RODILLAI',  # 5
    6: 'TOBILLOI',  # 6
    7: 'PIEI',  # 7
    8: 'PIED',  # 8
    9: 'TOBILLOD',  # 9
    10: 'RODILLAD',  # 10
    11: 'PIERNAD',  # 11
    12: 'CADERAD',  # 12
    13: 'HOMBROD',  # 13
    14: 'BRAZOD',  # 14
    15: 'CODOD'  # 15
}

# Ángulos iniciales para cada servo
initial_angles = {
    0: 90,   # CODOI
    1: 110,  # BRAZOI
    2: 90,   # HOMBROI
    3: 100,  # CADERAI
    4: 100,  # PIERNAI
    5: 85,   # RODILLAI
    6: 85,   # TOBILLOI
    7: 90,   # PIEI
    8: 90,   # PIED
    9: 100,  # TOBILLOD
    10: 80,  # RODILLAD
    11: 90,  # PIERNAD
    12: 100,  # CADERAD
    13: 90,  # HOMBROD
    14: 90,  # BRAZOD
    15: 90   # CODOD
}

def set_servo_angle(servo_index, angle):
    """Configura el ángulo del servo en el índice dado"""
    if 0 <= angle <= 180:
        mover.servo[servo_index].angle = angle
        print(f"Servo en Canal {servo_index + 1} configurado a {angle} grados")
    else:
        print("Error: El ángulo debe estar entre 0 y 180 grados.")

def get_angle_from_user(servo_name):
    """Solicita al usuario el ángulo para un servo específico"""
    while True:
        try:
            angle = float(input(f"Ingrese el ángulo para el servo '{servo_name}' (0-180): "))
            if 0 <= angle <= 180:
                return angle
            else:
                print("Debe estar entre 0 y 180.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

def main():
    """Función principal para probar servos"""
    print("Sistema de Control de Servos")
    print("Los servos disponibles son:")
    for num, name in servo_names.items():
        print(f"{num + 1}: {name}")

    # Configurar los servos a sus ángulos iniciales
    for num, angle in initial_angles.items():
        set_servo_angle(num, angle)  # Usar índice desde 0
    
    while True:
        try:
            # Entrada del usuario para la selección de servos
            servo_numbers = input("Ingrese los números de hasta seis servos que desea controlar (separados por comas) o '99' para terminar: ")
            if servo_numbers == '99':
                print("Devolviendo los servos a sus posiciones iniciales...")
                # Devolver todos los servos a sus posiciones iniciales
                for num, angle in initial_angles.items():
                    set_servo_angle(num, angle)
                print("Terminando el programa.")
                break

            # Procesar la entrada del usuario
            servo_numbers = [int(num.strip()) for num in servo_numbers.split(',')]

            # Validar los números de servos
            if len(servo_numbers) > 6:
                print("Error: Solo puedes seleccionar hasta seis servos.")
                continue
            
            if not all(0 <= num <= 15 for num in servo_numbers):  # Ajustar validación para índices desde 0
                print("Error: Todos los números de servo deben estar entre 0 y 15.")
                continue

            # Eliminar duplicados y ordenarlos
            servo_numbers = sorted(set(servo_numbers))

            angles = []
            for num in servo_numbers:
                servo_name = servo_names[num]  # Usar índice desde 0
                angle = get_angle_from_user(servo_name)
                angles.append((num, angle))
            
            # Configurar los servos
            for index, angle in angles:
                set_servo_angle(index, angle)
        
        except ValueError:
            print("Por favor, ingrese números válidos.")

if __name__ == "__main__":
    main()
