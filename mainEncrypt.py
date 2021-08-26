from RSA_encryption import *
from encryption_AES import *
from Crypto.Cipher import AES
from decryption_AES import *
import secrets
import csv


def main(user_text):
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
    # list of items for writing to file #######
    itemsToFile= [cipherKey]
    # name of csv file
    filename1 = "CipherKeyRSA.csv"
    filename2 = "EncryptedText.csv"
    filename3 = "NonceAES.csv"
    # writing to csv file
    with open(filename1, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        # writing the data rows
        csvwriter.writerows(itemsToFile)
    # writing cipherText to file
    f = open(filename2, "wb")
    f.write(cipherText)
    f.close()
    # writing nonce to file
    f = open(filename3, "wb")
    f.write(nonce)
    f.close()
    # returning cipherText
    return cipherText


if __name__ == "__main__":
    main()


