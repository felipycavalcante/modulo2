from  lib.scrapy_dadosAbertos import DadosAbertos

site_connect = DadosAbertos()

print(site_connect.help())

list_dep = site_connect.deputados()

de   lib.scrapy_dadosAbertos import DadosAbertos

list_dep = dadosAbertos ()

print ( " Numero de deputados: " , len (list_dep.deputados ()))