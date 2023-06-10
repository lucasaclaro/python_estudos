list_names = ['Spider-Man', 'Iron Man', "American Captain"]
for i in range(len(list_names)):
    print(f'{i}: {list_names[i]}')

print('')

heroes = {'spiderman': 'venom', 'batman': 'joker'}
for k, v in heroes.items():
    print(f'Hero: {k}, Villain: {v}.')

print('')

for i, v in enumerate(['zero', 'one', 'two']):
    print(f'Position {i}, Value: {v}.')

print('')

questions = ['name', 'color', 'age']
answers = ['Peter Parker', 'red', 22]
for q, a in zip(questions, answers):
    print(f'{q}: {a}')

print('')

# Maneira reversa
for i in reversed(range(1, 10, 2)):
    print(i)

print('')

# Maneira ordenada
basket = ['orange', 'apple', 'watermelon']
for i in sorted(basket):
    print(f'Fruit: {i}')

print('')

# Eliminar elementos duplicados

basket = ['apple', 'watermelon', 'watermelon', 'pear']
for i in set(basket):
    print(f'Fruit: {i}')

