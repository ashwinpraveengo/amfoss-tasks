import System.IO

Prime :: Int -> Bool
Prime n
    | n <= 1 = False
    | n <= 3 = True
    | n `mod` 2 == 0 || n `mod` 3 == 0 = False
    | otherwise = all (\i -> n `mod` i /= 0 && n `mod` (i + 2) /= 0) [5,11..isqrt n]

isqrt :: Int -> Int
isqrt = floor . sqrt . fromIntegral

main :: IO ()
main = do
    putStr "Enter a value for N: "
    hFlush stdout
    input <- getLine
    let n = read input :: Int
    if n <= 1
        then putStrLn "Invalid input. N must be greater than 1."
        else do
            putStrLn $ "Prime numbers up to " ++ show n ++ " are:"
            mapM_ (\i -> if Prime i then putStr (show i ++ " ") else return ()) [2..n]
            putStrLn ""
