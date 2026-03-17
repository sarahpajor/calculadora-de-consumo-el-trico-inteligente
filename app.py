# Programa de cálculo de consumo de energia
# Autor: aparelho
# Entrada
aparelho = input("Digite o nome do aparelho:")
potencia = float(input("Digite a potencia: "))
tempo = float(input("Digite o tempo de uso: "))
# Processamento
consumoMensal = (potencia * tempo * 30) / 1000
custoMensal = consumoMensal * 0.75
# Saída
print(f"\nAparelho: {aparelho}")
print(f"Consumo Mensal: {consumoMensal:.2f} kWh")
print(f"Custo Mensal: R$ {custoMensal:.2f}")
if consumoMensal >= 100:
    print("Situação: Alto consumo")
else:
    print("Situação: Consumo normal")
