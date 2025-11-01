# Vigenere_Cipher_Crack
This program is a collaborative effort to decipher variable-length strings that have been encoded using the Vigenere cipher. Strings are accepted using the English alphabet characters "ABCDEFGHIJKLMNOPQRSTUVWXYZ", and are presumed to be written in English (all upper case) with no punctuation or spaces.


**How It works**

This program uses a mix of brute force and the chisquare method of finding the key.

1. For each potential letter of K (keylength) form columns. each column was encrypted by the same letter like the caesar cipher
2. For each column tries a shift 0-25 (representing the letters of the alphabet). for each shift ith will produce a potential plaintext word, then compares it using the frequency of what letters in the alphabet using the chi square method
3. Picks a shift with the lowest chi square for the column. converts it into a key for the letter (goes through thousands of keys)
4. decrpyts the cipher text with the best keys it can find. lowest score is the best plaintext it could find.

**Math**
if cipher text maps to the number C E {0...25} and key maps to K E {0...25} then the plain text is P = (C-K) mod 26

chai squared formula Sum((O-E)^2)/E
