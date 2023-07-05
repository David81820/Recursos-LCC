<h1 style="text-align: center;">LA2 | Treino 1 | Horário</h1>

```Python

"""
Implemente uma função que calcula o horário de uma turma de alunos.
A função recebe dois dicionários, o primeiro associa a cada UC o
respectivo horário (um triplo com dia da semana, hora de início e
duração) e o segundo associa a cada aluno o conjunto das UCs em
que está inscrito. A função deve devolver uma lista com os alunos que
conseguem frequentar todas as UCs em que estão inscritos, indicando
para cada um desses alunos o respecto número e o número total de horas
semanais de aulas. Esta lista deve estar ordenada por ordem decrescente
de horas e, para horas idênticas, por ordem crescente de número.
"""

def calcHoras(inscr, ucs):
    horas = 0
    
    for cadeira in inscr:
            horas += ucs[cadeira][2]
    return horas

def verifComp(inscr, ucs):
    possible = True
    verif = []
    for cadeira in inscr:
        if not possible:                #tentar max eficiencia
            break
        else:
            verif.append(cadeira)       #tentar max eficiencia
            if cadeira not in ucs.keys():
                possible = False
                break
            else:
                for cadeira2 in inscr:  #testa compatibilidade cadeira a cadeira
                    if cadeira2 not in ucs.keys():
                        possible = False
                        break
                    if cadeira2 not in verif:  #tentar max eficiencia
                        if ucs[cadeira][0] == ucs[cadeira2][0]: # Mesmo Dia
                            #UC2 acaba antes de UC ou comeca depois
                            if (ucs[cadeira2][1] + ucs[cadeira2][2] <= ucs[cadeira][1]) or (ucs[cadeira][1] + ucs[cadeira][2] <= ucs[cadeira2][1]):
                                verif.append(cadeira2)
                                continue
                            else:
                                possible = False
                                break
                                
    return possible

def horario(ucs,alunos):
    alunosValidos = []
    
    for num, inscr in alunos.items():
        if verifComp(inscr, ucs):
            alunosValidos.append((num, calcHoras(inscr, ucs)))
            
    alunosValidos.sort(key = lambda x: (-x[1],x[0]))
    return alunosValidos

```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)