```Haskell
----------
2)
----------
a)
dobros :: [Float] -> [Float]
dobros [] = []
dobros (h:t) = h*2 : dobros t

b)
numOcorre :: Char -> String -> Int
numOcorre _ [] = 0
numOcorre c (h:t) | h==c = 1+(numOcorre c t)
                  | otherwise = numOcorre c t

c)				  
positivos :: [Int] -> Bool
positivos [] = True
positivos (h:t) = if h>=0 then positivos t else False

d)
soPos :: [Int] -> [Int]
soPos [] = []
soPos (h:t) = if h<0 then soPos t  else h : soPos t

e)
somaNeg :: [Int] -> Int
somaNeg [] = 0
somaNeg (h:t) = if h<0 then h+somaNeg t else somaNeg t

f)
tresUlt :: [a] -> [a] 
tresUlt [] = []
tresUlt (h:t) | length(h:t)<=3 = (h:t)
              | otherwise = tresUlt t

g)
segundos :: [(a,b)] -> [b]
segundos [] = []
segundos ((a,b):t) = b : segundos t

h)
nosPrimeiros :: (Eq a) => a -> [(a,b)] -> Bool
nosPrimeiros _ [] = False
nosPrimeiros c ((a,b):t) = if c==a then True else nosPrimeiros c t

i)
sumTriplos :: (Num a, Num b, Num c) => [(a,b,c)] -> (a,b,c)
sumTriplos ((a,b,c):[]) = (a,b,c)
sumTriplos ((a,b,c):t) = ( (a+sa(sumTriplos t)), (b+sb(sumTriplos t)), (c+sc(sumTriplos t)) )

sa :: (a,b,c) -> a
sa (a,b,c) = a

sb :: (a,b,c) -> b
sb (a,b,c) = b

sc :: (a,b,c) -> c
sc (a,b,c) = c


----------
3)
----------
a)
soDigitos :: [Char] -> [Char]
soDigitos [] = []
soDigitos (h:t) | h=='1' || h=='2' || h=='3' || h=='4' || h=='5' || h=='6' || h=='7' || h=='8' || h=='9' || h=='0' = h:soDigitos t
                | otherwise = soDigitos t

b)
minusculas :: [Char] -> Int
minusculas [] = 0
minusculas (h:t) = if elem h ['a'..'z'] then 1 + minusculas t else minusculas t

c)!!!!!!!!!!!!!!!!!!!!!!!!!!!!
nums :: String -> [Int]
nums [] = []
nums (x:xs) | elem x ['0'..'9'] = (digitToInt x) : nums(xs)
            | otherwise = nums(xs)


----------
4)
----------
type Polinomio = [Monomio]
type Monomio = (Float,Int)

conta :: Int -> Polinomio -> Int
conta _ [] = 0
conta g ((f,i):t) = if g/=i || f==0 then (conta g t) else 1 + (conta g t)

grau :: Polinomio -> Int
grau [(n,g)] = g
grau ((n,g):t) = if g>(grau t) then g else grau t

selgrau :: Int -> Polinomio -> Polinomio
selgrau _ [] = []
selgrau g ((f,i):t) | g==i = (f,i) : selgrau g t
                    | otherwise = selgrau g t

deriv :: Polinomio -> Polinomio
deriv [] = []
deriv ((n,g):t) = if g>0 then (n*(fromIntegral g),g-1):(deriv t) else deriv t

calcula :: Float -> Polinomio -> Float
calcula _ [] = 0
calcula x ((n,g):t) = n*(x^g) + calcula t

simp :: Polinomio -> Polinomio
simp [] = []
simp ((n,g):t) = if g/=0 then (n,g):simp t else simp t

mult :: Monomio -> Polinomio -> Polinomio
mult _ [] = []
mult (x,y) ((n,g):t) = (x*n,y+g) : mult (x,y) t

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
ordena :: Polinomio -> Polinomio
ordena [] = []
ordena ((b,e):ps) = ordena (maisAltos ps) ++ [(b,e)] ++ ordena (maisBaixos ps)
    where maisAltos [] = []
          maisAltos ((bx,ex):xs) = if (ex > e || (ex == e && bx >= b)) then (bx,ex):maisAltos xs else maisAltos xs
          maisBaixos [] = []
          maisBaixos ((bx,ex):xs) = if (ex < e || (ex == e && bx < b)) then (bx,ex):maisBaixos xs else maisBaixos xs
          
          
OU


quicksort' [] = []
quicksort' (x:xs) =
  let smallerSorted = quicksort' [a | a <- xs, a <= x]
      biggerSorted = quicksort' [a | a <- xs, a > x]
  in  smallerSorted ++ [x] ++ biggerSorted

ordena :: Polinomio -> Polinomio
ordena lista = concat [quicksort1 $ selgrau n lista | n <- aux]
  where aux = quicksort' $ graus [ b | (a, b) <- lista]
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

equiv :: Polinomio -> Polinomio -> Bool
equiv p1 p2 = ordena p1 == ordena p2
```
