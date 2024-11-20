from machine import Pin

class touch:
    def __init__(self, SENSOR_PIN):
        self.sensor = Pin(SENSOR_PIN, Pin.IN)
        
    def is_touching(self):
        self.state = sensor.value()
        if(state == 1):
            return True
        else:
            return False
