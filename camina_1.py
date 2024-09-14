import time
from adafruit_servokit import ServoKit

mover = ServoKit(channels=16)

#CONSTANTES
MANOD=0
CODOD=1
HOMBROD=2
CADERAD=3
MUSLOD=4
RODILLAD=5
TOBILLOD=6
PIED=7
MANOI=8
CODOI=9
HOMBROI=10
CADERAI=11
MUSLOI=12
RODILLAI=13
TOBILLOI=14
PIEI=15

#CONSTANTES DE TIEMPO EN MILISEGUNDOS
TEMPO500 = 500

class Humanoide():
    def __init__(self):
        pass
        
    def configuracion_inicio():
        #SERVOS LADO DERECHO
        mover.servo[HOMBROD].angle = 180
        mover.servo[CODOD].angle = 90
        mover.servo[HOMBROD].angle = 180
        mover.servo[CADERAD].angle = 110
        mover.servo[PIERNAD].angle = 90
        mover.servo[RODILLAD].angle = 90
        mover.servo[TOBILLOD].angle = 90
        mover.servo[PIED].angle = 72
        
        #SERVOS LADO IZQUIERDO
        mover.servo[MANOI].angle = 90
        mover.servo[CODOI].angle = 90
        mover.servo[HOMBROI].angle = 90
        mover.servo[CADERAI].angle = 90
        mover.servo[PIERDAI].angle = 90
        mover.servo[RODILLAI].angle = 90
        mover.servo[TOBILLOI].angle = 90
        mover.servo[PIEI].angle = 90
    
    
    def caminar_frente():
        inclinar_piei120_fuera()
        mover_pied_adelante()
        mover_piei_centro90()
        inclinar_pied120_fuera()
        mover_piei_adelante()
        mover_pied_centro90()

    def agacharse():
        pass


    def mover_piei_centro90():
        mover.servo[PIEI].angle = 180
        time.sleep(TEMPO500)
        
        
    def mover_pied_centro90():
        mover.servo[PIED].angle = 90
        time.sleep(TEMPO500)
        

    def inclinar_pied120_fuera():
        mover.servo[PIERNAD].angle = 90
        mover.servo[RODILLAD].angle = 90
        mover.servo[PIED].angle = 105
        mover.servo[PIEI].angle = 105
        time.sleep(TEMPO500)
        

    def inclinar_piei120_fuera():
        mover.servo[PIERNAI].angle = 90
        mover.servo[RODILLAI].angle = 90
        mover.servo[PIEI].angle = 75
        mover.servo[PIED].angle = 75
        time.sleep(TEMPO500)


    def mover_piei_adelante():
        mover.servo[PIERNAI].angle = 65
        mover.servo[RODILLAI].angle = 70
        mover.servo[PIEI].angle = 90
        time.sleep(TEMPO500)
        
        
    def mover_pied_adelante():
        mover.servo[PIERNAD].angle = 65
        mover.servo[RODILLAD].angle = 110
        mover.servo[PIED].angle = 90
        time.sleep(TEMPO500)
        
        
    def mover_pied_atras():
        mover.servo[PIERNAD].angle = 120
        mover.servo[RODILLAD].angle = 80
        mover.servo[PIED].angle = 90
        time.sleep(TEMPO500)
        
        
    def mover_piei_atras():
        mover.servo[PIERNAI].angle = 120
        mover.servo[RODILLAI].angle = 110
        mover.servo[PIEI].angle = 90
        time.sleep(TEMPO500)
        
    
if __name__=='__main__':
    h = Humanoide()
    h.mover_piei_centro90()
    