def decryptRSA(privateKey, encryptText):
    # separate private key to x and n for calculation
    x, n = privateKey
    decryptText = [chr((char ** x) % n) for char in encryptText]
    # returning decrypted text
    return decryptText
