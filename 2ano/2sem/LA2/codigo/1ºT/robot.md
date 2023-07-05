<h1 style="text-align: center;">LA2 | Treino 1 | Robot</h1>

```Python

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

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)