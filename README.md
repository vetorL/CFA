# CFA

ACH2157 - Computação Física e Aplicações (2024)

# Projeto Solar Cap

![SolarCap Logo](SolarCap_LOGO.gif)

## Design do Boné

![Design do Boné](design_bone.jpg)

# Documentação do Módulo `oled_display.py`

O módulo `oled_display.py` é responsável por controlar um display OLED de 128x64 pixels utilizando o driver SSD1306, através do protocolo I2C. A classe `Display` oferece funcionalidades para inicialização e exibição de imagens no display, incluindo diferentes conjuntos de imagens relacionadas a informações de UV.

## Dependências

Este módulo depende das seguintes bibliotecas:
- **`machine`**: Para controle dos pinos de I/O e comunicação I2C.
- **`ssd1306`**: Para controle do display OLED SSD1306.
- **`framebuf`**: Para manipulação de buffers de imagem para exibição no display.
- **`images_repo`**: Repositório contendo as listas de imagens a serem exibidas.
- **`utime`**: Para controle de tempo e delays.

## Classe `Display`

A classe `Display` encapsula todas as operações necessárias para controlar e exibir imagens no display OLED.

### Métodos

#### `__init__(self)`

Este método inicializa o display OLED utilizando o endereço I2C padrão (`0x3C`) e configura os pinos SDA (22) e SCL (23) para a comunicação I2C.

##### Parâmetros:
- Nenhum parâmetro é necessário.

##### Descrição:
- Este método configura a comunicação I2C com os pinos especificados e inicializa o display SSD1306 com resolução de 128x64 pixels.

#### `run(self, images_list)`

Exibe uma sequência de imagens no display OLED, que são passadas como parâmetro na lista `images_list`.

##### Parâmetros:
- **`images_list`** (list): Uma lista de imagens, onde cada imagem é representada como um objeto `bytearray`. Cada imagem é exibida uma a uma no display.

##### Descrição:
1. O método percorre a lista de imagens fornecida.
2. Cada imagem é convertida para um buffer de memória usando a classe `framebuf.FrameBuffer`.
3. O conteúdo da imagem é exibido no display OLED.
4. A tela é atualizada após cada imagem, com um intervalo de 100 milissegundos entre elas.

#### `run_intro(self)`

Exibe uma sequência de imagens de introdução.

##### Parâmetros:
- Nenhum parâmetro é necessário.

##### Descrição:
- Este método invoca o método `run()` passando a lista de imagens de introdução armazenadas em `images_repo.intro_images_list`.

#### `run_uv_low(self)`

Exibe uma sequência de imagens relacionadas ao nível baixo de UV.

##### Parâmetros:
- Nenhum parâmetro é necessário.

##### Descrição:
- Este método invoca o método `run()` passando a lista de imagens relacionadas ao UV baixo, armazenadas em `images_repo.uv_baixo_images_list`.

#### `run_uv_moderate(self)`

Exibe uma sequência de imagens relacionadas ao nível moderado de UV.

##### Parâmetros:
- Nenhum parâmetro é necessário.

##### Descrição:
- Este método invoca o método `run()` passando a lista de imagens relacionadas ao UV moderado, armazenadas em `images_repo.uv_moderado_images_list`.

#### `run_uv_high(self)`

Exibe uma sequência de imagens relacionadas ao nível alto de UV.

##### Parâmetros:
- Nenhum parâmetro é necessário.

##### Descrição:
- Este método invoca o método `run()` passando a lista de imagens relacionadas ao UV alto, armazenadas em `images_repo.uv_alto_images_list`.

#### `run_uv_very_high(self)`

Exibe uma sequência de imagens relacionadas ao nível muito alto de UV.

##### Parâmetros:
- Nenhum parâmetro é necessário.

##### Descrição:
- Este método invoca o método `run()` passando a lista de imagens relacionadas ao UV muito alto, armazenadas em `images_repo.uv_muito_alto_images_list`.

## Exemplo de Uso

```python
from oled_display import Display

# Criando uma instância do display OLED
display = Display()

# Iniciando a exibição das imagens de introdução
display.run_intro()

# Iniciando a exibição das imagens para nível de UV baixo
display.run_uv_low()

# Iniciando a exibição das imagens para nível de UV moderado
display.run_uv_moderate()

# Iniciando a exibição das imagens para nível de UV alto
display.run_uv_high()

# Iniciando a exibição das imagens para nível de UV muito alto
display.run_uv_very_high()
```

## Estrutura de Arquivos

### `images_repo.py`

Este arquivo deve conter as listas de imagens em formato de buffer de dados, que são referenciadas nos métodos da classe `Display`. Cada lista contém imagens que serão exibidas no display OLED.

#### Exemplo de estrutura do `images_repo.py`:

```python
intro_images_list = [
    bytearray(b'\x00\x00\x00\x00\x00...'),  # Imagem 1
    bytearray(b'\x00\x00\x00\x00\x00...'),  # Imagem 2
    ...
]

uv_baixo_images_list = [
    bytearray(b'\x00\x00\x00\x00\x00...'),  # Imagem UV Baixo 1
    bytearray(b'\x00\x00\x00\x00\x00...'),  # Imagem UV Baixo 2
    ...
]

uv_moderado_images_list = [
    bytearray(b'\x00\x00\x00\x00\x00...'),  # Imagem UV Moderado 1
    bytearray(b'\x00\x00\x00\x00\x00...'),  # Imagem UV Moderado 2
    ...
]

uv_alto_images_list = [
    bytearray(b'\x00\x00\x00\x00\x00...'),  # Imagem UV Alto 1
    bytearray(b'\x00\x00\x00\x00\x00...'),  # Imagem UV Alto 2
    ...
]

uv_muito_alto_images_list = [
    bytearray(b'\x00\x00\x00\x00\x00...'),  # Imagem UV Muito Alto 1
    bytearray(b'\x00\x00\x00\x00\x00...'),  # Imagem UV Muito Alto 2
    ...
]
```

Cada elemento da lista deve ser um `bytearray` representando uma imagem compatível com a resolução do display (128x64 pixels) e profundidade de cor de 1 bit.

## Notas
- O módulo assume que o display OLED está conectado corretamente aos pinos I2C padrão (SDA = 22, SCL = 23). Caso contrário, os pinos podem ser alterados no construtor `SoftI2C`.
- As imagens no repositório `images_repo` devem estar no formato apropriado para uso com o `framebuf.FrameBuffer`, ou seja, buffers de 128x64 pixels com profundidade de cor de 1 bit.
- O tempo de exibição de cada imagem é de 100 milissegundos, conforme definido no método `run`. Esse valor pode ser ajustado conforme necessário.

## Mapemento dos Pinos

### Sensor UV (GYML8511)

- **VIN** -> Não conectado
- **3V3** -> 3V3
- **GND** -> GND
- **OUT** -> D34
- **EN** -> 3V3

### Sensor de Luz - LDR

- **5Vcc** -> 3V3
- **Sinal Analógico** -> D32
- **GND** -> GND
- **Led1** -> D13
- **Led2** -> D12
- **Led3** -> D14

### Motor de Vibração Coin

- **Fio Vermelho** -> D5
- **Fio Preto** -> GND

### Sensor Touch - TTP223B

- **IO** -> D18
- **VCC** -> 3V3
- **GND** -> GND

### OLED Display

- **GND** -> GND
- **VCC** -> 3V3
- **SCL** -> D23
- **SDA** -> D22