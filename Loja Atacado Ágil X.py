print('Bem vindo a loja Atacado Ágil X')
valor_unitario = float(input('Entre com valor do produto:')) #valor unitario com valor do produto
qtd_produto = int(input('Entre com a quantidade desejada:')) #quantidade de produtos
valor_frete = 0 #frete

if 0 <= qtd_produto < 11:
  valor_frete = 30

elif 11<= qtd_produto < 101:
  valor_frete = 60

elif 101<= qtd_produto < 1001:
  valor_frete = 120

else:
  valor_frete = 240

valor_parcial = float(valor_unitario * qtd_produto)
valor_total = float(valor_parcial + float(valor_frete))
print('O valor sem frete foi: R$ {:.2f}' . format(valor_parcial))
print('O valor com frete foi: R$ {:.2f}' . format(valor_total) + ' (frete de R$ {:.2f}' . format(valor_frete) + ')')

