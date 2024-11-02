try:
  with open('nomes.txt', 'a') as arquivo:
      arquivo.write('Davi Lucas\n')
      print(arquivo.readlines())
except Exception as error:
  print('An exception occurred')
  print(error)
  
  
# 'r' - abre para ler
# 'w' - abre para escrever / arquivo é sobrescrito
# 'a' - abre para escrever / novo conteudo é adicionado ao final do arquivo