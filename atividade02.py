resposta = 'S'
vendedor = 1 
meta = 2000
soma = 0 

while resposta == 'S':
    valores_venda = float(input('informe valor da venda: '))
    percentual_meta = (valores_venda / meta) * 100 
    print(f'percentual de metas: {percentual_meta}')
    soma = valores_venda + percentual_meta

    resposta = input('quer continuar: [S/N]').upper()

print(f'valor da venda dos vendedores: {soma}') 


     

    

