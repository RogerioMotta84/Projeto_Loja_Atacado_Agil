print('Bem vindo a loja Atacado Ágil X')

# Recebe o valor do produto e substitui a vírgula por ponto
valor_unitario = float(input('Entre com valor do produto:').replace(',', '.'))

# Recebe a quantidade de produtos
qtd_produto = int(input('Entre com a quantidade desejada:')) 

# Inicializa o valor do frete
valor_frete = 0

# Condições para definir o valor do frete
if 0 <= qtd_produto < 11:
    valor_frete = 30
elif 11 <= qtd_produto < 101:
    valor_frete = 60
elif 101 <= qtd_produto < 1001:
    valor_frete = 120
else:
    valor_frete = 240

# Calcula o valor parcial e o valor total
valor_parcial = valor_unitario * qtd_produto
valor_total = valor_parcial + valor_frete

# Exibe os resultados
print('O valor sem frete foi: R$ {:.2f}'.format(valor_parcial))
print('O valor com frete foi: R$ {:.2f} (frete de R$ {:.2f})'.format(valor_total, valor_frete))

