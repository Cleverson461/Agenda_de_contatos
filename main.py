AGENDA = {}


def mostrar_contatos():
    if AGENDA:
        for contato in AGENDA:
            buscar_contato(contato)
    else:
        print('>>> Agenda Vazia <<< ')


def buscar_contato(contato):
    try:
        print(f'Nome: {contato.title()}')
        print(f'Telefone: {AGENDA[contato]['telefone']}')
        print(f'Email: {AGENDA[contato]['email']}')
        print(f'Endereço: {AGENDA[contato]['endereco']}')
        print(100 * '-')
    except KeyError:
        print('>>> Contato inexistente')
    except Exception as error:
        print('>>> Um erro inesperado ocorreu')
        print(error)


def ler_detalhes_contato():
    telefone = input('Digite o nome do telefone: ')
    email = input('Digite o nome do email: ')
    endereco = input('Digite o nome do endereço: ')
    return telefone, email, endereco


def incluir_editar_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco
    }
    salvar()
    print()
    print(f'>>> Contato {contato.title()} adicionado/editado com Sucesso! <<<')
    print()


def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        salvar()
        print()
        print(f'>>> Contato {contato.upper()} excluido Sucesso! <<<')
        print()
    except KeyError:
        print('>>> Contato inexistente')
    except Exception as error:
        print('>>> Um erro inesperado ocorreu')
        print(error)


def exportar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'w') as arquivo:
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write(
                    f'{contato} - {telefone} - {email} - {endereco}\n')
        print('>>> Agenda exportada com sucesso.')
    except Exception as error:
        print('>>>> Algum erro ocorreu ao exportar contatos')
        print(error)


# def importar_contatos(nome_do_arquivo):
    # try:
    #     with open(nome_do_arquivo, 'r') as arquivo:
    #         linhas = arquivo.readlines()
    #         for linha in linhas:
    #             detalhes = linha.strip().split(',')

    #             nome = detalhes[0]
    #             telefone = detalhes[1]
    #             email = detalhes[2]
    #             endereco = detalhes[3]

    #             incluir_editar_contato(nome, telefone, email, endereco)
    # except FileNotFoundError:
    #     print('>>> Arquivo não encontrado')
    # except Exception as error:
    #     print('>>> Algum erro inesperado ocorreu')
    #     print(error)

def importar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')
                
                if len(detalhes) >= 4:  # Verifica se há pelo menos 4 itens na linha
                    nome = detalhes[0]
                    telefone = detalhes[1]
                    email = detalhes[2]
                    endereco = detalhes[3]

                    incluir_editar_contato(nome, telefone, email, endereco)
                else:
                    print(f'>>> Linha inválida encontrada no arquivo: {linha.strip()}')
    except FileNotFoundError:
        print('>>> Arquivo não encontrado')
    except Exception as error:
        print('>>> Algum erro inesperado ocorreu')
        print(error)


def salvar():
    exportar_contatos('database.csv')


def carregar():
    try:
        with open('database.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')

                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                AGENDA[nome] = {
                    'telefone': telefone,
                    'email': email,
                    'endereco': endereco,
                }
        print('>>>> Database carregado com sucesso')
        print('>>>> {} contatos carregados'.format(len(AGENDA)))
    except FileNotFoundError:
        print('>>>> Arquivo não encontrado')
    except Exception as error:
        print('>>>> Algum erro inesperado ocorreu')
        print(error)


def imprimir_menu():
    print(100 * '-')
    print('1 - Mostrar todos os contatos da agenda')
    print('2 - Buscar contato')
    print('3 - Incluir contato')
    print('4 - Editar contato')
    print('5 - Excluir contato')
    print('6 - Exportar contato CSV')
    print('7 - Importar contato CSV')
    print('0 - Fechar agenda')
    print(100 * '-')


# INICIO DO PROGRAMA
carregar()
while True:
    imprimir_menu()

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        mostrar_contatos()
    elif opcao == '2':
        contato = input('Digite o nome do contato: ')
        buscar_contato(contato)
    elif opcao == '3':
        contato = input('Digite o nome do contato: ')
        try:
            AGENDA[contato]
            print(f'>>> Contato já existente')
        except KeyError:
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, telefone, email, endereco)
    elif opcao == '4':
        contato = input('Digite o nome do contato: ')
        try:
            AGENDA[contato]
            print(f'>>> Editando o contato: {contato}')
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, telefone, email, endereco)
        except KeyError:
            print('>>> Contato inexistente')
    elif opcao == '5':
        contato = input('Digite o nome do contato: ')
        excluir_contato(contato)
    elif opcao == '6':
        nome_do_arquivo = input('Digite o nome do arquivo a ser exportado: ')
        exportar_contatos(nome_do_arquivo)
    elif opcao == '7':
        nome_do_arquivo = input('Digite o nome do arquivo a ser importado: ')
        importar_contatos(nome_do_arquivo)
    elif opcao == '0':
        print('>>> Fechando o programa! <<<')
        break
    else:
        print('>>> Opção inválida. <<<')
