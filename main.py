# Instrução match

def http_error(status):
    match status:
        case 400:
            return 'Bad request'
        case 404:
            return 'Not found'
        case 418:
            return 'I am a teapot'
        case 401 | 403: # uma condição ou outra
            return 'Not allowed'
        case _: # operador curinga
            return 'Something is wrong with the internet'

print(http_error(401))


# Criar lista com range

nova_lista = list(range(5, 10))
print(nova_lista)



# Iterar sobre os índices de uma sequência

lista_nomes = ['Spider-Man', 'Iron-Man', "American Captain"]

for i in range(len(lista_nomes)):
    print(f'{i}: {lista_nomes[i]}')

# continuar daqui: https://docs.python.org/pt-br/3/tutorial/controlflow.html#pass-statements

