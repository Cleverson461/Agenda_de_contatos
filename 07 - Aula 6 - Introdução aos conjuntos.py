conjunto_cores = {'vermelho', 'azul', 'verde'}

conjunto_cores.add('branco')
conjunto_cores.add('vermelho')
conjunto_cores.add('branco')

conjunto_cores.remove('branco')
conjunto_cores.clear()

for cor in conjunto_cores:
    print(cor)