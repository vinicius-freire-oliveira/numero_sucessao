count = 0 # inicializa a contagem em 0

for i in range(1, 10001): # itera sobre os números inteiros entre 1 e 10000
    count += str(i).count('1') # incrementa a contagem pelo número de vezes que o algarismo '1' aparece em cada número

print(f'O algarismo 1 aparece {count}')