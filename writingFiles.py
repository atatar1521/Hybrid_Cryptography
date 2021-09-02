import csv


def writingCipherRSAKey(cipherKey):
    # list of items for writing to file #######
    itemsToFile = [cipherKey]
    # name of csv file
    filename1 = "fileCipherKeyRSA.csv"
    # writing to csv file
    with open(filename1, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        # writing the data rows
        csvwriter.writerows(itemsToFile)


def writingEncryptedText(cipherText):
    filename2 = "fileEncryptedText.csv"
    # writing cipherText to file
    f = open(filename2, "wb")
    f.write(cipherText)
    f.close()

def txtWritingFile(file):
    filename3 = "fileDecrypt.txt"
    # writing nonce to file
    f = open(filename3, "wb")
    f.write(file)
    f.close()


def writingNonce(nonce):
    filename3 = "fileNonceAES.csv"
    # writing nonce to file
    f = open(filename3, "wb")
    f.write(nonce)
    f.close()


def writingPublicKey(list1):
    filename1 = "filePublicKey.csv"
    itemsToFile = [list1]
    with open(filename1, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        # writing the data rows
        csvwriter.writerows(itemsToFile)


def writingPublicPQ(list2):
    filename2 = "filePublicPQ.csv"
    itemsToFile = [list2]
    with open(filename2, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        # writing the data rows
        csvwriter.writerows(itemsToFile)