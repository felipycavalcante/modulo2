from  lib.scrapy_dadosAbertos import DadosAbertos

site_connect = DadosAbertos()

print(site_connect.help())

list_dep = site_connect.deputados()

de   lib.scrapy_dadosAbertos import DadosAbertos

listJson = DadosAbertos ()

para org em listJson.orgaos ():
    id    = org [ ' id ' ]
    nome = org [ ' nome ' ]
    print ( id , nome.upper ())
© 2019 GitHub , Inc.