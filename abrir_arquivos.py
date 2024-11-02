try:
    with open('emails.txt') as arquivo:
        print(arquivo.readlines())
    # arquivo = open('emails.txt')
    # print(type(arquivo))
    # print(arquivo)
except FileExistsError:
    print('Arquivo não encontrado')
except:
    print('Algum erro ocorreu')
finally:
    arquivo.close()