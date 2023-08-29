a = 0

print('Equação Quadrática')
while a == 0:
  a = float(input('Digite o valor de a: '))

b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

delta = b**2 - 4*a*c

if delta < 0:
  print(f'Não há raizes reais.')
elif delta == 0:
  x = -b / (2*a)
  print(f'Há apenas uma raiz real. \nO valor da raiz é {x:.2f}.')
else:
  x1 = (-b + (delta**(1/2)))/ (2*a)
  x2 = (-b - (delta**(1/2)))/ (2*a)
  print(f'Há duas raízes. \nO valor da raiz1 é {x1:.2f} e raiz2 é {x2:.2f}.')