from machine import ADC, Pin
import time

led = Pin(13, Pin.OUT)
led2 = Pin(12, Pin.OUT)
led3 = Pin(14, Pin.OUT)

# Configure the ADC pin (use GPIO34 or GPIO32, which are valid ADC pins)
UVsensorIn = ADC(Pin(34))  # Use GPIO34 or GPIO32 for ADC
UVsensorIn.atten(ADC.ATTN_11DB)  # Set the attenuation to 0-3.3V range
UVsensorIn.width(ADC.WIDTH_12BIT)  # Set the resolution to 12 bits (0-4095)

# Function to take an average of readings
def average_analog_read(pinToRead, num_readings=8):
    running_value = 0
    for _ in range(num_readings):
        running_value += pinToRead.read()  # Read the analog value
        time.sleep(0.05)  # Small delay between readings to reduce noise
    return running_value // num_readings  # Return the average

# Function to map a float value from one range to another
def mapfloat(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


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
            raise Exception('Min value is greater or equal to max value')

        # initialize ADC (analog to digital conversion)
        self.adc = ADC(Pin(pin))

        # set 11dB input attenuation (voltage range roughly 0.0v - 3.6v)
        self.adc.atten(ADC.ATTN_11DB)

        self.min_value = min_value
        self.max_value = max_value

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


# inicializa o LDR
ldr = LDR(32)

class DadosLuminosidadeUltimaHora:
    #Inicializa a classe
    def __init__(self):
        self.lista = []
        
    # Administra o tamanho da lista para garantir que não passe de 60 elementos
    def adicionar(self, valor):
        # Limita a lista a 60 valores
        if len(self.lista) < 60:
            self.lista.append(valor)
            
        # Caso em que a lista já tem mais de 60 entradas
        else:
            # Remove o primeiro elemento da lista
            self.lista.pop(0)
            
            # Adiciona um elemento na última posição da lista
            self.lista.append(valor)
    
    # Faz um print da lista na tela
    def mostrar(self):
        print(self.lista)

dadosLuminosidadeUltimaHora = DadosLuminosidadeUltimaHora()

while True:
    
    # Lista para o calculo da média da luminosidade do último minuto
    dadosUltimoMinuto = []
    
    for _ in range(60):
        
        uv_level = average_analog_read(UVsensorIn)  # Read the averaged analog value
        
        # Calculate the output voltage (3.3V reference)
        output_voltage = 3.3 * uv_level / 4095.0  # Scaling the value to 0-3.3V
        
        # Debug: Print the raw UV level and corresponding output voltage
        print("Raw UV Level: {}".format(uv_level))
        print("Output Voltage: {:.2f} V".format(output_voltage))
        
        # Adjusted map function for voltage-to-UV intensity conversion
        # Modify the voltage range to more accurately reflect your sensor's behavior
        # Assume 0.85V corresponds to around 3.85 mW/cm², which is a typical indoor UV reading.
        # Map voltage range 0V-3.3V to UV intensity range 0-15 mW/cm².
        uv_intensity = mapfloat(output_voltage, 0.0, 3.3, 0.0, 15.0)
        
        # Debug: Print the calculated UV intensity
        print("UV Intensity: {:.2f} mW/cm^2".format(uv_intensity))
        
        # Wait 200ms before the next reading
        time.sleep(0.2)
        
        # lê o valor do LDR
        value = ldr.value()
        
        print('luminosidade = {:.0f} de 100'.format(value))
        
        dadosUltimoMinuto.append(value)
        
        # faz o led acender de acordo com a luminosidade
        if(value >= 50):
            led.value(1)
            time.sleep(0.5)
        else:
            led.value(0)
        if(value >= 80):
            led2.value(1)
        else:
            led2.value(0)
        if(value == 100):
            led3.value(1)
        else:
            led3.value(0)
            

        # delay de 1 segundo entre medições
        time.sleep(1)
        
    # calcula a média da luminosidade do último minuto
    mediaLuminosidadeUltimoMinuto = sum(dadosUltimoMinuto)/60

    # adiciona a média da luminosidade do último minuto
    dadosLuminosidadeUltimaHora.adicionar(mediaLuminosidadeUltimoMinuto)
    dadosLuminosidadeUltimaHora.mostrar()

