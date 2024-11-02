AGENDA = {}

AGENDA['guilherme'] = {
    'telefone': '99992-8272',
    'email': 'guilherme@solyd.com.br',
    'endereco': 'Av. 1'
}

AGENDA['maria'] = {
    'telefone': '99928-1010',
    'email': 'maria@solyd.com.br',
    'endereco': 'Av. 2'
}


def mostrar_contatos():
    for contato in AGENDA:
        print(f'Nome: {contato}')
        print(f'Telefone: {AGENDA[contato]['telefone']}')
        print(f'Email: {AGENDA[contato]['email']}')
        print(f'Endereço: {AGENDA[contato]['endereco']}')
        print(100 * '-')


mostrar_contatos()
