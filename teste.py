import random
import base64
import time

def html_base(fundo, banner, cont): #cria a estrutura html da pagina
    return """<html>
                  <head>
                      <title>GF - Comendador Ermelino/L12</title>
                      <meta http-equiv='refresh' content='5'>
                      <link rel='stylesheet' type='text/css' href='style.css'>
                  </head>
                  <body>
                      <div class='back'><img src='data:image/jpeg;base64,""" + fundo + """'></div>
                      <div class='banner'><img src='data:image/jpeg;base64,""" + banner + """'></div>
                      <div class='content'>"""+ cont +"""%</div>
                  </body>
              </html>"""

entrada = open("dados.txt").read() #le o arquivo com os registros de celulares captados pelo roteador
saida = open("sso.html", "w") #saida do arquivo html

cont = entrada.count('"}') # faz a contagem dos aparelhos
i=int(0) #variavel SOMENTE para o laco de repeticao de teste

while i < 20:
    cont = random.randint(0, 400) #numero randomico SOMENTE para teste
    cont = (cont*100)/400 #descobre a porcentagem de ocupacao (400 seria o valor definido conforme o tamanho da estacao)
    percent = int(cont)
    saida.truncate(0) #limpa a pagina html
    if cont < 25:
        fundo = base64.b64encode(open('low.jpeg', 'rb').read()).decode('utf-8')
        banner = base64.b64encode(open('banner.png', 'rb').read()).decode('utf-8')
        saida.write(html_base(fundo, banner, str(percent)))
    elif cont >= 25 and cont < 50:
        fundo = base64.b64encode(open('medium.jpeg', 'rb').read()).decode('utf-8')
        banner = base64.b64encode(open('banner.png', 'rb').read()).decode('utf-8')
        saida.write(html_base(fundo, banner, str(percent)))
    elif cont >= 50 and cont < 75:
        fundo = base64.b64encode(open('high.jpeg', 'rb').read()).decode('utf-8')
        banner = base64.b64encode(open('banner.png', 'rb').read()).decode('utf-8')
        saida.write(html_base(fundo, banner, str(percent)))
    else:
        fundo = base64.b64encode(open('intense.jpeg', 'rb').read()).decode('utf-8')
        banner = base64.b64encode(open('banner.png', 'rb').read()).decode('utf-8')
        saida.write(html_base(fundo, banner, str(percent)))
             
    time.sleep(5)
    i += 1
