tuplas_cores = ('amarelo', 'azul', 'roxo')
listas_cores = ['amarelo', 'azul', 'roxo']

listas_cores[1] = 'branco'
listas_cores.append('vermelho')

print(tuplas_cores)
print(listas_cores)

for cor in tuplas_cores:
    print(f'Está é a cor {cor}')