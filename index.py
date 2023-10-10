import requests
import re
from bs4 import BeautifulSoup
try:
    resposta = requests.get("https://www.intel.com.br/content/www/br/pt/products/sku/230500/intel-core-i713700k-processor-30m-cache-up-to-5-40-ghz/specifications.html")
    site = BeautifulSoup(resposta.content, 'html.parser')
    textoFoda = site.find('div', attrs={'data-target': 'processors-specifications'}).contents
    #print(textoFoda)
    potencia = re.findall("\d{1,2}\.\d{1,2} GHz", str(textoFoda[5]))
    print(potencia)
except:
    print("algo deu errado")