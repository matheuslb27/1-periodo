alunos = []
matematica = []
fisica = []
portugues = []
historia = []
lista_alunos = []
lista_distancia = []
humanas = [portugues,historia]
exatas = [matematica,fisica]

#questionario

for i in range(3):
    alunos.append(input('seu nome? > '))
    matematica.append(bool(input('você gosta de matemática? > ')))
    fisica.append(bool(input('você gosta de fisica? > ')))
    portugues.append(bool(input('você gosta de portugues? > ')))
    historia.append(bool(input('você gosta de historia? > ')))


#Distancia euclidiana

for alunoA in range(len(alunos)):
  for alunoB in range(len(alunos)):
    if alunoA != alunoB and alunoA < alunoB:
      x=alunos[alunoA] + '-' +alunos[alunoB]
      lista_alunos.append(x)
      dist = ((matematica[alunoA] - matematica[alunoB])**2+(fisica[alunoA]-fisica[alunoB])**2+(portugues[alunoA]-portugues[alunoB]**2))**0.5
      lista_distancia.append(dist)


menor  = 0
for _ in range(len(lista_distancia)):
  if lista_distancia[_] < lista_distancia[menor]:
    menor = _
print(f'Os usuário mais similares são ,{lista_alunos[menor]},portanto os dois gostariam de cursos como: engenharia ')
  
  
    
