import random
import base64
import time

def html_base(fundo, cont, img):
    return """<html>
                  <head>
                      <title>GF - Comendador Ermelino/L12</title>
                      <meta http-equiv='refresh' content='8'>
                      <link rel='stylesheet' type='text/css' href='style.css'>
                  </head>
                  <body>
                      <div class='container'><img src='data:image/jpeg;base64,""" + fundo + """'></div>
                      <div class='centered'>Passageiros na plataforma:</br>"""+ cont +"""</div>
                      <img src='data:image/jpeg;base64,""" + img + """'>
                  </body>
              </html>"""

entrada = open("dados.txt").read()
saida = open("sso.html", "w")

cont = entrada.count('"}')
i=int(0)

while i < 10:
    cont = random.randint(0, 400)   
    saida.truncate(0)
    if cont < 100:
        fundo = base64.b64encode(open('fundo.jpg', 'rb').read()).decode('utf-8')
        img = base64.b64encode(open('1.jpg', 'rb').read()).decode('utf-8')
        saida.write(html_base(fundo, str(cont), img))
    elif cont >= 100 and cont < 200:
        fundo = base64.b64encode(open('fundo.jpg', 'rb').read()).decode('utf-8')
        img = base64.b64encode(open('3.jpg', 'rb').read()).decode('utf-8')
        saida.write(html_base(fundo, str(cont), img))
    elif cont >= 200 and cont < 300:
        fundo = base64.b64encode(open('fundo.jpg', 'rb').read()).decode('utf-8')
        img = base64.b64encode(open('3.jpg', 'rb').read()).decode('utf-8')
        saida.write(html_base(fundo, str(cont), img))
    else:
        fundo = base64.b64encode(open('fundo.jpg', 'rb').read()).decode('utf-8')
        img = base64.b64encode(open('2.jpg', 'rb').read()).decode('utf-8')
        saida.write(html_base(fundo, str(cont), img))
             
    time.sleep(8)
    i += 1
