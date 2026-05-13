# Lista para armazenar os gastos das viagens
historico_gastos = []

continuar = 's'

# Loop principal do programa
while continuar == 's':
    distancia_percorrida = int(input("Quantos KMs você percorreu? "))
    consumo_litro = int(input("Quantos KMs seu carro faz por litro? "))

    # Evita divisão por zero
    if consumo_litro <= 0:
        print("O consumo deve ser maior que zero.")
        continue

    preco_combustivel = float(input("Qual valor do litro de combustível? "))
    
    # Calcula o valor gasto na viagem
    gasto_viagem = (distancia_percorrida / consumo_litro) * preco_combustivel
    
    # Adiciona o gasto ao histórico
    historico_gastos.append(gasto_viagem)

    print(f"Você vai gastar R${gasto_viagem:.2f} nessa viagem")

    if gasto_viagem > 100:
        print("Essa viagem está ficando cara, melhor dividir a gasolina!")
    elif 50 <= gasto_viagem <= 100:
        print("O custo está razoável.")
    else:
        print("Viagem barata, aproveite!")

    continuar = input("Deseja calcular outra viagem? (s/n): ").lower()

print("Histórico de viagens:")

for gasto in historico_gastos:
    print(f"R${gasto:.2f}")

print(f"Total gasto hoje: R${sum(historico_gastos):.2f}")
