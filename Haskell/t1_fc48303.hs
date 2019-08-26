-- Aluno: Luís Miguel Duarte Conceição; nº48303

-- Exercício A-1

cut :: Integral x => x -> [x]
cut 0 = []
cut x = cut (div x 10) ++ [mod x 10]

inacreditaveis :: [Integer]
inacreditaveis = [x | x <-[1..999],  (x `mod` sum(cut x)) == 0] 

--Exercício A-2

raiocinco :: Integer -> Bool
raiocinco n = notElem (n+1) inacreditaveis && notElem (n+2) inacreditaveis && notElem (n+3) inacreditaveis && notElem (n+4) inacreditaveis && notElem (n+5) inacreditaveis && notElem (n-1) inacreditaveis && notElem (n-2) inacreditaveis && notElem (n-3) inacreditaveis && notElem (n-4) inacreditaveis && notElem (n-5) inacreditaveis

rarosInacreditaveis :: [Integer]
rarosInacreditaveis = [x | x<-inacreditaveis, raiocinco x]

{- 
Exercício B-1
A função f recebe dois parametros do tipo Bool: a , b.
Se a e b forem iguais retorna 1, se não, retorna 0. -}
f :: Bool -> Bool -> Integer
f a b = if (a == b)
        then 1
        else 0

{- 
Exercício B-2
A função g recebe dois parametros: a , b (que podem ser de qualquer tipo).
Esta função retorna um tuple de listas, ou seja, retorna a e b em lista dentro de um tuple. -}
g :: a -> b -> ([a], [b])
g a b = ([a], [b])

{- 
Exercício B-3
A função h recebe dois parametros: t , x (o primeiro é do tipo Char e o segundo é a variável x).
Esta função retorna True se o Char t: 
	- Vir antes de "n" (segundo a ordem alfabética);
	- For igual a "n";
	- For um número.
Retorna False se o Char t:
	- Vir depois de "n" (segundo a ordem alfabética). -}
h :: Ord t =>t -> [t] -> Bool
x = "n"
h t x = [t] <= x
