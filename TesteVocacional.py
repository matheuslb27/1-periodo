alunos = []
matematica = []
fisica = []
portugues = []
historia = []
lista_alunos = []
lista_distancia = []
humanas = [portugues, historia]
exatas = [matematica, fisica]

# questionário

for i in range(3):
    alunos.append(input('Qual o seu nome? > '))
    matematica.append(bool(input('Você gosta de matemática? (Digite True ou False) > ')))
    fisica.append(bool(input('Você gosta de física? (Digite True ou False) > ')))
    portugues.append(bool(input('Você gosta de português? (Digite True ou False) > ')))
    historia.append(bool(input('Você gosta de história? (Digite True ou False) > ')))

# Distância Euclidiana

for alunoA in range(len(alunos)):
    for alunoB in range(alunoA+1, len(alunos)):
        x = alunos[alunoA] + '-' + alunos[alunoB]
        lista_alunos.append(x)
        dist = ((matematica[alunoA] - matematica[alunoB])**2 +
                (fisica[alunoA] - fisica[alunoB])**2 +
                (portugues[alunoA] - portugues[alunoB])**2 +
                (historia[alunoA] - historia[alunoB])**2)**0.5
        lista_distancia.append(dist)

menor = 0
for i in range(len(lista_distancia)):
    if lista_distancia[i] < lista_distancia[menor]:
        menor = i

print(f'Os usuários mais similares são {lista_alunos[menor]}. Portanto, os dois gostariam de cursos como Engenharia.')
