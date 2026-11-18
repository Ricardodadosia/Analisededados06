total_despesas = 0 
quantidade_despesas= 0 
continua = "S"

while True:
    valor = float(input("digite o valor da despesa realizada: R$ "))

    total = total + valor 
    quantidade = quantidade + 1 
    
    continuar = input('\nQuer continuar [S/N]').upper()
    
    if continuar == "N":
         break

    print("Resumo das despesas" {total_despesas})
    print("quantidades de despesas registrada:", {quantidade_despesas})
    print(f'("valor total das despesas:) R$" {total_despesas} )  

    
    

