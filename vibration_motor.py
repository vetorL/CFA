import machine
import time

# Set the GPIO pin for PWM control
motor_pin = machine.Pin(5, machine.Pin.OUT)  # You can change the GPIO number

# Create PWM object
pwm = machine.PWM(motor_pin)

# Set PWM frequency (motor can typically run between 500Hz to 2kHz)
pwm.freq(1000)  # 1 kHz frequency

# Set PWM duty cycle (range 0-1023)
# 0 is off, 1023 is full speed
def set_motor_speed(speed):
    pwm.duty(speed)

try:
    while True:
        # Turn the motor on at full speed
        print("Motor on")
        set_motor_speed(1023)
        time.sleep(2)

        # Turn the motor off
        print("Motor off")
        set_motor_speed(0)
        time.sleep(2)

except KeyboardInterrupt:
    pwm.deinit()  # Stop PWM when exiting
    print("Program stopped")
