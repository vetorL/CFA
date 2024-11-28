# CFA

ACH2157 - Computação Física e Aplicações (2024)

# Projeto Solar Cap

![SolarCap Logo](SolarCap_LOGO.gif)

## Design do Boné

![Design do Boné](design_bone.jpg)

## Documentação

# Documentação do Módulo `oled_display.py`

O módulo `oled_display.py` é responsável por controlar um display OLED de 128x64 pixels utilizando o driver SSD1306. A comunicação é realizada via protocolo I2C utilizando os pinos SDA e SCL. A classe `Display` encapsula funcionalidades para inicialização e exibição de imagens no display OLED.

## Dependências
Este módulo depende das seguintes bibliotecas:
- `machine`: Para controle dos pinos de I/O e comunicação I2C.
- `ssd1306`: Para controle do display OLED SSD1306.
- `framebuf`: Para manipulação de buffers de imagem para exibição no display.
- `images_repo`: Repositório contendo uma lista de imagens a serem exibidas.
- `utime`: Para controle de tempo e delays.

## Classe `Display`

A classe `Display` fornece métodos para inicializar o display OLED e exibir uma sequência de imagens em introdução.

### `__init__(self)`
Inicializa o display OLED utilizando o endereço I2C padrão `0x3C`.

#### Parâmetros:
- Nenhum parâmetro é necessário para este método, pois ele usa os pinos padrão `22` (SDA) e `23` (SCL) para a comunicação I2C.

#### Descrição:
Este método configura a comunicação I2C com os pinos especificados e inicializa o display SSD1306 com resolução de 128x64 pixels.

### `start_intro(self)`
Exibe uma sequência de imagens armazenadas no repositório `images_repo.images_list` no display OLED. Cada imagem será exibida por um curto período de tempo (100 milissegundos).

#### Parâmetros:
- Nenhum parâmetro é necessário para este método.

#### Descrição:
1. O método percorre a lista de imagens contida em `images_repo.images_list`.
2. Cada imagem da lista é exibida no display.
3. A imagem é convertida para um buffer de memória (utilizando a classe `framebuf.FrameBuffer`).
4. O conteúdo da imagem é exibido no display OLED.
5. O display é atualizado após cada imagem, com um intervalo de 100 milissegundos entre elas.

## Exemplo de Uso

```python
from oled_display import Display

# Criando uma instância do display OLED
display = Display()

# Iniciando a exibição das imagens de introdução
display.start_intro()
```

## Estrutura de Arquivos

### `images_repo.py`

Este arquivo deve conter uma lista de imagens (em formato de buffer de dados), que são referenciadas no método `start_intro` para exibição no display.

Exemplo de estrutura do `images_repo.py`:

```python
images_list = [
    bytearray(b'\x00\x00\x00\x00\x00...'),  # Imagem 1
    bytearray(b'\x00\x00\x00\x00\x00...'),  # Imagem 2
    ...
]
```

Cada elemento da lista `images_list` deve ser uma sequência de bytes representando uma imagem compatível com a resolução do display (128x64 pixels).

## Notas
- O módulo presume que o display OLED está conectado corretamente aos pinos I2C padrão (SDA = 22, SCL = 23). Caso contrário, esses pinos podem ser alterados na instância de `SoftI2C` no método `__init__`.
- As imagens no repositório `images_repo` devem estar no formato apropriado para o uso com o `framebuf.FrameBuffer`, ou seja, buffers de 128x64 pixels com profundidade de cor de 1 bit.
- O tempo de exibição de cada imagem é de 100 milissegundos, conforme definido no método `start_intro`. Esse valor pode ser ajustado para diferentes durações.

## Mapemento dos Pinos

### Sensor UV (GYML8511)

VIN <-> nada\
3V3 <-> 3V3\
GND <-> GND\
OUT <-> D34\
EN <-> 3V3

### Sensor de Luz - LDR

5Vcc <-> 3V3\
Sinal Analog. <-> D32\
GND <-> GND\
Led1 <-> D13\
Led2 <-> D12\
Led3 <-> D14

### Motor de Vibração Coin

Fio Vermelho <-> D5\
Fio Preto <-> GND

### Sensor touch - TTP223B

IO <-> D18\
VCC <-> 3V3\
GND <-> GND

### OLED Display

GND <-> GND\
VCC <-> 3V3\
SCL <-> 23\
SDA <-> 22
