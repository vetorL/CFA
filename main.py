from vibration_motor import VibrationMotor
from LDR import LDR
from touch import touch
from UV import UV
from dados import Dados
import time


class SolarCap:
    
    def __init__(self):
        
        # inicializa o motor de vibração
        self.vibration_motor = VibrationMotor(5)

        # inicializa o LDR
        self.ldr = LDR(32)
        
        # inicializa o touch
        self.touch = touch(18)

        # inicializa o sensor de UV
        self.UV_sensor = UV(34)
        
        # Lista com os últimos 900 valores (equivalente aos últimos 15 minutos)
        self.dados = Dados(900)

    
    def start(self):
        
        try:
            # Main loop do código
            while True:
                
                # Caso os dados tenham uma média maior que 90, ligar o motor de vibração até que ele
                # seja manualmente desligado pelo usuário
                if self.dados.getAverage() > 90:
                    self.vibration_motor.on()
                else:
                    self.vibration_motor.off()
                    
                # Caso o usuário aperte o botão touch, resetar Dados (consequentemente desligará o motor caso esteja ligado)
                if self.touch.is_touching() == True:
                    self.dados.reset()
                
                # Ajusta os LEDs do LDR conforme o valor atual da luminosidade
                self.ldr.adjust_LEDs()
                
                # Adiciona dados de luminosidade da iteração atual em Dados
                self.dados.add(self.ldr.value())
                
                print(self.dados.getAverage())
                
                # timer de 1 segundo entre iterações do loop
                time.sleep(1)

        except KeyboardInterrupt:
            self.vibration_motor.pwm.deinit()  # Stop PWM when exiting
            self.ldr.turnoff()
            print("Program stopped")


solarCap = SolarCap()

solarCap.start()
