from  lib.scrapy_dadosAbertos import DadosAbertos

site_connect = DadosAbertos()

print(site_connect.help())

list_dep = site_connect.deputados()

de   lib.scrapy_dadosAbertos import DadosAbertos

listJson = DadosAbertos ()

ldeputados = {}
para lista em listJson.deputados ():
    nome     =   lista [ ' nome ' ]
    partido =   lista [ ' siglaPartido ' ]
    ldeputados [nome] = partido

para partido em  sorted (ldeputados.values ​​()):
    para nome em ldeputados:
        se partido == ldeputados [nome]:
            print ( " Nome: {0} , Partido: {1} " .format (nome, partido))