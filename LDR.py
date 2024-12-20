from machine import ADC, Pin
import time


class LDR:
    """This class read a value from a light dependent resistor (LDR)"""

    def __init__(self, pin, min_value=0, max_value=100):
        """
        Initializes a new instance.
        :parameter pin A pin that's connected to an LDR.
        :parameter min_value A min value that can be returned by value() method.
        :parameter max_value A max value that can be returned by value() method.
        """

        if min_value >= max_value:
            raise Exception("Min value is greater or equal to max value")

        # initialize ADC (analog to digital conversion)
        self.adc = ADC(Pin(pin))

        # set 11dB input attenuation (voltage range roughly 0.0v - 3.6v)
        self.adc.atten(ADC.ATTN_11DB)

        self.min_value = min_value
        self.max_value = max_value
        
        # pinos dos leds
        self.led1 = Pin(13, Pin.OUT)
        self.led2 = Pin(12, Pin.OUT)
        self.led3 = Pin(14, Pin.OUT)

    def read(self):
        """
        Read a raw value from the LDR.
        :return A value from 0 to 4095.
        """
        return self.adc.read()

    def value(self):
        """
        Read a value from the LDR in the specified range.
        :return A value from the specified [min, max] range.
        """
        return (self.max_value - self.min_value) * self.read() / 4095
    
    def adjust_LEDs(self):
        # faz o led acender de acordo com a luminosidade
        if self.value() >= 50:
            self.led1.value(1)
        else:
            self.led1.value(0)
            
        if self.value() >= 80:
            self.led2.value(1)
        else:
            self.led2.value(0)
        
        if self.value() == 100:
            self.led3.value(1)
        else:
            self.led3.value(0)
            
    def mostrar_luminosidade(self):
        print("luminosidade = " + str(self.value()))
        
    def turnoff(self):
        self.led1.value(0)
        self.led2.value(0)
        self.led3.value(0)
              
