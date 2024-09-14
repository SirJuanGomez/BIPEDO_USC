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

# Mapeo de nombres de servos a sus canales
servidores = {
    "MANOD": MANOD,
    "CODOD": CODOD,
    "HOMBROD": HOMBROD,
    "CADERAD": CADERAD,
    "MUSLOD": MUSLOD,
    "RODILLAD": RODILLAD,
    "TOBILLOD": TOBILLOD,
    "PIED": PIED,
    "MANOI": MANOI,
    "CODOI": CODOI,
    "HOMBROI": HOMBROI,
    "CADERAI": CADERAI,
    "MUSLOI": MUSLOI,
    "RODILLAI": RODILLAI,
    "TOBILLOI": TOBILLOI,
    "PIEI": PIEI
}

# Configura los servos con sus ángulos iniciales
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

    print("Posiciones iniciales establecidas en 90 grados.")

# Ajusta el ángulo de los servos seleccionados
def ajustar_servos(servos_ajustar):
    for nombre, (canal, angulo) in servos_ajustar.items():
        mover.servo[canal].angle = angulo
    print("Ángulos ajustados.")

def main():
    # Configurar servos a posiciones iniciales
    configuracion_inicio()
    
    # Iniciar el ajuste de servos
    while True:
        try:
            # Leer la entrada del usuario
            num_servos = int(input("Ingrese el número de servos a ajustar (1-6): "))
            if num_servos < 1 or num_servos > 6:
                print("Número inválido. Debe estar entre 1 y 6.")
                continue
            
            servos_ajustar = {}
            
            for i in range(num_servos):
                nombre = input(f"Ingrese el nombre del servo {i + 1} (por ejemplo, 'MANOD', 'CODOD', etc.): ").strip().upper()
                if nombre not in servidores:
                    print("Nombre de servo inválido. Debe ser uno de los nombres definidos.")
                    continue
                
                angulo = float(input(f"Ingrese el ángulo para el servo {nombre} (0-180): "))
                if angulo < 0 or angulo > 180:
                    print("Ángulo inválido. Debe estar entre 0 y 180 grados.")
                    continue
                
                canal = servidores[nombre]
                servos_ajustar[nombre] = (canal, angulo)
            
            # Ajustar los servos seleccionados
            ajustar_servos(servos_ajustar)
        
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")
        
        # Preguntar si desea continuar
        continuar = input("¿Desea ajustar más servos? (s/n): ").strip().lower()
        if continuar != 's':
            break
    
    print("Finalizando el programa.")

# Ejecutar el programa
main()
