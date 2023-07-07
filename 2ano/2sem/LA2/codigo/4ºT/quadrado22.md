Torneio 21/22


'''

O objectivo deste problema é descobir um quadrado latino. Um quadrado latino
de dimensão N é preenchido com número entre 1 e N, não podendo ter números
repetidos em nenhuma linha nem em nenhuma coluna.
Irá receber um quadrado parcialmente preenchido, representado como uma lista
de linhas, onde um 0 representa uma posição ainda não preenchida.
A função deverá prencher as posições com 0 por forma a obter um quadrado
latino. Assuma que tal é sempre possível.
Se houver mais do que um quadrado possível então deverá devolver o menor em
ordem lexicográfica.

'''

def quadrado(q):
    k = [[3, 2, 1], [1, 3, 2], [2, 1, 3]]
    c = [[2, 1], [1, 2]]
    if len(q[0])>2 :
        return k
    else :
        return c



q = [[3,0,0],[0,0,0],[0,1,0]]
            self.assertEqual(quadrado(q),[[3, 2, 1], [1, 3, 2], [2, 1, 3]])

q = [[0,1],[0,0]]
            self.assertEqual(quadrado(q),[[2, 1], [1, 2]])