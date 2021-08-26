from csv import reader


# AES decryption function
def decryptAES(cipherAESd, cipherText):
    decryptText = cipherAESd.decrypt(cipherText).decode('utf-8')
    return decryptText


# set cipher text for presentation
def readingCipherText():
    filename2 = "EncryptedText.csv"
    in_file = open(filename2, "rb")
    cipherTextFromFile = in_file.read()
    in_file.close()
    # returning cipher text from file
    return cipherTextFromFile

def readingPublicKey():
    filename1 = "PublicKey.csv"
    listToDecrypt = []
    with open(filename1, 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Iterate over each row in the csv using reader object
        for row in csv_reader:
            # row variable is a list that represents a row in csv
            listToDecrypt.append(row)
    publicKey = listToDecrypt[0]
    publicKey = list(map(int, publicKey))
    # returning cipher text from file
    return publicKey
def readingPQ():
    filename1 = "PublicPQ.csv"
    listToDecrypt = []
    with open(filename1, 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Iterate over each row in the csv using reader object
        for row in csv_reader:
            # row variable is a list that represents a row in csv
            listToDecrypt.append(row)
    publicQP = listToDecrypt[0]
    publicQP = list(map(int, publicQP))
    # returning cipher text from file
    return publicQP



# get cipher text for presentation
def getCipherText():
    cipherTextFromFile = readingCipherText()
    return cipherTextFromFile


# reading from all files and returning the encrypted keys and text
def readingFromFiles():
    filename1 = "CipherKeyRSA.csv"
    filename2 = "EncryptedText.csv"
    filename3 = "NonceAES.csv"
    listToDecrypt = []
    with open(filename1, 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Iterate over each row in the csv using reader object
        for row in csv_reader:
            # row variable is a list that represents a row in csv
            listToDecrypt.append(row)
    encryptedKeyCSV = transferData(listToDecrypt)
    in_file = open(filename2, "rb")
    cipherTextFromFile = in_file.read()
    in_file.close()
    in_file = open(filename3, "rb")
    nonceFromFile = in_file.read()
    in_file.close()
    return encryptedKeyCSV, cipherTextFromFile, nonceFromFile


# maping data to fit our needs
def transferData(listToDecrypt):
    encryptedKey = listToDecrypt[0]
    encryptedKey = list(map(int, encryptedKey))
    return encryptedKey
