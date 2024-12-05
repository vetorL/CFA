# CFA

ACH2157 - Computação Física e Aplicações (2024)

# Projeto Solar Cap

![SolarCap Logo](SolarCap_LOGO.gif)

## Design do Boné

![Design do Boné](design_bone.jpg)

# Documentação do Módulo `main.py`

O módulo `main.py` é responsável pela execução do sistema **SolarCap**, que integra diferentes sensores (vibração, luminosidade, UV, e toque) com um display OLED para fornecer informações sobre a intensidade de UV e outras condições ambientais. Ele utiliza sensores e dispositivos periféricos para controlar e exibir informações, com ações baseadas em leituras de luminosidade e UV.

## Dependências

Este módulo depende dos seguintes arquivos e bibliotecas:

- **`vibration_motor`**: Para controle do motor de vibração.
- **`LDR`**: Para ler e ajustar LEDs de acordo com a luminosidade.
- **`touch`**: Para verificar se o botão touch foi pressionado.
- **`UV`**: Para capturar a intensidade de UV.
- **`dados`**: Para gerenciar e armazenar dados de luminosidade e UV.
- **`oled_display`**: Para exibir informações no display OLED.
- **`time`**: Para controle do tempo (delays).

## Classe `SolarCap`

A classe `SolarCap` é a principal do sistema e controla todos os sensores e dispositivos, gerenciando o fluxo de dados e a interação com o usuário.

### Métodos

#### `__init__(self)`

Este é o método inicializador que configura todos os sensores e dispositivos periféricos necessários para o funcionamento do sistema.

##### Parâmetros:

- Nenhum parâmetro é necessário.

##### Descrição:

- Inicializa os componentes do sistema:
  - **Motor de vibração**: Configura o motor de vibração, conectando-o ao pino D5.
  - **LDR (Light Dependent Resistor)**: Configura o sensor de luminosidade, conectando-o ao pino D32.
  - **Touch**: Configura o sensor de toque, conectando-o ao pino D18.
  - **UV Sensor**: Configura o sensor de UV, conectando-o ao pino D34.
  - **Dados**: Cria uma instância do repositório de dados, configurando para armazenar até 900 entradas (equivalente a 15 minutos).
  - **Display**: Inicializa o display OLED para exibir informações sobre os níveis de UV.

#### `start(self)`

Inicia o ciclo principal do programa, onde o sistema irá realizar leituras dos sensores, controlar o motor de vibração, exibir informações no display e permitir que o usuário interaja com o sistema por meio do toque.

##### Parâmetros:

- Nenhum parâmetro é necessário.

##### Descrição:

- O método começa com a exibição de uma introdução utilizando o display OLED, através do método `run_intro()` da classe `Display`.
- Em seguida, entra em um **loop principal**, onde ocorre a verificação contínua de várias condições e ações:
  - Se a média de luminosidade for maior que 90 e a intensidade de UV for maior que 5, o motor de vibração é ativado.
  - Se o botão de toque for pressionado, os dados de luminosidade e UV são resetados.
  - O sensor de luminosidade ajusta os LEDs conforme o valor da luminosidade.
  - Os dados de luminosidade e UV da iteração atual são armazenados em `dados`.
  - A intensidade de UV é verificada para exibir uma sequência de imagens no display OLED:
    - Se a intensidade UV for superior a 6, exibe imagens de "UV Muito Alto".
    - Se a intensidade UV for superior a 5, exibe imagens de "UV Alto".
    - Se a intensidade UV for superior a 4, exibe imagens de "UV Moderado".
    - Se a intensidade UV for superior a 3, exibe imagens de "UV Baixo".
- O loop principal ocorre a cada 1 segundo, com um delay controlado pela função `time.sleep(1)`.

#### Exceções

- Se o programa for interrompido pelo usuário (via `KeyboardInterrupt`), o método realiza a desativação de componentes para garantir que o sistema seja desligado corretamente:
  - Desliga o motor de vibração.
  - Desliga o sensor LDR.
  - Exibe a mensagem "Program stopped".

## Exemplo de Uso

```python
from main import SolarCap

# Criando uma instância do sistema SolarCap
solarCap = SolarCap()

# Iniciando o sistema
solarCap.start()
```

## Estrutura do Sistema

### Sensores e Dispositivos

- **Motor de vibração**: Controlado pela classe `VibrationMotor`, é ativado quando as condições de luminosidade e UV são altas.
- **LDR**: Utiliza a classe `LDR` para medir a luminosidade e ajustar LEDs.
- **Sensor de toque**: Utiliza a classe `touch` para detectar quando o usuário pressiona o botão.
- **Sensor de UV**: Mede a intensidade de UV utilizando a classe `UV`.
- **Display OLED**: Utiliza a classe `Display` para exibir diferentes imagens dependendo da intensidade UV detectada.

### Fluxo de Dados

1. O sistema coleta dados de luminosidade e UV em intervalos de 1 segundo.
2. A média desses dados é calculada e, se as condições forem atendidas (luminosidade > 90 e UV > 5), o motor de vibração é ativado.
3. O display OLED exibe imagens correspondentes ao nível de UV detectado.

## Notas

- O programa assume que os sensores e dispositivos estão conectados corretamente aos pinos especificados. Caso os pinos sejam alterados, é necessário atualizar a configuração no código.
- O sistema possui um **loop contínuo** que coleta dados e controla o motor de vibração, além de exibir informações no display OLED.
- O tempo de execução é controlado pelo **delay de 1 segundo** entre as iterações, o que permite uma atualização contínua e precisa dos dados.

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

---

# Documentação do Módulo `img_bytearray_script.py`

O módulo `img_bytearray_script.py` automatiza a geração de byte arrays para imagens em escala de cinza, formatadas para exibição em displays OLED ou outras aplicações que utilizem buffers de imagem em formato binário. Ele processa imagens localizadas em subdiretórios de uma pasta raiz, gera versões invertidas e redimensionadas, e as armazena em um arquivo Python no formato necessário.

---

## Dependências

Este script utiliza as seguintes bibliotecas:

- **`os`**: Para manipulação de diretórios e caminhos de arquivos.
- **`io`**: Para criar fluxos de bytes em memória.
- **`PIL` (Pillow)**: Para manipulação e transformação de imagens.
- **`re`**: Para ordenação natural de nomes de arquivos e diretórios.

---

## Parâmetros Configuráveis

- **Dimensões de saída**:
  - `x, y = 128, 64`: Dimensões das imagens de saída (em pixels).
- **Pasta raiz das imagens**:
  - `assets_dir = "assets"`: Caminho para a pasta contendo subdiretórios com imagens a serem processadas.
- **Arquivo de saída**:
  - `output_file = "images_repo.py"`: Caminho para o arquivo Python onde os byte arrays gerados serão salvos.

---

## Fluxo do Script

1. **Configuração inicial**:
   - Cria e inicializa o arquivo de saída, inserindo um cabeçalho.
2. **Ordenação natural**:
   - Ordena subdiretórios e arquivos para garantir que as imagens sejam processadas na sequência esperada.
3. **Processamento de imagens**:
   - Para cada subdiretório:
     - Processa cada imagem:
       - Redimensiona para as dimensões especificadas.
       - Inverte as cores (para compatibilidade com displays que usam cor binária invertida).
       - Converte a imagem para um byte array.
     - Gera variáveis Python para cada imagem e lista de imagens para o subdiretório.
4. **Exportação**:
   - Escreve os byte arrays e listas de imagens no arquivo de saída.

---

## Funções e Métodos

### `natural_sort_key(s)`

- **Descrição**:
  Retorna uma chave de ordenação natural para strings, permitindo que nomes de arquivos como `img1`, `img2`, ..., `img10` sejam ordenados corretamente.
- **Parâmetros**:

  - `s` (str): Nome do arquivo ou diretório.

- **Retorno**:
  - Uma lista contendo inteiros e strings, permitindo a ordenação natural.

---

## Exemplo de Estrutura de Arquivos

### Entrada

**Diretório `assets/`**:

```
assets/
├── intro/
│   ├── frame1.png
│   ├── frame2.png
│   └── frame3.png
├── uv_baixo/
│   ├── img1.png
│   └── img2.png
└── uv_alto/
    ├── img1.png
    ├── img2.png
    └── img3.png
```

### Saída

**Arquivo `images_repo.py`**:

```python
# Image byte arrays with inverted colors

intro_img_1 = bytearray(b'\x00\x01\x02...')  # Byte array da imagem 1
intro_img_2 = bytearray(b'\x01\x02\x03...')  # Byte array da imagem 2

intro_images_list = [intro_img_1, intro_img_2]

uv_baixo_img_1 = bytearray(b'\x04\x05\x06...')
uv_baixo_img_2 = bytearray(b'\x07\x08\x09...')

uv_baixo_images_list = [uv_baixo_img_1, uv_baixo_img_2]

uv_alto_img_1 = bytearray(b'\x0A\x0B\x0C...')
uv_alto_img_2 = bytearray(b'\x0D\x0E\x0F...')
uv_alto_img_3 = bytearray(b'\x10\x11\x12...')

uv_alto_images_list = [uv_alto_img_1, uv_alto_img_2, uv_alto_img_3]
```

---

## Notas Importantes

- **Formatos suportados**: O script processa arquivos compatíveis com o Pillow (ex.: PNG, JPEG, BMP).
- **Inversão de cores**: Essencial para displays OLED que usam buffer de cor binária invertida.
- **Resolução**: Certifique-se de que o display ou dispositivo alvo suporta as dimensões configuradas (`128x64` por padrão).

---

## Execução

1. Certifique-se de que as imagens estão organizadas na estrutura de pastas correta dentro do diretório especificado (`assets/`).
2. Execute o script:
   ```bash
   python img_bytearray_script.py
   ```
3. Verifique o arquivo de saída (`images_repo.py`) para os byte arrays e listas de imagens gerados.

---

# Documentação do Módulo `LDR.py`

O módulo `LDR.py` implementa uma classe para a leitura de um sensor LDR (Light Dependent Resistor) conectado a um microcontrolador. Além de fornecer leituras ajustadas para um intervalo personalizado, ele também controla LEDs que indicam diferentes níveis de luminosidade.

## Classe `LDR`

A classe `LDR` encapsula a funcionalidade necessária para interagir com o sensor LDR e controlar LEDs com base nas leituras de luminosidade.

### Métodos

#### `__init__(self, pin, min_value=0, max_value=100)`

Este método inicializa a classe `LDR`.

##### Parâmetros:

- **`pin`** (`int`): O número do pino ao qual o sensor LDR está conectado.
- **`min_value`** (`int`, opcional): O menor valor no intervalo de saída. O padrão é 0.
- **`max_value`** (`int`, opcional): O maior valor no intervalo de saída. O padrão é 100.

##### Descrição:

- Configura o ADC (Conversor Analógico-Digital) para ler valores do pino especificado.
- Define os pinos dos LEDs e os configura como saídas.
- Lança uma exceção se `min_value` for maior ou igual a `max_value`.

##### Exemplo:

```python
ldr = LDR(pin=32, min_value=0, max_value=100)
```

---

#### `read(self)`

Lê o valor bruto do sensor LDR.

##### Retorno:

- **`int`**: Um valor entre 0 e 4095 representando a leitura do sensor.

##### Exemplo:

```python
raw_value = ldr.read()
print(f"Valor bruto do LDR: {raw_value}")
```

---

#### `value(self)`

Retorna o valor ajustado da leitura do LDR com base nos intervalos definidos no construtor.

##### Retorno:

- **`float`**: Um valor no intervalo `[min_value, max_value]`.

##### Exemplo:

```python
luminosidade = ldr.value()
print(f"Luminosidade ajustada: {luminosidade}")
```

---

#### `adjust_LEDs(self)`

Controla o estado dos LEDs com base no nível de luminosidade lido pelo sensor.

##### Descrição:

- Acende o LED 1 se a luminosidade for maior ou igual a 50.
- Acende o LED 2 se a luminosidade for maior ou igual a 80.
- Acende o LED 3 se a luminosidade atingir 100.

##### Exemplo:

```python
ldr.adjust_LEDs()
```

---

#### `mostrar_luminosidade(self)`

Exibe a luminosidade ajustada no console.

##### Exemplo:

```python
ldr.mostrar_luminosidade()
```

---

#### `turnoff(self)`

Desliga todos os LEDs.

##### Exemplo:

```python
ldr.turnoff()
```

---

## Exemplo de Uso

```python
from LDR import LDR
import time

# Instanciando o sensor LDR
ldr = LDR(pin=32, min_value=0, max_value=100)

try:
    while True:
        # Mostra a luminosidade no console
        ldr.mostrar_luminosidade()

        # Ajusta os LEDs com base na leitura de luminosidade
        ldr.adjust_LEDs()

        # Aguarda 1 segundo antes de fazer a próxima leitura
        time.sleep(1)
except KeyboardInterrupt:
    # Desliga os LEDs ao interromper o programa
    ldr.turnoff()
    print("Programa encerrado.")
```

---

## Estrutura de Pinos

### Sensor LDR

- **Pino Analógico** -> Conectado ao pino especificado no construtor (por exemplo, D32).
- **GND** -> GND.
- **VCC** -> 3.3V ou 5V (dependendo do modelo do LDR).

### LEDs

- **LED 1** -> Conectado ao pino D13.
- **LED 2** -> Conectado ao pino D12.
- **LED 3** -> Conectado ao pino D14.

---

## Notas

- **Intervalo de Valores:** O método `value()` ajusta a leitura bruta do LDR (0-4095) para o intervalo especificado pelo usuário (`min_value` a `max_value`).
- **Controle de LEDs:** Os LEDs fornecem um feedback visual sobre a luminosidade detectada.
- **Exceção:** O construtor lançará uma exceção se `min_value` for maior ou igual a `max_value`.

# Documentação do Módulo `touch.py`

O módulo `touch.py` implementa uma classe simples para interagir com um sensor de toque conectado a um microcontrolador. Ele verifica se o sensor detecta um toque e retorna um estado booleano.

---

## Classe `touch`

A classe `touch` encapsula a lógica para gerenciar um sensor de toque conectado a um pino específico.

---

### Métodos

#### `__init__(self, SENSOR_PIN)`

Inicializa a instância da classe `touch`.

##### Parâmetros:

- **`SENSOR_PIN`** (`int`): O número do pino digital ao qual o sensor de toque está conectado.

##### Descrição:

- Configura o pino especificado como entrada para capturar o estado do sensor.

##### Exemplo:

```python
sensor_toque = touch(SENSOR_PIN=27)
```

---

#### `is_touching(self)`

Verifica se o sensor de toque está ativo (toque detectado).

##### Retorno:

- **`bool`**:
  - `True`: Quando o sensor detecta um toque (estado lógico 1).
  - `False`: Quando nenhum toque é detectado (estado lógico 0).

##### Exemplo:

```python
if sensor_toque.is_touching():
    print("Sensor de toque ativado!")
else:
    print("Nenhum toque detectado.")
```

---

## Exemplo de Uso

```python
from touch import touch
import time

# Instanciando o sensor de toque
sensor = touch(SENSOR_PIN=27)

try:
    while True:
        if sensor.is_touching():
            print("Toque detectado!")
        else:
            print("Nenhum toque.")

        # Aguarda 0.5 segundos antes de verificar novamente
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Programa encerrado.")
```

---

## Estrutura de Pinos

### Sensor de Toque

- **Sinal** -> Conectado ao pino especificado no construtor (por exemplo, D27).
- **GND** -> GND.
- **VCC** -> 3.3V ou 5V (dependendo do modelo do sensor).

---

## Notas

- **Lógica:** O método `is_touching()` verifica o estado do pino digital associado ao sensor de toque.
  - Um valor lógico 1 indica que o sensor detectou um toque.
  - Um valor lógico 0 indica que nenhum toque foi detectado.
- **Uso em Loops:** Ideal para aplicações que requerem detecção contínua de toque, como interruptores táteis ou interfaces interativas.

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
