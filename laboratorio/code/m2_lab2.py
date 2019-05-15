from  lib.scrapy_dadosAbertos import DadosAbertos

site_connect = DadosAbertos()

print(site_connect.help())

list_dep = site_connect.deputados()

de   lib.scrapy_dadosAbertos import DadosAbertos

list_dep = dadosAbertos ()

print ( len (list_dep.deputados ()))


para dep em list_dep.deputados ():    
    id    = dep [ ' id ' ]
    nome = dep [ ' nome ' ]

    infodep = list_dep.deputado_id ( id )
    
    mascara =  " Id: {0} \ n Nome: {1} \ n Data de Nascimento: {2} \ n Estado do Nascimento: {3} \ n E-mail: {4} \ n Sigla do Partido: {5} \ n # ------------------------------------------------ - "

    print (mascara.format (
                         id ,
                         nome,
                         infodep [ ' dataNascimento ' ],
                         infodep [ ' ufNascimento ' ],
                         infodep [ ' ultimoStatus ' ] [ ' gabinete ' ] [ ' email ' ],
                         infodep [ ' ultimoStatus ' ] [ ' siglaPartido ' ]
                         ))