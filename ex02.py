# Função de Fibonacci
def x(num):
    termo1 = 0
    termo2 = 1
    while termo2 < num:
        termo3 = termo2
        termo2 = termo1 + termo2
        termo1 = termo3
    return termo2 == num

# Informar número
num = 2

# Resultado
if x(num):
    print(f'O número {num} pertence à sequência')
else:
    print(f'O número {num} não pertence')
