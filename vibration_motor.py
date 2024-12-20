from machine import Pin, PWM
import time

class VibrationMotor:
    
    def __init__(self, pin):
        
        # Set the GPIO pin for PWM control
        self.motor_pin = Pin(pin, Pin.OUT) # You can change the GPIO number

        # Create PWM object
        self.pwm = PWM(self.motor_pin)

        # Set PWM frequency (motor can typically run between 500Hz to 2kHz)
        self.pwm.freq(1000)  # 1 kHz frequency

    # Set PWM duty cycle (range 0-1023)
    # 0 is off, 1023 is full speed
    def set_motor_speed(self, speed):
        self.pwm.duty(speed)
       
    # Turn the motor on at full speed
    def on(self):
        print("Motor on")
        self.set_motor_speed(1023)
        
    # Turn the motor off
    def off(self):
        print("Motor off")
        self.set_motor_speed(0)

    # Faz o motor vibrar por 3 segundos
    def warn(self):
        self.on()
        time.sleep(3)
        self.off()
