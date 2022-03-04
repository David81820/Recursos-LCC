```Python

#--------------------------------------------------------------------------------------------------
#   ALOCA
#--------------------------------------------------------------------------------------------------

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


  
#--------------------------------------------------------------------------------------------------
#   APELIDOS
#--------------------------------------------------------------------------------------------------

'''
Defina uma função que, dada uma lista de nomes de pessoas, devolva essa lista ordenada 
por ordem crescente do número de apelidos (todos menos o primeiro nome). No caso de pessoas com o mesmo número de apelidos,
devem ser listadas por ordem lexicográfica do nome completo.
'''

def apelidos(nomes):
    nomes.sort(key = lambda x: (len(x.split()), x) )
    return nomes


  
#--------------------------------------------------------------------------------------------------
#   CRUZAMENTOS
#--------------------------------------------------------------------------------------------------

'''
Podemos usar um (multi) grafo para representar um mapa de uma cidade: 
cada nó representa um cruzamento e cada aresta uma rua.
Pretende-se que implemente uma função que lista os cruzamentos de uma cidade 
por ordem crescente de criticidade: um cruzamento é tão mais crítico quanto 
maior o número de ruas que interliga.
A entrada consistirá numa lista de nomes de ruas (podendo assumir que os nomes de ruas são únicos). 
Os identificadores dos cruzamentos correspondem a letras do alfabeto, e cada rua começa (e acaba) no cruzamento 
identificado pelo primeiro (e último) caracter do respectivo nome.
A função deverá retornar uma lista com os nomes dos cruzamentos por ordem crescente de criticidade, 
listando para cada cruzamento um tuplo com o respectivo identificador e o número de ruas que interliga.
Apenas deverão ser listados os cruzamentos que interliguem alguma rua, e os cruzamentos com o mesmo 
nível de criticidade deverão ser listados por ordem alfabética.
'''

def cruzamentos(ruas):
    cruz = {}
    for rua in ruas:
        if rua[0] not in cruz.keys():
            cruz[rua[0]] = 1
        else:
            cruz[rua[0]] += 1
        if rua[-1] not in cruz.keys():
            cruz[rua[-1]] = 1
        elif rua[0] != rua[-1]:
            cruz[rua[-1]] += 1
        
    result = list(cruz.items())
    result.sort(key = lambda x: (x[1], x[0]) )
    return result



#--------------------------------------------------------------------------------------------------
#   FATORIZA
#--------------------------------------------------------------------------------------------------

'''
Defina uma função que recebe um número positivo
e produz a soma dos seus factores primos distintos.
'''

def factoriza(n):
    soma = 0
    for i in range(2,n+1//2):
        if n == 1:
            break
        if n % i == 0:
            soma += i
            while(n%i == 0):
                n /= i
    return soma



#--------------------------------------------------------------------------------------------------
#   FREQUÊNCIA
#--------------------------------------------------------------------------------------------------

'''
Neste problem pretende-se que defina uma função que, dada uma string com palavras, 
devolva uma lista com as palavras nela contidas ordenada por ordem de frequência,
da mais alta para a mais baixa. Palavras com a mesma frequência devem ser listadas 
por ordem alfabética.
'''

def frequencia(texto):
    freq = {}
    for pal in texto.split():
        if pal not in freq.keys():
            freq[pal] = 1
        else:
            freq[pal] += 1
    
    result = [a for a,b in sorted(freq.items(), key = lambda x: (-x[1], x[0]))]
    return result



#--------------------------------------------------------------------------------------------------
#   FUTEBOL
#--------------------------------------------------------------------------------------------------

'''
Implemente uma função que calcula a tabela classificativa de um campeonato de
futebol. A função recebe uma lista de resultados de jogos (tuplo com os nomes das
equipas e os respectivos golos) e deve devolver a tabela classificativa (lista com 
as equipas e respectivos pontos), ordenada decrescentemente pelos pontos. Em
caso de empate neste critério, deve ser usada a diferença entre o número total
de golos marcados e sofridos para desempatar, e, se persistir o empate, o nome
da equipa.
'''

def tabela(jogos):
    ponts = {}
    for e1,g1,e2,g2 in jogos:
        if e1 not in ponts.keys():
            ponts[e1] = [0,0,0]
        if e2 not in ponts.keys():
            ponts[e2] = [0,0,0]
        if g1 == g2:
            ponts[e1][0] += 1
            ponts[e2][0] += 1
        elif g1>g2:
            ponts[e1][0] += 3
        else:
            ponts[e2][0] += 3
        ponts[e1][1] += g1
        ponts[e1][2] += g2
        ponts[e2][1] += g2
        ponts[e2][2] += g1
        
    result = [(x,y[0]) for x,y in sorted(ponts.items(), key = lambda x: (-x[1][0], -(x[1][1]-x[1][2]), x[0]))]
    return result



#--------------------------------------------------------------------------------------------------
#   HACKER
#--------------------------------------------------------------------------------------------------

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



#--------------------------------------------------------------------------------------------------
#   ISBN
#--------------------------------------------------------------------------------------------------

'''
Pretende-se que implemente uma função que detecte códigos ISBN inválidos. 
Um código ISBN é constituído por 13 digitos, sendo o último um digito de controlo.
Este digito de controlo é escolhido de tal forma que a soma de todos os digitos, 
cada um multiplicado por um peso que é alternadamente 1 ou 3, seja um múltiplo de 10.
A função recebe um dicionário que associa livros a ISBNs,
e deverá devolver a lista ordenada de todos os livros com ISBNs inválidos.
'''

def isbn(livros):
    inv = []
    for t, c in livros.items():
        sum = 0
        for i in range(0,13):
            sum += int(c[i])*(3,1)[i%2==0] # (False = 3, True = 1)[condition == T]
        if sum % 10 != 0:
            inv.append(t)
    inv.sort()
    return inv



#--------------------------------------------------------------------------------------------------
#   REPETE
#--------------------------------------------------------------------------------------------------

'''
Implemente uma função que determine qual a menor sequência de caracters que
contém n repetições de uma determinada palavra
'''

def repete(palavra,n):
    maxeq = 0
    for i in range(1,len(palavra)):
        if palavra[:i] == palavra[-i:]:
            maxeq = i
    final = palavra
    final += (n-1) * palavra[maxeq:]
    
    if n != 0:   #Caso para 0 repeticoes (deve haver solucoes melhores)
        return final
    else:
        return ''



#--------------------------------------------------------------------------------------------------
#   ROBOT
#--------------------------------------------------------------------------------------------------

'''
Neste problema prentede-se que implemente uma função que calcula o rectângulo onde se movimenta um robot.
Inicialmente o robot encontra-se na posição (0,0) virado para cima e irá receber uma sequência de comandos numa string.
Existem quatro tipos de comandos que o robot reconhece:
  'A' - avançar na direcção para o qual está virado
  'E' - virar-se 90º para a esquerda
  'D' - virar-se 90º para a direita 
  'H' - parar e regressar à posição inicial virado para cima
  
Quando o robot recebe o comando 'H' devem ser guardadas as 4 coordenadas (minímo no eixo dos X, mínimo no eixo dos Y, máximo no eixo dos X, máximo no eixo dos Y) que definem o rectângulo 
onde se movimentou desde o início da sequência de comandos ou desde o último comando 'H'.
A função deve retornar a lista de todas os rectangulos (tuplos com 4 inteiros)
'''

def robot(comandos):
    rect = []
    mx, my, Mx, My, x, y = 0,0,0,0,0,0
    dx,dy = 0,1
    for c in comandos:
        if c == 'H':
            rect.append( (mx,my,Mx,My) )
            mx, my, Mx, My, x, y, dx, dy = 0,0,0,0,0,0,0,1
        elif c == 'A':
            x += 1*dx
            y += 1*dy
            mx = min(x,mx)
            Mx = max(x,Mx)
            my = min(y,my)
            My = max(y,My)
        elif c == 'E':
            dx,dy = -dy,dx
        elif c == 'D':
            dx,dy = dy,-dx
    return rect


```
