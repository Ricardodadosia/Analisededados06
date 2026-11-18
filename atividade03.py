total = 0 
quantidade = 0 

while True:
    valor = float(input("\ndigite o valor da despesa realizada: R$ "))

    total = total + valor 
    quantidade = quantidade + 1 
    
    continuar = input('\nQuer continuar [S/N]').upper()
    
    if continuar == "N":
         break

    print("\nResumo das despesas")
    print("quantidades de despesas:", quantidade)
    print(f"valor total das despesas: R$")   
    

    