from machine import ADC, Pin
import time

led = Pin(13, Pin.OUT)
led2 = Pin(12, Pin.OUT)
led3 = Pin(14, Pin.OUT)


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
    # Inicializa a classe
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
        # lê o valor do LDR
        value = ldr.value()

        print("luminosidade = {:.0f} de 100".format(value))

        dadosUltimoMinuto.append(value)

        # faz o led acender de acordo com a luminosidade
        if value >= 50:
            led.value(1)
            time.sleep(0.5)
        else:
            led.value(0)
        if value >= 80:
            led2.value(1)
        else:
            led2.value(0)
        if value == 100:
            led3.value(1)
        else:
            led3.value(0)

        # delay de 1 segundo entre medições
        time.sleep(1)

    # calcula a média da luminosidade do último minuto
    mediaLuminosidadeUltimoMinuto = sum(dadosUltimoMinuto) / 60

    # adiciona a média da luminosidade do último minuto
    dadosLuminosidadeUltimaHora.adicionar(mediaLuminosidadeUltimoMinuto)
    dadosLuminosidadeUltimaHora.mostrar()
