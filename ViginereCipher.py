#cipherKey = "" #Note: needs to be uppercase. in main file use .upper()
#keyArray = []
#cipherText = "" #Note: needs to be uppercase. in main file use .upper()
#keyLength = len(cipherKey) - 1

#if keyLength < 0: # Error handler
#    print("Error: No key")
#    exit(1)

#for c in cipherKey: # coverts the cipher key into an array
#    keyArray.append(c)

#def solver(cipher, key):
#    plain = ""
#    counter = 0
#    cipher = cipher.upper()
#    for s in cipher:
#        cipherVal = ord(s) - ord('A')
#        keyVal = ord(key[counter]) - ord('A')
#        written = (cipherVal - keyVal) % 26
#        counter += 1
 #       if counter > keyLength:
  #          counter = 0
 #       plain = plain + chr(written + ord('A'))
        #print(f"Cipher: {s}, Key letter: {key[counter]}, Counter: {counter}")

#    print(plain)


#Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
#EnglishFreq = [ 8.2, 1.5, 2.8, 4.3, 12.7, 2.2, 2.0, 6.1, 7.0, 0.15, 0.77, 4.0, 2.4, 6.7, 7.5, 1.9, 0.095, 6.0, 6.3, 9.1, 2.8, 0.98, 2.4, 0.15, 2.0, 0.074 ] 
#EnglishFreqPerc = [f/ 100.0 for f in EnglishFreq]

#def indexOfCo(string: str) -> float:
#    num = len(string)
#    count = [0] * 26
#    for c in string:
#        count[ord(c) - ord('A')] += 1
 #   numer = sum(c * (c - 1) for c in count)
 #   return numer / (num * (num -1))

#def friedmanTest(cipher: str):
#    cipher = cipherText
#    cNum = len(cipher)
#    iC = indexOfCo(cipher)
#    kr = 0.0385
#    kp = 0.067
#    k = kp - kr

#    denomiator = ((cNum - 1) * iC) - (kr * cNum) + kp
#    estimate = (k * cNum) / denomiator

#    test = max(1, int(round(estimate)))

#    print(f"Friedman Test:")
#    print(f"  Length (n): {cNum}")
#    print(f"  Index of Coincidence (IC): {iC}")
#    print(f"  Estimated key length (float): {estimate}")
#    print(f"  Estimated key length (int): {test}")

#    return test

#friedmanTest(cipherText)


