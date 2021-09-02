from decryption_RSA import *
from decryption_AES import *
from Crypto.Cipher import AES
from encryption_RSA import *
from readFiles import *


def mainDecrypt():
    # reading from files
    publicRSAKey = readingPublicKey()
    encryptedKeyFromFile, cipherTextFromFile, nonceFromFile = readingEncryptedKey(),readingCipherText(),readingNonce()
    p, q = readingPQ()
    privateRSAKey = privateKeyGeneration(publicRSAKey, p, q)
    privateRSAKey = list(map(int, privateRSAKey))
    # decryption of AES key with RSA decryption
    decryptedKey = ''.join(decryptRSA(privateRSAKey, encryptedKeyFromFile))
    # decryption of AES text with key after decryption
    decryptedKey = decryptedKey.encode('utf-8')
    cipherAESd = AES.new(decryptedKey, AES.MODE_GCM, nonce=nonceFromFile)
    decryptedText = decryptAES(cipherAESd, cipherTextFromFile)
    # returning decrypted text

    return decryptedText



if __name__ == "__main__":
    mainDecrypt()
