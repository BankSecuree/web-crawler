import requests
import re
import mysql.connector
from bs4 import BeautifulSoup

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="urubu100",
        password="urubu100",
        database="BankSecure"
    )
    cr = mydb.cursor()
    try:
        resposta = requests.get("https://www.tempo.com/sao-paulo.htm")
        site = BeautifulSoup(resposta.content, 'html.parser')
        res = site.find('span', attrs={'class': 'dato-temperatura changeUnitT'}).contents
        print(res[0])
        valor = int((res[0].split("°"))[0])
        
        if valor > 26:
            print("Alerta, temperatura do computador pode estar sendo influenciada pelo ambiente")
            cr.execute("INSERT INTO alertas VALUES (null, 1, 'alerta altas temperaturas ambientes', 1, 1)")
        else:
            print("Qualquer temperatura alta é provinda do computador.")
    except:
        print("erro ao conectar ao banco de dados")

        
except:
    print("algo deu errado")


