```Haskell
module Ficha2 where
import Data.Char (ord)
import Data.List (partition)

-- Exercício 1

{-
a) funA [2,3,5,1] = funA (2:[3,5,1]) = 2^2 + funA [3,5,1] = 
    = 4 + funA (3:[5,1]) = 4 + 3^2 + funA [5,1] = 13 + funA (5:[1]) = 
    = 13 + 5^2 + funA [1] =  38 + funA (1:[]) = 38 + 1^2 + funA [] = 39 + 0 = 39
b) funB [8,5,12] = funB (8:[5,12]) = 8:funB [5,12] = 8:funB (5:[12]) =
    = 8:funB [12] = 8:funB (12:[]) = 8:12:funB [] = 8:12:[] = [8,12]
c) funC [1,2,3,4,5] = funC (1:2:[3,4,5]) = funC [3,4,5] = funC (3:4:[5]) =
    = funC [5] = []
d) funD "otrec" = g [] "otrec" = g [] 'o':"trec" = g 'o':[] "trec" = g ['o'] 't':"rec" =
    = g 't':['o'] "rec" = g "to" 'r':"ec" = g 'r':"to" "ec" = g "rto" 'e':['c'] = 
    = g 'e':"rto" ['c'] = g "erto" 'c':[] = g 'c':"erto" [] = "certo"
-}

-- Exercício 2

dobros :: [Float] -> [Float]
dobros [] = []
dobros (h:t) = 2*h : dobros t

numOcorre :: Char -> String -> Int
numOcorre _ [] = 0
numOcorre x (c:str) = if x==c then 1 + numOcorre x str else numOcorre x str

positivos :: [Int] -> Bool
positivos [n] = n >= 0
positivos (n:ns)
    | n < 0 = False
    | otherwise = positivos ns

positivos' :: [Int] -> Bool
positivos' = all (>=0)

soPos :: [Int] -> [Int]
soPos [n] 
    | n < 0 = []
    | otherwise = [n]
soPos (n:ns)
    | n < 0 = soPos ns
    | otherwise = n:soPos ns
soPos' ns = fst (partition (>0) ns) 

somaNeg :: [Int] -> Int
somaNeg l = case l of [n] -> if n < 0 then n else 0
                      (n:ns) -> if n < 0 then n + somaNeg ns else somaNeg ns

somaNeg' :: [Int] -> Int
somaNeg' = foldl (\acc x -> if x < 0 then acc + x else acc) 0

tresUlt :: [a] -> [a]
tresUlt l = case l of (_:b:c:d:xs) -> tresUlt (b:c:d:xs)
                      _ -> l

tresUlt' :: [a] -> [a]
tresUlt' = foldr (\x acc -> if length acc < 3 then x : acc else acc) []

segundos :: [(a,b)] -> [b]
segundos [] = []
segundos ((_,b):l) = b:segundos l

segundos' :: [(a, b)] -> [b]
segundos' = map snd

nosPrimeiros :: (Eq a) => a -> [(a,b)] -> Bool
nosPrimeiros x [(a,_)] = x == a
nosPrimeiros x (s:ss) = x == fst s || nosPrimeiros x ss

nosPrimeiros' :: (Eq a) => a -> [(a,b)] -> Bool
nosPrimeiros' x = foldl (\acc (a,b) -> x == a || acc) False

sumTriplos :: (Num a, Num b, Num c) => [(a,b,c)] -> (a,b,c)
sumTriplos [(x,y,z)] = (x,y,z)
sumTriplos ((x,y,z):ts) = (x + sumX, y + sumY, z + sumZ)
        where (sumX, sumY, sumZ) = sumTriplos ts

sumTriplos' l = (sumA, sumB, sumC)
        where sumA = sum [a | (a,_,_) <- l]
              sumB = sum [b | (_,b,_) <- l]
              sumC = sum [c | (_,_,c) <- l]

-- Exercício 3

-- Forma não recursiva:
soDigitos :: [Char] -> [Char]
soDigitos l = [digit | digit <- l, digit `elem` ['0'..'9']]

-- Forma recursiva:
soDigitos' :: [Char] -> [Char]
soDigitos' [] = []
soDigitos' (l:ls)
        | l `elem` ['0'..'9'] = l:soDigitos' ls
        | otherwise = soDigitos' ls

soDigitos'' :: [Char] -> [Char]
soDigitos'' = filter (`elem` ['0'..'9'])

minusculas :: [Char] -> Int
minusculas [] = 0
minusculas (c:str) = if c `elem` ['a'..'z'] then 1 + minusculas str
                                            else minusculas str
                                            
minusculas' :: [Char] -> Int
minusculas' = foldl (\acc x -> if x `elem` ['a'..'z'] then acc + 1 else acc) 0

-- Forma não recursiva:
nums' :: [Char] -> [Int]
nums' str = [ord num - ord '0' | num <- str, num `elem` ['0'..'9']]
-- Forma recursiva:
nums :: [Char] -> [Int]
nums [] = []
nums (c:str) = if c `elem` ['0'..'9'] then (ord c - ord '0') : nums str 
                                      else nums str

-- Exercício 4

type Polinomio = [Monomio]
type Monomio = (Float,Int)

conta :: Int -> Polinomio -> Int
-- ASSIM: OU conta n p = length selgrau n p
conta n p = length [(b,e) | (b,e) <- p, e == n]
-- OU ASSIM:
conta' :: Int -> Polinomio -> Int
conta' _ [] = 0
conta' n ((_,e):ps) = if e == n then 1 + conta' n ps else conta' n ps

grau :: Polinomio -> Int
grau [(b,e)] = e
grau ((b,e):ps) = if e > grau ps then e else grau ps

grau' :: Polinomio -> Int
grau' = maximum . map snd

selgrau :: Int -> Polinomio -> Polinomio
selgrau n p = [(b,e) | (b,e) <- p, e == n]

deriv :: Polinomio -> Polinomio
deriv [] = []
deriv ((b,e):ps) = if e > 0 then (b*fromIntegral e,e-1):deriv ps else deriv ps

calcula :: Float -> Polinomio -> Float
calcula x [] = 0
calcula x ((b,e):ps) = b*(x^e) + calcula x ps

simp :: Polinomio -> Polinomio
simp [(b,e)] = if e < 1 then [] else [(b,e)]
simp ((b,e):ps) = if e < 1 then simp ps else (b,e):simp ps

mult :: Monomio -> Polinomio -> Polinomio
mult _ [] = []
mult (b,e) ((bp,ep):ps) = (b*bp,e+ep):mult (b,e) ps

normaliza :: Polinomio -> Polinomio
normaliza [] = []
normaliza ((b,e):ps) = (sum [bs | (bs,es) <- selgrau e ps] + b,e):normaliza [(bo,eo) | (bo,eo) <- ps, eo /= e]

normaliza' :: Polinomio -> Polinomio
normaliza' [] = []
normaliza' [(b,e)] = [(b,e)]
normaliza' ((b, e) : (b2, e2) : ps)
  | e == e2 = normaliza' ((b + b2, e) : ps)
  | conta e ps == 0 = (b, e) : normaliza' ((b2, e2) : ps)
  | otherwise = normaliza' ((b, e) : ps ++ [(b2, e2)])

soma :: Polinomio -> Polinomio -> Polinomio
soma p1 p2 = normaliza (p1 ++ p2)

produto :: Polinomio -> Polinomio -> Polinomio
produto [] _ = []
produto (p:p1) p2 = soma (mult p p2) (produto p1 p2) 

ordena :: Polinomio -> Polinomio -- Esta função deu-me cabo da cabeça, foda-se, tive que ir online ver como se fazia quicksort no haskell, e é fácil pra caraças, mas eu sou deficiente e não consegui chegar a esta merda facílima sozinha!
ordena [] = []
ordena ((b,e):ps) = ordena (maisAltos ps) ++ [(b,e)] ++ ordena (maisBaixos ps)
    where maisAltos [] = []
          maisAltos ((bx,ex):xs) = if ex > e || (ex == e && bx >= b) then (bx,ex):maisAltos xs else maisAltos xs
          maisBaixos [] = []
          maisBaixos ((bx,ex):xs) = if ex < e || (ex == e && bx < b) then (bx,ex):maisBaixos xs else maisBaixos xs
{- 
ordena ((b,e):ps) = monomiosMaisAltos ++ [(b,e)] ++ monomiosMaisBaixos
        where monomiosMaisAltos = ordena [mm | mm@(bm,em) <- ps, (em > e || (em == e && bm >= b))]
              monomiosMaisBaixos = ordena [mm | mm@(bm,em) <- ps, (em < e || (em == e && bm < b))]
-}

equiv :: Polinomio -> Polinomio -> Bool
equiv p1 p2 = ordena (normaliza p1) == ordena (normaliza p2)
```
