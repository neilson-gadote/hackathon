import random
import base64

entrada = open("dados.txt").read()
saida = open("sso.html", "w")

cont = entrada.count('"}')

cont = random.randint(-100, 100) + cont

if cont < 100 :
    data_uri = base64.b64encode(open('1.jpg', 'rb').read()).decode('utf-8')
    saida.write("""<html>
               <head><title>Teste</title></head>
               <body>
                <div style='float:left'>Quantidade de usuários na plataforma:"""+ str(cont) +""".</div>
                <img src='data:image/jpeg;base64,""" + data_uri + """'>
               </body>
               </html>""")
elif cont > 200 :
    data_uri = base64.b64encode(open('3.jpg', 'rb').read()).decode('utf-8')
    saida.write("""<html>
               <head><title>Teste</title></head>
               <body>
                <div style='float:left'>Quantidade de usuários na plataforma:"""+ str(cont) +""".</div>
                <img src='data:image/jpeg;base64,""" + data_uri + """'>
               </body>
               </html>""")
else :
    data_uri = base64.b64encode(open('2.jpg', 'rb').read()).decode('utf-8')
    saida.write("""<html>
               <head><title>Teste</title></head>
               <body>
                <div style='float:left'>Quantidade de usuários na plataforma:"""+ str(cont) +""".</div>
                <img src='data:image/jpeg;base64,""" + data_uri + """'>
               </body>
               </html>""")

