<h1 style="text-align: center;">LA2 | Torneio 5 (2022/2023) | Decifrar</h1>

```Python

"""
Na cifra de Vigenère, dado um texto e uma chave (esta só com letras minúsculas), 
cada letra do texto é cifrada aplicando um desvio correspondente à posição no 
alfabeto da letra respetiva na chave. 
Por exemplo, para cifrar "BoaTarde" com a chave "ola", temos que repetidamente 
aplicar os desvios 14, 11, e 0. Como 'B'+14 == 'P', 'o'+11 == 'z', 'a'+0 == 'a',
'T'+14 == 'H', 'a'+11 == 'a', 'r'+0 = 'r', 'd'+14=='r', e 'e'+11 == 'p', o 
criptograma resultante seria "PzaHlrrp".
Implemente a função que decifra um criptograma cifrado com esta técnica.
"""


def decifrar(texto, chave):
    rep = chave * (len(texto) // len(chave)) + chave[:len(texto) % len(chave)]
    res = []
    for i in range(len(texto)):
        if texto[i].isupper():
            x = (ord(texto[i]) - ord(rep[i].upper()) + 26) % 26
            x += ord('A')
        elif texto[i].islower():
            x = (ord(texto[i]) - ord(rep[i].lower()) + 26) % 26
            x += ord('a')
        else:
            x = ord(texto[i])
        res.append(chr(x))
    return "".join(res)

```

<br>


## Testes

```Python
# 1
texto = "AyuvfnimkpcfScTsubggmtwnXG"
chave = "python"
> Resultado = "LaboratoriosDeAlgoritmiaII"

# 2
texto = "WkeppetcvftcPoEtgpnkcdFcNqoawvlecz"
chave = "lcc"
> Resultado = "LicenciaturaEmCienciasDaComputacao" 
```

[![retroceder](https://raw.githubusercontent.com/David81820/Recursos-LCC/main/Rewind.png)](https://david81820.github.io/Recursos-LCC/2ano/2sem/LA2/codigo)