from RSA_decryption import *
from decryption_AES import *
from Crypto.Cipher import AES


def mainDecrypt():
    # reading from files
    privateKeyCSV, encryptedKeyCSV, cipherTextFromFile, nonceFromFile = readingFromFiles()
    # decryption of AES key with RSA decryption
    decryptedKey = ''.join(decryptRSA(privateKeyCSV, encryptedKeyCSV))
    # decryption of AES text with key after decryption
    decryptedKey = decryptedKey.encode('utf-8')
    cipherAESd = AES.new(decryptedKey, AES.MODE_GCM, nonce=nonceFromFile)
    decrypted = decryptAES(cipherAESd, cipherTextFromFile)
    # returning decrypted text
    return decrypted


if __name__ == "__main__":
    mainDecrypt()
