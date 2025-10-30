cipherKey = "" #Note: needs to be uppercase. in main file use .upper()
keyArray = []
cipherText = "" #Note: needs to be uppercase. in main file use .upper()
keyLength = len(cipherKey) - 1

if keyLength < 0: # Error handler
    print("Error: No key")
    exit(1)

for c in cipherKey: # coverts the cipher key into an array
    keyArray.append(c)

def solver(cipher, key):
    plain = ""
    counter = 0
    cipher = cipher.upper()
    for s in cipher:
        cipherVal = ord(s) - ord('A')
        keyVal = ord(key[counter]) - ord('A')
        written = (cipherVal - keyVal) % 26
        counter += 1
        if counter > keyLength:
            counter = 0
        plain = plain + chr(written + ord('A'))
        #print(f"Cipher: {s}, Key letter: {key[counter]}, Counter: {counter}")

    print(plain)



