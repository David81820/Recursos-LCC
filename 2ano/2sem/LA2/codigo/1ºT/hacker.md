<h1 style="text-align: center;">LA2 | Treino 1 | Hacker</h1>

```Python

"""
Um hacker teve acesso a um log de transações com cartões de
crédito. O log é uma lista de tuplos, cada um com os dados de uma transação,
nomedamente o cartão que foi usado, podendo alguns dos números estar
ocultados com um *, e o email do dono do cartão.
Pretende-se que implemente uma função que ajude o hacker a 
reconstruir os cartões de crédito, combinando os números que estão
visíveis em diferentes transações. Caso haja uma contradição nos números 
visíveis deve ser dada prioridade à transção mais recente, i.é, a que
aparece mais tarde no log.
A função deve devolver uma lista de tuplos, cada um com um cartão e um email,
dando prioridade aos cartões com mais digitos descobertos e, em caso de igualdade
neste critério, aos emails menores (em ordem lexicográfica).
"""

def hacker(log):
    mail = {}
    for c,e in log:
        if e not in mail.keys():
            mail[e] = c
        else:
            cf = ""
            for i in range(0,16):
                if c[i] != '*':
                    cf += c[i]
                else:
                    cf += mail[e][i]
            mail[e] = cf
                    
    result = [(c,e) for e,c in sorted(mail.items(), key = lambda x: (x[1].count('*'), x[0]))]
    return result

```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)