-- Exercício 1

calc_h :: (Fractional a1, Integral a2) => (a1, a1) -> a2 -> a1
calc_h intr divs = (snd(intr) - fst(intr)) / fromIntegral divs

list_x :: (Enum b, Integral a, Fractional b) => (b, b) -> a -> [b]
list_x intr divs = [fst(intr), calc_h intr divs.. snd(intr)]

list_y :: (Enum t, Fractional t, Integral a1) => (t -> a2) -> (t, t) -> a1 -> [a2]
list_y func intr divs = [func x| x <- list_x intr divs]

soma_y :: (Num a, Eq a) => [a] -> a
soma_y list = head(list) + sum([2*x| x<-list, x/=head(list), x/=last(list)]) + last(list)

areaTrapeziosFixos :: (Double -> Double) -> (Double,Double) -> Int -> Double
areaTrapeziosFixos func intr divs = 0.5 * calc_h intr divs * soma_y(list_y func intr divs)

-- Exercício 2

calc_h_fixos :: Fractional a => (a, a) -> a
calc_h_fixos intr = (snd(intr) - fst(intr))/2

list_x_fixos :: (Fractional b, Enum b) => p -> (b, b) -> [b]
list_x_fixos func intr = [fst(intr), fst(intr)+calc_h_fixos intr.. snd(intr)]

list_y_fixos :: (Enum t, Fractional t) => (t -> a) -> (t, t) -> [a]
list_y_fixos func intr = [func x| x<-list_x_fixos func intr]

calc_A1 :: (Fractional a, Enum a) => (a -> a) -> (a, a) -> a
calc_A1 func intr = ((head(y) + y!!1) / 2) * (x!!1 - head(x))
 where y = list_y_fixos func intr
       x = list_x_fixos func intr

calc_A2 :: (Fractional a, Enum a) => (a -> a) -> (a, a) -> a
calc_A2 func intr = ((y!!1 + last(y)) / 2) * (last(x) - x!!1)
 where y = list_y_fixos func intr
       x = list_x_fixos func intr

calc_A3 :: (Fractional a, Enum a) => (a -> a) -> (a, a) -> a
calc_A3 func intr = ((head(y) + last(y)) / 2) * (last(x) - head(x))
 where y = list_y_fixos func intr
       x = list_x_fixos func intr

areaTrapeziosVariaveis :: (Double -> Double) -> (Double, Double) -> Double -> Double
areaTrapeziosVariaveis func intr prec
 | a3 - (a1+a2) < prec = a1+a2
 | otherwise = areaTrapeziosVariaveis func intr1 prec + areaTrapeziosVariaveis func intr2 prec
 where a1 = calc_A1 func intr
       a2 = calc_A2 func intr
       a3 = calc_A3 func intr
       intr1 = (fst(intr),snd(intr)/2)
       intr2 = (snd(intr)/2,snd(intr))