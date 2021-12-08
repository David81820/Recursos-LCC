```Haskell
1

myenumFromTo :: Int -> Int -> [Int]
myenumFromTo a b = if (a<=b) then (a : (myenumFromTo (a+1) b) ) else []

----------------------------------------------------------------------------

2

enumFromThenTo :: Int -> Int -> Int -> [Int]
enumFromThenTo x y z = if (x<=z) then (x : (enumFromThenTo y (y+(y-x)) z)) else []

--------------------------------------------------------------------------------------

3

junta :: [a] -> [a] -> [a]
junta [] lista2 = lista2
junta lista1 [] = lista1
junta (h:t) lista2 = (h : (junta t lista2))

-------------------------------------------------

4


posLis :: [a] -> Int -> a
posLis (h:t) 0 = h
posLis (h:t) n = posLis t (n-1)

---------------------------------------

5

reverse' :: [a] -> [a]
reverse' [] = []

reverse' list = aux list [] where
        aux [] new = new
        aux (h:t) new = aux t (h:new)

OU

reverse' (h:t) = reverse' t ++ [h]

-------------------------------------------

6

take' :: Int -> [a] -> [a]
take' 0 l = []
take' n [] = []
take' n (h:t) = h : (take' (n-1) t)

---------------------------------------------

7

drop' :: Int -> [a] -> [a]
drop' 0 l = l
drop' n [] = []
drop' n (h:t) = drop' (n-1) t

------------------------------------------

8

zip' :: [a] -> [b] -> [(a,b)]
zip' [] l2 = []
zip' l1 [] = []
zip' (h:t) (a:b) = (h,a) : zip' t b

------------------------------------------

9

elem' :: Eq a => a -> [a] -> Bool
elem' n [] = False
elem' n (h:t) = if n==h then True else elem' n t

-------------------------------------------------------

10

replicate' :: Int -> a -> [a]
replicate' 0 x = []
replicate' n x = x : replicate' (n-1) x

---------------------------------------------

11

intersperse :: a -> [a] -> [a]
intersperse n [] = []
intersperse n [x] = [x]
intersperse n (h:t) = h : n : intersperse n t

----------------------------------------------------

12

group :: Eq a => [a] -> [[a]]
group [] = [[]]
group (h:t) = aux [h] t
             where
               aux x [] = [x]
               aux x (h:t) = if elem h x then aux (h:x) t else x : aux [h] t

---------------------------------------------------------------------------------

13

concat' :: [[a]] -> [a]
concat' [] = []
concat' (h:t) = h ++ concat' t

---------------------------------------

14

inits :: [a] -> [[a]]
inits [] = [[]]
inits list = aux list [] where
   aux [] end = [end]
   aux (h:t) list = list : aux t (list ++ [h])

---------------------

15

tails :: [a] -> [[a]]
tails [] = [[]]
tails (h:t) = (h:t) : tails t

------------------------------------

14

isPrefixOf :: Eq a => [a] -> [a] -> Bool
isPrefixOf [] l2 = True
isPrefixOf l1 [] = False
isPrefixOf (h:t) (x:y) = if h==x then isPrefixOf t y else False

----------------------------------------------------------------------

17

isSuffixOf :: Eq a => [a] -> [a] -> Bool
isSuffixOf [] l2 = True
isSuffixOf l1 [] = False
isSuffixOf l1 l2 = if (last l1)==(last l2) then isSuffixOf (init l1) (init l2) else False

-----------------------------------------------------------------------------------------------

18

isSubSeqOf :: Eq a => [a] -> [a] -> Bool
isSubSeqOf [] list = True
isSubSeqOf seq [] = False
isSubSeqOf (a:b) (h:t) = if a==h then isSubSeqOf b t else isSubSeqOf (a:b) t

----------------------------------------------------------------------------------

19


elemIndices :: Eq a => a -> [a] -> [Int]
elemIndices n [] = []
elemIndices n list = aux n list 0 where
   aux _ [] _ = []
   aux n (h:t) pos = if n==h then pos : aux n t (pos+1) else aux n t (pos+1)

--------------------------------------------------------------------------------------------------

20

nub :: Eq a => [a] -> [a]
nub [] = []
nub lista = aux lista [] where
   aux [] n = n
   aux (h:t) n = if (elem h n == False) then aux t (n++[h]) else aux t n

-------------------------------------------------------------------------------------

21

delete' :: Eq a => a -> [a] -> [a]
delete' n [] = []
delete' n (h:t) = if n==h then t else h : delete' n t

-------------------------------------------------------------

22

removePrimeiras :: Eq a => [a] -> [a] -> [a]
removePrimeiras [] [] = []
removePrimeiras [] l2 = l2
removePrimeiras (a:b) (h:t) = if a==h then removePrimeiras b t else h : removePrimeiras b t

--------------------------------------------------------------------------------------------------

23

union :: Eq a => [a] -> [a] -> [a]
union [] l2 = l2
union l1 [] = l1
union l1 (a:b) = if elem a l1 then union l1 b else union (l1++[a]) b

-------------------------------------------------------------------------

24

intersect :: Eq a => [a] -> [a] -> [a]
intersect [] l2 = []
intersect l1 [] = []
intersect (h:t) l2 = if (elem h l2 == True) then h : (intersect t l2) else intersect t l2

-----------------------------------------------------------------------------------------------

25

insert :: Ord a => a -> [a] -> [a]
insert n [] = [n]
insert n (h:t) = if n > h then h : insert n t else n : (h:t)

----------------------------------------------------------------

26

unwords' :: [String] -> String
unwords' [] = ""
unwords' [x] = x
unwords' (h:t) = h ++ " " ++ unwords' t

---------------------------------------------

27

unlines' :: [String] -> String
unlines' [] = []
unlines' (h:t) = h ++ "\n" ++ unlines' t

--------------------------------------------

28

pMaior :: Ord a => [a] -> Int
pMaior list = aux 0 list  where
 aux pos [] = pos
 aux pos (h:t) = if h == maximum (h:t) then pos else aux (pos+1) t

------------------------------------------------------------------------

29

temRepetidos :: Eq a => [a] -> Bool
temRepetidos [] = False
temRepetidos (h:t) = if (elem h t) then True else temRepetidos t

------------------------------------------------------------------------

30

algarismos :: [Char] -> [Char]
algarismos [] = []
algarismos (h:t) = if ((h>='0') && (h<='9')) then h : algarismos t else algarismos t

------------------------------------------------------------------------------------------

31

posImpares :: [a] -> [a]
posImpares [] = []
posImpares [x] = []
posImpares [x,y] = [y]
posImpares (h:s:t) = s : posImpares t

---------------------------------------------

32

posPares :: [a] -> [a]
posPares [] = []
posPares [x] = []
posPares [x,y] = [x]
posPares (h:s:t) = h : posPares t

-----------------------------------------

33

isSorted :: Ord a => [a] -> Bool
isSorted [] = True
isSorted [x] = True
isSorted (h:s:t) = if h<=s then isSorted (s:t) else False

--------------------------------------------------------------

34

iSort :: Ord a => [a] -> [a]
iSort [] = []
iSort (h:t) = insert h (iSort t)

insert :: Ord a => a -> [a] -> [a]
insert x [] = [x]
insert a (x:y) | a<=x = a : insert x y
               | otherwise = x : insert a y

---------------------------------------------------

35

menor :: String -> String -> Bool
menor "" s2 = True
menor s1 "" = False
menor s1 s2 = if (len s1)<(len s2) then True else False

len :: String -> Int
len str = length str

------------------------------------------------------------

36

elemMSet :: Eq a => a -> [(a,Int)] -> Bool
elemMSet e [] = False
elemMSet e ((x,y):z) = if e==x then True else elemMSet e z

----------------------------------------------------------------

37

lengthMSet :: [(a,Int)] -> Int
lengthMSet [] = 0
lengthMSet ((x,y):z) = y + lengthMSet z

----------------------------------------------

38

converteMSet :: [(a,Int)] -> [a]
converteMSet [] = []
converteMSet ((x,y):z) = if y>0 then x : converteMSet ((x,y-1):z) else converteMSet z

--------------------------------------------------------------------------------------------

39

insereMSet :: Eq a => a -> [(a,Int)] -> [(a,Int)]
insereMSet e [] = [(e,1)]
insereMSet e ((x,y):z) | e==x = ((x,y+1):z)
                       | otherwise = (x,y) : insereMSet e z

----------------------------------------------------------------

40

removeMSet :: Eq a => a -> [(a,Int)] -> [(a,Int)]
removeMSet e [] = []
removeMSet e ((x,y):z) | e==x = (if y>1 then ((x,y-1):z) else z)
                       | otherwise = (x,y) :  removeMSet e z

---------------------------------------------------------------------

41 - COPIADA

constroiMSet :: Ord a => [a] -> [(a,Int)]
constroiMSet [] = []
constroiMSet s = aux [] s
 where
  aux b [] = b
  aux b (h:t) = aux (insereMSet h b) t


---------------------------------------------

42 - COPIADA

partitionEithers' :: [Either a b] -> ([a],[b])

partitionEithers' l = (lefts l, rights l)

-------------------------------------------------

43 - COPIADA

catMaybes' :: [Maybe a] -> [a]

catMaybes' [] = []

catMaybes' (Just x : t) = x:catMaybes' t

catMaybes' (Nothing :t) = catMaybes' t

```
