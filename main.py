#Blake Marshall, Isaac Tate & Aaron Vadnais
#CISS 478
#Team Challenge 1: Vigenere Cipher 
#This program attempts to decipher a string that has been 
#encoded using the Vigenere cipher.

# alphabet setter
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# letter fequency in words taken from https://en.wikipedia.org/wiki/Letter_frequency
freq = {
    'A': .082, 'B': .015, 'C': .028, 'D': .043, 'E': .127, 'F': .022, 'G': .02, 'H': .061, 'I': .07, 'J': .0015, 'K': .0077, 'L': .04, 'M': .024, 'N': .067, 'O': .075,'P': .019, 'Q': .00095, 'R': .06, 'S': .063, 'T': .091, 'U': .028, 'V': .0098, 'W': .024, 'X': .0015, 'Y': .02,'Z': .00074
}


def solver(cipher, key):
    """_summary_

    Args:
        cipher (_type_): takes the cipher as an argument
        key (_type_): takes the key as an argument

    Returns:
        _type_: returns the plain text
    """
    plain = "" # initilizer for key
    counter = 0 # initilizer of counter
    """_summary_
    Main for loop for translation
    Takes the unicode for the letter in the sequence of characters (s), and subtracts unicode(A) to initialize
    Does the same for the key
    """
    for s in cipher:
        cVal = ord(s) - ord('A')
        kVal = ord(key[counter]) - ord('A')
        pVal = (cVal - kVal) % 26
        plain += chr(pVal + ord('A'))
        counter = (counter + 1) % len(key) # adds to the counter and mods it by the length of the key so it doesnt go above what it needs to
    return plain

def chi_square(text):
    """_summary_

    Args:
        text (_type_): takes in str as an argument

    Returns:
        _type_: returns solution to chi
    """
    total = len(text) #length of text
    counts = {c: 0 for c in alphabet} # counts how many characters are in the text
    for c in text: # for loop initilizes the frequency table for characters in alphabet
        counts[c] += 1
    chi = 0
    # for loop for chi square method that iterates through A-Z
    for l in alphabet:
        expected = freq[l] * total
        observed = counts.get(l, 0) # collects observed(l) defaults to 0 if missing. gave me error if i didnt have that check
        if expected > 0:
            chi += (observed - expected) ** 2 / expected #chi squared method
        #print(f"For letter {l}\nexpected: {expected}\nObserved: {observed}")
    return chi

def bestKey(cipher, keyLen):
    """_summary_

    Args:
        cipher (_type_): takes in string ciphertext
        keyLen (_type_): takes in key

    Returns:
        _type_: returns the key and total score of how likely it is
    """
    key = ""
    totalScore = 0
    for i in range(keyLen): # for loops takes the key length at the index i
        col = cipher[i::keyLen] #splits it into columns for each position in cipher
        #print(col)
        bestShift, bestScore = 0, 9001 # starting values of shift and best score. its over 9000!
        for shift in range(26): # tries each possible shift 0-25 for the column
            shifted = "".join(chr(((ord(c)-ord('A')-shift)%26)+ord('A')) for c in col)
            #print(shifted)
            score = chi_square(shifted)
            #print(score)
            if score < bestScore:
                bestScore = score
                bestShift = shift
        totalScore += bestScore
        key += chr(bestShift + ord('A'))
        #print(f"Keys searched: {key}\nScore: {score}\nShift: {shift}")
    return key, totalScore

def crack(cipher):
    # This works using frequency analysis of chisquared method.
    bestPlaintext = ""
    bestKeyGuess = ""
    bestScore = 1000 # lowest score is most likely the answer
    for keyLen in range(2, 9): # goes through the the key guesses (if you enable the debug in this function you can see how many keys its goes through)
                               # if the key is in the range it keeps it
        keyGuess, score = bestKey(cipher, keyLen)
        plain = solver(cipher, keyGuess)
        print(f"Potential key: {keyGuess}\nScore: {score}\nPlaintext: {plain}\n")
        if score < bestScore:
            bestScore = score
            bestPlaintext = plain
            bestKeyGuess = keyGuess
    print("=========================================================\n")
    print("Most likely solution:")
    print(" Key:", bestKeyGuess)
    print(" Plaintext:", bestPlaintext)

# This is what happens when you run the program
cipherText = input("Input cipher text to decrpyt: ")
crack(cipherText)


