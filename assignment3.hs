-- Question 1: rqsort for 'reverse quicksort'
rqsort [] = [] --function signature
rqsort (x:xs) =
 rqsort smaller ++ [x] ++ rqsort larger
 where
  smaller = [a | a <- xs, a > x]
  larger = [b | b <- xs, b <= x]

-- Question 2: remove function
remove :: Int -> [a] -> [a] --function signature
remove x ys = take (x) ys ++ drop (x + 1) ys

-- Question 3: riffle function
riffle :: [a] -> [a] -> [a] --function signature
riffle [][] = [] --base case where neither list has anything in it
riffle (x:xs) (y:ys) = x : y : riffle xs ys

-- Question 4: implement a merge sort function on blank and single-element lists. ('merge' and 'halve' functions were included in the assignment description, so I did not include them here)
msort :: Ord a => [a] -> [a] --function signature
msort [] = [] --only a blank base case
msort [x] = [x] --only a singleton base case
msort xs = merge (msort leftside) (msort rightside) where (leftside, rightside) = halve xs
