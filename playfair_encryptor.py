# cite: https://dev.to/karanmunjani/encryption-using-playfair-cipher-in-python-24l4


key1 = "monarchybdefgiklpqstuvwxz"
key2 = "playfirexmbcdghknoqstuvwz"

ptext1 = "ATTACK"
ptext2 = "ATTACKATDAWN"
ptext3 = "ATTACKATMIDNIGHT"
ptext4 = "THE PLAYFAIR CIPHER WAS THE FIRST PRACTICAL DIGRAPH SUBSTITUTION CIPHER"
ptext5 = "THEPLAYFAIRCIPHERWASTHEFIRSTPRACTICALDIGRAPHSUBSTITUTIONCIPHER"

ctext1 = "RSSRDE"
ctext2 = "RSSRDERSBRNY"
ctext3 = "RSSRDERSAEYRKIDP"
ctext4 = "PDFLSMHGBSMDFSCFNZBXPDFGKATLTOMBSKBMTCKIMRVFLXIXSKLZSKNABEVFKM"
ctext5 = "PDFLSMHGBSMDFSCFNZBXPDFGKATLTOMBSKBMTCKIMRVFLXIXSKLZSKNABEVFKM"

ptext10 = "hide the gold in the tree stump"

ctext10 = "BMODZ BXDNA BEKUD MUIXM MOUVI F"


def playfairEncrypt(ptext):
    ptext = ptext.replace(" ", "")
    for i in range(0, len(ptext), 2):
        print()


# def playfairEncryptBigram(ptext):


# playfairEncrypt(ptext10)


def generateKeyMatrix(key):
    key = key.replace(" ", "")
    key = key.upper()
    keyMatrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    j = 0
    k = 0
    for i in range(0, len(key)):
        if j == 5:
            j = 0
            k = k + 1

        keyMatrix[k][j] = key[i]
        j = j + 1

    return keyMatrix


print(generateKeyMatrix(key2))
