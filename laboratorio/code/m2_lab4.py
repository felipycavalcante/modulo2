from  lib.scrapy_dadosAbertos import DadosAbertos

site_connect = DadosAbertos()

print(site_connect.help())

list_dep = site_connect.deputados()

de   lib.scrapy_dadosAbertos import DadosAbertos

listJson = DadosAbertos ()

deputado = listJson.deputado_id ( ' 73437 ' )
nome = deputado [ ' nomeCivil ' ]

despesas = listJson.deputado_despesas ( ' 73437 ' )
Para despesa em despesas:
    print ( " {2} , {3} , {0} / {1} , R $ {4} " . Formatar (despesa [ ' mes ' ], despesa [ ' ano ' ], nome, despesa [ ' tipoDespesa ' ] , despesa [ ' valorDocumento ' ]))