from encryption_RSA import *
from encryption_AES import *
from Crypto.Cipher import AES
from readFiles import *
from writingFiles import *
import secrets


def textEncryption(user_text):
    # print("Generating RSA public and Private keys......")
    publicRSAKey = readingPublicKey()
    # print("Generating AES symmetric key......")
    key = secrets.token_hex(16)
    # print("AES Symmetric Key: ")
    KeyAES = key.encode('utf-8')
    # getting text from user   ######
    plainText = user_text
    # object of AES encryption    #######
    cipherAESe = AES.new(KeyAES, AES.MODE_GCM)
    # unique bytes item for encrypted message and key  #######
    nonce = cipherAESe.nonce
    # encrypt text with AES encryption    #######
    cipherText = encryptAES(cipherAESe, plainText)
    # encrypt AES key with RSA encryption  #########
    cipherKey = encryptRSA(publicRSAKey, key)
    # writing to files
    writingCipherRSAKey(cipherKey)
    writingEncryptedText(cipherText)
    writingNonce(nonce)
    # returning cipherText
    return cipherText


def filesEncryption(fileName):
    # print("Generating RSA public and Private keys......")
    publicRSAKey = readingPublicKey()
    fileToEncrypt = readingFileContains(fileName)
    # print("Generating AES symmetric key......")
    key = secrets.token_hex(16)
    # print("AES Symmetric Key: ")
    KeyAES = key.encode('utf-8')
    # getting text from user   ######
    plainText = str(fileToEncrypt)
    # object of AES encryption    #######
    cipherAESe = AES.new(KeyAES, AES.MODE_GCM)
    # unique bytes item for encrypted message and key  #######
    nonce = cipherAESe.nonce
    # encrypt text with AES encryption    #######
    cipherText = encryptAES(cipherAESe, plainText)
    # encrypt AES key with RSA encryption  #########
    cipherKey = encryptRSA(publicRSAKey, key)
    # writing to files
    writingCipherRSAKey(cipherKey)
    writingEncryptedText(cipherText)
    writingNonce(nonce)
    # returning cipherText
    return cipherText

if __name__ == "__main__":
    textEncryption()


