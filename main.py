from vibration_motor import VibrationMotor
from LDR import LDR
from touch import touch
from UV import UV
import time


class SolarCap:
    
    def __init__(self):
        
        # inicializa o motor de vibração
        self.vibration_motor = VibrationMotor(5)

        # inicializa o LDR
        self.ldr = LDR(32)
        
        # inicializa o touch
        self.touch(18)

        # inicializa o sensor de UV
        self.UV_sensor = UV(34)

    
    def start(self):
        
        try:
            # Main loop do código
            while True:
                # adicinar para ativar um timer quando a media do LDR > 95 && media do UV > 5
                if self.ldr.value() == 100:
                    # Liga o motor de vibração
                    self.vibration_motor.on()    
                else:
                    # Desliga o motor de vibração
                    self.vibration_motor.off()
                
                self.ldr.mostrar_luminosidade()
                self.ldr.adjust_LEDs()
                
                time.sleep(1)
                
                if(self.touch.is_touching() == True):
                    self.vibration_motor.pwm.deinit()

        except KeyboardInterrupt:
            self.vibration_motor.pwm.deinit()  # Stop PWM when exiting
            self.ldr.turnoff()
            print("Program stopped")


solarCap = SolarCap()

solarCap.start()
