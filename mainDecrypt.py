from RSA_decryption import *
from decryption_AES import *
from Crypto.Cipher import AES
from RSA_encryption import *

def mainDecrypt():
    # reading from files
    publicRSAKey = readingPublicKey()
    p,q = readingPQ()
    print (p,q)
    privateRSAKey = privateKeyGeneration(publicRSAKey,p,q)
    privateRSAKey = list(map(int, privateRSAKey))
    print (privateRSAKey)
    encryptedKeyCSV, cipherTextFromFile, nonceFromFile = readingFromFiles()
    # decryption of AES key with RSA decryption
    print (encryptedKeyCSV)
    decryptedKey = ''.join(decryptRSA(privateRSAKey, encryptedKeyCSV))
    print(decryptedKey)
    # decryption of AES text with key after decryption
    decryptedKey = decryptedKey.encode('utf-8')

    cipherAESd = AES.new(decryptedKey, AES.MODE_GCM, nonce=nonceFromFile)
    decrypted = decryptAES(cipherAESd, cipherTextFromFile)
    # returning decrypted text
    return decrypted


if __name__ == "__main__":
    mainDecrypt()
