from  lib.scrapy_dadosAbertos import DadosAbertos

site_connect = DadosAbertos()

print(site_connect.help())

list_dep = site_connect.deputados()

de   lib.scrapy_dadosAbertos import DadosAbertos

listJson = DadosAbertos ()

para comissao em   listJson.orgaos_membros ( ' 5973 ' ):
    print (comissao [ ' nome ' ])