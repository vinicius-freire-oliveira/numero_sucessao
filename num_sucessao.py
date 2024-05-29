n = int(input("Digite um número inteiro positivo: "))
a = str(input("Digite algarismo: "))
count = 0 # inicializa a contagem em 0

for i in range(1, n+1): # itera sobre os números inteiros entre 1 e o número limite digitado pelo usuário
    count += str(i).count(a) # incrementa a contagem pelo número de vezes que o algarismo '1' aparece em cada número

# Exibe a contagem total para o usuário
print(f'O algarismo {a} aparece {count} vezes na sucessão de números inteiros entre 1 e {n}.')