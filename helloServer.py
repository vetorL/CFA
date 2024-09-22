# from microdot import Microdot
# 
# # setup webserver
# app = Microdot()
# 
# @app.route('/')
# async def hello(request):
#     return 'Hello world'
# 
# app.run()

# https://github.com/miguelgrinberg/microdot/blob/main/examples/hello/hello.py
# import connectAsAP
from microdot import Microdot
from machine import Pin, PWM
import time

# Define o pino do buzzer
buzzer = PWM(Pin(15), freq=1000, duty=512)  # 50% de duty cycle

# Notas da música em Hertz
notes = {
    'C4': 261.63,
    'C#4': 277.18,
    'D4': 293.66,
    'D#4': 311.13,
    'E4': 329.63,
    'F4': 349.23,
    'F#4': 369.99,
    'G4': 392.00,
    'G#4': 415.30,
    'A4': 440.00,
    'A#4': 466.16,
    'B4': 493.88,
    'C5': 523.25,
    'C#5': 554.37,
    'D5': 587.33,
    'D#5': 622.25,
    'E5': 659.25,
    'F5': 698.46,
    'F#5': 739.99,
    'G5': 783.99,
    'G#5': 830.61,
    'A5': 880.00,
    'A#5': 932.33,
    'B5': 987.77,
}


app = Microdot()

html = '''
<!DOCTYPE html>
<html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Piano Playing</title>
        <style>
            @import url(
            'https://fonts.googleapis.com/css2?family=Poppins&amp;display=swap');

            body {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: &quot;Poppins&quot;, sans-serif;
            }

            .container {
                background-image: 
                      linear-gradient(90deg, #9331d4, rgb(239 5 92 / 70%));
                height: 100vh;
                width: 100%;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
            }

            .intro-container {
                color: #fff;
                text-align: center;
            }

            .piano-container {
                display: flex;
                align-items: center;
                justify-content: center;
            }

            .piano-keys-list {
                list-style: none;
                display: flex;
                justify-content: center;
            }

            .piano-keys {
                width: 5rem;
                cursor: pointer;
                position: relative;
                height: 20rem;
                border-radius: 10px;
                border: 1px solid #000;
            }

            .white-key {
                background-color: #fff;
            }

            .black-key {
                width: 2rem;
                height: 13rem;
                border-radius: 5px;
                border-top-left-radius: 0;
                border-top-right-radius: 0;
                background-color: #000;
                z-index: 2;
                margin: 0 -20px 0 -20px;
            }

            @media screen and (min-width: 821px) and (max-width: 1024px) {
                .piano-keys {
                    width: 4rem;
                    cursor: pointer;
                    position: relative;
                    height: 20rem;
                    border-radius: 10px;
                    border: 1px solid #000;
                }

                .black-key {
                    width: 2rem;
                    height: 13rem;
                    border-radius: 5px;
                    border-top-left-radius: 0;
                    border-top-right-radius: 0;
                    background-color: #000;
                    z-index: 2;
                    margin: 0 -20px 0 -20px;
                }
            }

            @media screen and (min-width: 768px) and (max-width: 820px) {
                .piano-keys {
                    width: 3.5rem;
                    cursor: pointer;
                    position: relative;
                    height: 16rem;
                    border-radius: 10px;
                    border: 1px solid #000;
                }

                .black-key {
                    width: 1.8rem;
                    height: 10rem;
                    border-radius: 5px;
                    border-top-left-radius: 0;
                    border-top-right-radius: 0;
                    background-color: #000;
                    z-index: 2;
                    margin: 0 -20px 0 -20px;
                }
            }

            @media screen and (max-width: 576px) {
                .piano-container {
                    width: 90%;
                    display: flex;
                    align-items: center;
                    justify-content: flex-start;
                    overflow: auto;
                }

                .piano-keys {
                    width: 3.5rem;
                    cursor: pointer;
                    position: relative;
                    height: 16rem;
                    border-radius: 10px;
                    border: 1px solid #000;
                }

                .black-key {
                    width: 1.8rem;
                    height: 10rem;
                    border-radius: 5px;
                    border-top-left-radius: 0;
                    border-top-right-radius: 0;
                    background-color: #000;
                    z-index: 2;
                    margin: 0 -20px 0 -20px;
                }
            }
            
        </style>
    </head>

    <body>
        <div class="container">
            <div class="intro-container">
                <h1>Piano ESP32 + Buzzer</h1>
                <h3>This is a 24-key piano. Click any piano key to play the sound.</h3>
            </div>
            <div class="piano-container">
                <ul class="piano-keys-list">
                    <li class="piano-keys white-key" data-key="1"></li>
                    <li class="piano-keys black-key" data-key="2"></li>
                    <li class="piano-keys white-key" data-key="3"></li>
                    <li class="piano-keys black-key" data-key="4"></li>
                    <li class="piano-keys white-key" data-key="5"></li>
                    <li class="piano-keys black-key" data-key="6"></li>
                    <li class="piano-keys white-key" data-key="7"></li>
                    <li class="piano-keys white-key" data-key="8"></li>
                    <li class="piano-keys black-key" data-key="9"></li>
                    <li class="piano-keys white-key" data-key="10"></li>
                    <li class="piano-keys black-key" data-key="11"></li>
                    <li class="piano-keys white-key" data-key="12"></li>
                    <li class="piano-keys white-key" data-key="13"></li>
                    <li class="piano-keys black-key" data-key="14"></li>
                    <li class="piano-keys white-key" data-key="15"></li>
                    <li class="piano-keys black-key" data-key="16"></li>
                    <li class="piano-keys white-key" data-key="17"></li>
                    <li class="piano-keys black-key" data-key="18"></li>
                    <li class="piano-keys white-key" data-key="19"></li>
                    <li class="piano-keys white-key" data-key="20"></li>
                    <li class="piano-keys black-key" data-key="21"></li>
                    <li class="piano-keys white-key" data-key="22"></li>
                    <li class="piano-keys black-key" data-key="23"></li>
                    <li class="piano-keys white-key" data-key="24"></li>
                </ul>
            </div>
        </div>

        <script>
            const url = "10.8.10.195:5000";
            const keys = document.querySelectorAll('.piano-keys');
            
            keys.forEach((key) => {
                key.addEventListener('click', (e) => {
                    const clickedKey = e.target.dataset.key;
                    console.log(clickedKey);
                    
                    fetch("/tocar/" + clickedKey);
                })
            })
        </script>
    </body>

</html>

'''

@app.route('/')
async def hello(request):
    return html, 200, {'Content-Type': 'text/html'}

@app.get('/tocar/<int:id>')
async def tocar(request, id):
    print(str(id) + " foi tocado")
    
    frequency = list(notes.values())[id]
    buzzer.freq(frequency)
    buzzer.duty(512)
    time.sleep(0.5)
    
    return

@app.route('/shutdown')
async def shutdown(request):
    request.app.shutdown()
    return 'The server is shutting down...'

print("FINISHED LOADING <START>")
app.run(debug=True)

