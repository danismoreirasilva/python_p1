qtd = 0
while qtd==0:
  qtd = int(input('Digite a quantidade de cópias: '))

preco = 24.95 * qtd * 0.6
custoTotal = preco + 3 + (qtd-1)*0.75

print(f'O custo total é de R$ {custoTotal:.2f}')