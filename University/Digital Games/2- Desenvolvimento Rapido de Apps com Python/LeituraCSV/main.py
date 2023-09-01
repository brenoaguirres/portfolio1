import xlrd
from modelos import Variavel

planilha = xlrd.open_workbook("dados/dicionario_pessoas.xls") # abre a planilha
primeira_aba = planilha.sheet_by_index(0)  # seleciona a aba que interessa pelo seu index
# print("Nome:", primeira_aba.name)  # nome da aba
# print("Num lin:", primeira_aba.nrows)  # numero linhas aba
# print("Num cols:", primeira_aba.ncols)  # numero colunas aba

variaveis = []
nova_variavel = None
for idx, linha in enumerate(primeira_aba.get_rows()):  # iterando sobre as linhas da planilha
    print(linha)
    primeira_celula = linha[0]  # atributos da celula -> ctype e value
    if primeira_celula.ctype == 2:  # ctype == 2 (number)
        # Nova variavel
        if nova_variavel:
            # guarda a última variável criada
            variaveis.append(nova_variavel)
        # Variaveis do construtor
        posicao_inicial = linha[0].value
        tamanho = linha[1].value
        codigo = linha[2].value
        descricao = linha[4].value
        nova_variavel = Variavel(posicao_inicial, tamanho, codigo, descricao)
        # Variaveis da primeira categoria
        categoria_tipo = linha[5].value
        categoria_descricao_tipo = linha[6].value
        nova_variavel.add_categoria({'categoria_tipo': categoria_tipo,
                                     'categoria_descricao_tipo': categoria_descricao_tipo})
    else:
        if nova_variavel:
            # Variaveis das demais categorias
            categoria_tipo = linha[5].value
            categoria_descricao_tipo = linha[6].value
            nova_variavel.add_categoria({'categoria_tipo': categoria_tipo,
                                         'categoria_descricao_tipo': categoria_descricao_tipo})

    if idx > 50:
        break

print('Total de variaveis: ', len(variaveis))
for variavel in variaveis:
    print(variavel)
    for categ in variavel.categoria:
        print('\t', categ)


