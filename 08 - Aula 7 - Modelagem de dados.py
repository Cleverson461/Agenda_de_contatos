AGENDA = {
    'guilherme': {
        'tel': '99999-1010',
        'email': 'contato@solyd.com.br',
        'endereco': 'av. 1'
    },
    'maria': {
        'tel': '97287-1010',
        'email': 'maria@solyd.com.br',
        'endereco': 'av. 2'
    },
    'joao': {
        'tel': '99827-1560',
        'email': 'joao@solyd.com.br',
        'endereco': 'av. 2'
    }
}

AGENDA['guilherme']['endereco'] = 'Rua das nações'
AGENDA['lucas'] = {
    'tel': '98882-2189',
    'email': 'lucas@solyd.com.br',
    'endereco': 'av. jose bonifacio'
}

# print(AGENDA['joao']['endereco'])

for contato in AGENDA:
    print(contato)
