<h1 style="text-align: center;">LA2 | Treino 1 | Aloca</h1>

```Python

"""
Implemente uma função que dado um dicionário com as preferências dos alunos
por projectos (para cada aluno uma lista de identificadores de projecto, 
por ordem de preferência), aloca esses alunos aos projectos. A alocação
é feita por ordem de número de aluno, e cada projecto só pode ser feito
por um aluno. A função deve devolver a lista com os alunos que não ficaram
alocados a nenhum projecto, ordenada por ordem de número de aluno.
"""

def aloca(prefs):
    proj = {}
    alinv = []
    for num, ucs in sorted(prefs.items(), key = lambda x: x[0]):
        for uc in ucs:
            if uc not in proj.keys():
                proj[uc] = num
                break
        if num not in proj.values():
            alinv.append(num)
        
    sorted(alinv)
    return alinv

```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)