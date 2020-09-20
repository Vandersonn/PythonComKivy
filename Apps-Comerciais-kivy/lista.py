"""
print()
lista = list(range(10))
print(lista)
print()
nome = ('Vanderson')
print(nome)
print(nome[0])
print(nome[1])
print(nome[2])
print(nome[3])
print(nome[-3])
print()
print('While in used')
i = 0
while i < len(nome):
    print(nome[i])
    i +=1
print("For in use")
print()
for v in nome:
    print(v)
print('Enumerate')
for i, v in enumerate(nome):
    print(i, v)
"""
print('Dicionários ou mapas ou #tags')
linguas = {'br':'portugues', 'eua':'ingles'}
"""
print(linguas)
print(linguas['br'])
print(linguas['eua'])
print(linguas.get('es'))
print(linguas.get('br'))
print('es' in linguas)
print('br' in linguas)
linguas['es'] = 'espanhol'
print(linguas['es'])
print(linguas)
for chave in linguas:
    print(chave)
"""
for chave, valor in linguas.items():
    print(chave, valor)

for chave in linguas.keys():
    print(valor)

for valor in linguas.values():
    print(valor)