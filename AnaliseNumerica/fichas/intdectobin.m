function bits=intdectobin(N)
% Dado (na base 10) um número N, inteiro positivo, dá a representação
% binária na forma de um vetor de bits (exercício 3.a da folha 1)

bits=[],pause  % inicializa (vazio) o vetor de bits
q=N;      % inicialização do quociente das divisões sucessivas por 2
while q>=2
    bits=[rem(q,2),bits], pause % rem(q/2) dá o resto na divisão inteira de q por 2
    q=floor(q/2);
end
bits=[q,bits]; % o bit mais à esquerda é o último quociente



