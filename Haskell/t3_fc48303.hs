module DNA
( dnaParaRna
, estabilidadePrimer
, dnaValido
) where

import Data.Char

-- Exercício 1

dnaParaRna :: [Char] -> [Char]
dnaParaRna sequence = concat (map (\seq ->
                       if seq == 'A' then "U"
                       else if seq == 'T' then "A"
                       else if seq == 'C' then "G"
                       else if seq == 'G' then "C"
                       else [seq]) seq)
                       where seq = reverse sequence

-- Exercício 2

estabilidadePrimer :: [Char] -> Double
estabilidadePrimer sequence
    | length seq <= 36  = cg_length / total_length
    | otherwise = estabilidadePrimer(first_18 ++ last_18)
    where seq = sequence
          cg_length = fromIntegral(length (filter (`elem` ['C','G']) seq))
          total_length = fromIntegral(length(seq))
          first_18 = fst(splitAt 18 seq)
          last_18 = fst(splitAt 18 $ reverse(seq))

-- Exercício 3

not_valid_char :: [Char] -> [Char]
not_valid_char = foldr f []
    where f x | elem x "ACGT" = id
              | otherwise = (x:)

checklowercase :: Foldable t => t Char -> Bool
checklowercase sequence = any isLower sequence

dnaValido :: [Char] -> Bool
dnaValido sequence
    | any (`elem` not_valid_char ['A'..'Z']) sequence == True = False
    | checklowercase sequence == True = False
    | otherwise = True
