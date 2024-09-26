import network
import usocket as socket

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid="Pizza de chocolate com banana", password="ehmtbom")

while ap.active() == False:
    pass

print('Conexão realizada com sucesso! gg')
print(ap.ifconfig())

def web_page():
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
    return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    print('Content = %s' % str(request))
    response = web_page()
    conn.send(response)
    conn.close()
