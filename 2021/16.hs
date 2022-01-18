import Numeric 
import Data.Char (intToDigit)

hexCharToInt :: Char -> Int 
hexCharToInt = fst . head . readHex . (:[])

duplicate :: String -> Int -> String
duplicate string n = concat $ replicate n string

bin :: Int -> String
bin n | length b < 4 = duplicate "0" (4-length b) ++ b
      | otherwise = b
    where b = showIntAtBase 2 intToDigit n ""

hexToBinString :: String -> String
hexToBinString = concatMap (bin . hexCharToInt)
      

main = do
    contents <- readFile "input/16.txt"
    let binString = hexToBinString contents
    print binString
