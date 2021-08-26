# AES decryption function
def decryptAES(cipherAESd, cipherText):
    decryptText = cipherAESd.decrypt(cipherText).decode('utf-8')
    return decryptText

