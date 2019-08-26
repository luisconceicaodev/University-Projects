module Descendencia
( raiz
, juntar
) where

import Data.List

data Familia = Familia {progenitor :: [String], descendentes :: [[String]]} deriving (Read,Ord)

-- Exercício 1
raiz :: String -> Familia
raiz x = Familia [x] [[""]]

-- Exercício 2

addDescendentes :: String -> Familia -> [String] -> Familia
addDescendentes prog (Familia y ys) desc = Familia (y++[prog]) (appendDesc desc ys)

appendDesc :: a -> [a] -> [a]
appendDesc i (x:xs) = x : appendDesc i xs
appendDesc i [] = i : []

juntar :: String -> Familia -> [String] -> Familia
juntar x y z = addDescendentes x y z

-- Exercício 3

showPFormat :: [[Char]] -> [Char]
showPFormat xs = foldr (++) "" (map (\str -> "" ++ str ++ "\n  ") xs)

showDFormat :: [[Char]] -> [Char]
showDFormat xs = foldr (++) "" (map (\str -> "" ++ str ++ "\n  ") xs)

formatCycle :: [[[Char]]] -> [[Char]]
formatCycle [] = []
formatCycle (x:xs) = showDFormat x : formatCycle xs

instance Show Familia where
    show (Familia progenitor descendentes) = showPFormat(progenitor) ++ (showDFormat (formatCycle(descendentes)))

-- Exercício 4

instance Eq Familia where
    Familia {progenitor=p1, descendentes=d1} == Familia {progenitor=p2, descendentes=d2} = ((length(head(d1)) == length(head(d2))) && (length(p1) == length(p2)))