```Python

'''
Implemente uma função que calcula o perímetro externo de uma figura.
A figura está desenhada usando o símbolo '#' num mapa quadriculado 
onde cada quadrícula tem dimensão 1x1. Assuma que a figura nunca 
irá estar encostada às margens do mapa.
'''

def perimetro(figura):
    if not figura:
        return 0

    rows = len(figura)
    cols = len(figura[0])

    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if figura[row][col] == '#':
                if row == 0 or figura[row - 1][col] != '#':  # Upper neighbor
                    perimeter += 1
                if row == rows - 1 or figura[row + 1][col] != '#':  # Lower neighbor
                    perimeter += 1
                if col == 0 or figura[row][col - 1] != '#':  # Left neighbor
                    perimeter += 1
                if col == cols - 1 or figura[row][col + 1] != '#':  # Right neighbor
                    perimeter += 1

    return perimeter

```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)