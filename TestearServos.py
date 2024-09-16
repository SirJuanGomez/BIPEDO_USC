import time
from adafruit_servokit import ServoKit

# Inicializa el controlador de servos con 16 canales
kit = ServoKit(channels=16)

# Valores iniciales para los servos
valores_iniciales = {
    0: 90, 1: 90, 2: 90, 3: 97.5, 4: 90, 5: 90,
    6: 90, 7: 90, 8: 90, 9: 90, 10: 90, 11: 97.5,
    12: 90, 13: 90, 14: 90, 15: 90
}

# Configura los servos con sus ángulos iniciales
def configuracion_inicio():
    for canal, angulo in valores_iniciales.items():
        kit.servo[canal].angle = angulo
    print("Posiciones iniciales establecidas.")

# Ajusta el ángulo de los servos seleccionados
def ajustar_servos(servos_ajustar):
    for canal, angulo in servos_ajustar.items():
        kit.servo[canal].angle = angulo
    print("Ángulos ajustados.")

def mostrar_lista_servos():
    print("Lista de servos disponibles:")
    for canal in range(16):
        print(f"Canal {canal} - Ángulo actual: {valores_iniciales.get(canal, 90)}")

def main():
    # Configurar servos a posiciones iniciales
    configuracion_inicio()
    
    while True:
        try:
            # Mostrar lista de servos disponibles
            mostrar_lista_servos()
            
            # Leer la entrada del usuario para el número de servos a ajustar
            num_servos = int(input("Ingrese el número de servos a ajustar (1-6): "))
            if num_servos < 1 or num_servos > 6:
                print("Número inválido. Debe estar entre 1 y 6.")
                continue
            
            servos_ajustar = {}
            
            for i in range(num_servos):
                canal = int(input(f"Ingrese el número del canal del servo {i + 1} (0-15): "))
                if canal < 0 or canal > 15:
                    print("Número de canal inválido. Debe estar entre 0 y 15.")
                    continue
                
                angulo = float(input(f"Ingrese el ángulo para el servo en el canal {canal} (0-180): "))
                if angulo < 0 or angulo > 180:
                    print("Ángulo inválido. Debe estar entre 0 y 180 grados.")
                    continue
                
                servos_ajustar[canal] = angulo
            
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
if __name__ == "__main__":
    main()
