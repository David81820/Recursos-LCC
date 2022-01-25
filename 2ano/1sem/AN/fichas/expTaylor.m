
function [soma, n]=expTaylor(x, tol)

% calcula a soma dos termos da série de potências de x para a função
% exponencial até encontrar um termo cujo valor absoluto
% é inferior a uma tolerância tol.
% n é o grau do último termo somado.

termo=1;
soma=0;
n=0;
while abs(termo)> tol
    soma = soma + termo;
    n=n+1;
    termo = termo*x/n;
end
n=n-1;


