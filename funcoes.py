def hero(name, origin='Marvel', partner='None'):
    return f'Name: {name},\n' \
           f'Origin: {origin},\n' \
           f'Partner: {partner}.'

print(hero('Hulk'))
print('')
print(hero('Iron man', partner='Spider-man'))
print('')
print(hero('Flash', 'DC'))
print('')

print('')

def starwars(name, **partners): # **args em uma função retorna um dicionário
    print(f'Name: {name}')
    if len(partners) > 0:
        for kw in partners:
            print(f'{kw}: {partners[kw]}')

starwars('R2D2')
print('')
starwars('Leia Princess', partner_name='Luke Skywalker', partner_starship='x-wing')