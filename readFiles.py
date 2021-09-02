from csv import reader



def readingFileContains(filename):
    filename1 = filename
    in_file = open(filename1, "rb")
    fileToEncrypt = in_file.read()
    in_file.close()
    # returning cipher text from file
    return fileToEncrypt

# set cipher text for presentation
def readingCipherText():
    filename2 = "fileEncryptedText.csv"
    in_file = open(filename2, "rb")
    cipherTextFromFile = in_file.read()
    in_file.close()
    # returning cipher text from file
    return cipherTextFromFile


def readingPublicKey():
    filename1 = "filePublicKey.csv"
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
    filename1 = "filePublicPQ.csv"
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


# reading from all files and returning the encrypted keys and text
def readingEncryptedKey():
    filename1 = "fileCipherKeyRSA.csv"
    listToDecrypt = []
    with open(filename1, 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Iterate over each row in the csv using reader object
        for row in csv_reader:
            # row variable is a list that represents a row in csv
            listToDecrypt.append(row)
    encryptedKeyCSV = transferData(listToDecrypt)
    return encryptedKeyCSV


def readingNonce():
    filename1 = "fileNonceAES.csv"
    in_file = open(filename1, "rb")
    nonceFromFile = in_file.read()
    in_file.close()
    return nonceFromFile


# maping data to fit our needs
def transferData(listToDecrypt):
    encryptedKey = listToDecrypt[0]
    encryptedKey = list(map(int, encryptedKey))
    return encryptedKey


# get cipher text for presentation
def getCipherText():
    cipherTextFromFile = readingCipherText()
    return cipherTextFromFile
