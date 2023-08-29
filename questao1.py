opcao = 0
while opcao < 1 or opcao > 5:
  print('Escolha uma das opções disponíveis abaixo:\n(1)Soma\n(2)Subtração')
  print('(3)Multiplicação')
  print('(4)Divisão')
  print('(5)Sair')
  opcao = int(input('Sua escolha é: '))
  if not(1 <= opcao <= 5):
    print('Você digitou uma opção inválida.')

if opcao == 5:
  print('Você saiu do programa!')
else:
  num1 = float(input('Digite o primeiro valor: '))
  num2 = float(input('Digite o segundo valor: '))

  if opcao == 1:
    operador = '+'
    resultado = num1 + num2
  elif opcao == 2:
    operador = '-'
    resultado = num1 - num2
  elif opcao == 3:
    operador = '*'
    resultado = num1 * num2
  elif opcao == 4:
    operador = '/'
    while num2==0:
      print('O segundo valor não pode ser zero.')
      num2 = float(input('Digite novamente o segundo valor: '))
    resultado = num1 / num2

  print(f'{num1} {operador} {num2} = {resultado:.2f}')