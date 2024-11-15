from vibration_motor import VibrationMotor
from LDR import LDR
import time


class SolarCap:
    
    def __init__(self):
        
        # inicializa o motor de vibração
        self.vibration_motor = VibrationMotor(5)

        # inicializa o LDR
        self.ldr = LDR(32)
        
    def start(self):
        
        try:
            # Main loop do código
            while True:
                
                if self.ldr.value() == 100:
                    # Liga o motor de vibração
                    self.vibration_motor.on()    
                else:
                    # Desliga o motor de vibração
                    self.vibration_motor.off()
                
                self.ldr.mostrar_luminosidade()
                self.ldr.adjust_LEDs()
                
                time.sleep(1)

        except KeyboardInterrupt:
            self.vibration_motor.pwm.deinit()  # Stop PWM when exiting
            print("Program stopped")

solarCap = SolarCap()

solarCap.start()