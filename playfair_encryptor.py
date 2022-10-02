# cite: https://dev.to/karanmunjani/encryption-using-playfair-cipher-in-python-24l4
import math
import random

import numpy as np
from ngram_score import ngram_score

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

ptext10 = "hide the gold in the trexe stump"

ctext10 = "BMODZ BXDNA BEKUD MUIXM MOUVI F"

TEMP = 20
STEP = 0.2
COUNT = 10000
SEED = 1
random.seed(SEED)

def playfairEncryptBigram(ptext, keyMatrix):
    np_keyMatrix = np.array(keyMatrix)
    np_char1 = np.array(ptext[0])
    np_char2 = np.array(ptext[1])

    result1 = ""
    result2 = ""

    char1_loc = np.argwhere(np_keyMatrix == np_char1)[0]
    char2_loc = np.argwhere(np_keyMatrix == np_char2)[0]

    # if in same col
    if char1_loc[1] == char2_loc[1]:
        result1 = keyMatrix[(char1_loc[0] + 1) % 5][char1_loc[1]]
        result2 = keyMatrix[(char2_loc[0] + 1) % 5][char1_loc[1]]

    # if in same row
    elif char1_loc[0] == char2_loc[0]:
        result1 = keyMatrix[char1_loc[0]][(char1_loc[1] + 1) % 5]
        result2 = keyMatrix[char1_loc[0]][(char2_loc[1] + 1) % 5]

    else:
        result1 = keyMatrix[char1_loc[0]][char2_loc[1]]
        result2 = keyMatrix[char2_loc[0]][char1_loc[1]]

    return result1 + result2


def playfairEncrypt(ptext, keyMatrix):
    ptext = ptext.replace(" ", "").upper()

    if len(ptext) % 2 == 1:
        ptext += 'Z'

    result = ""
    for i in range(0, len(ptext) - 1, 2):
        result += playfairEncryptBigram(ptext[i] + ptext[i + 1], keyMatrix)

    return result


def playfairDecryptBigram(ptext, keyMatrix):
    np_keyMatrix = np.array(keyMatrix)
    np_char1 = np.array(ptext[0])
    np_char2 = np.array(ptext[1])

    result1 = ""
    result2 = ""

    char1_loc = np.argwhere(np_keyMatrix == np_char1)[0]
    char2_loc = np.argwhere(np_keyMatrix == np_char2)[0]

    # if in same col
    if char1_loc[1] == char2_loc[1]:
        result1 = keyMatrix[(char1_loc[0] - 1) % 5][char1_loc[1]]
        result2 = keyMatrix[(char2_loc[0] - 1) % 5][char1_loc[1]]

    # if in same row
    elif char1_loc[0] == char2_loc[0]:
        result1 = keyMatrix[char1_loc[0]][(char1_loc[1] - 1) % 5]
        result2 = keyMatrix[char1_loc[0]][(char2_loc[1] - 1) % 5]

    else:
        result1 = keyMatrix[char1_loc[0]][char2_loc[1]]
        result2 = keyMatrix[char2_loc[0]][char1_loc[1]]

    return result1 + result2


def playfairDecrypt(ptext, keyMatrix):
    ptext = ptext.replace(" ", "").upper()

    result = ""
    for i in range(0, len(ptext) - 1, 2):
        result += playfairDecryptBigram(ptext[i] + ptext[i + 1], keyMatrix)

    return result


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


keyMatrix = generateKeyMatrix(key2)

print(playfairDecrypt(ctext10, keyMatrix))

bigrams = "./english_bigrams.txt"
trigrams = "./english_trigrams.txt"
quadgrams = "./english_quadgrams.txt"

bigramScorer = ngram_score(bigrams)
trigramScorer = ngram_score(trigrams)
quadgramScorer = ngram_score(quadgrams)

sampleText1 = "ATTACK THE EAST WALL OF THE CASTLE AT DAWN"
sampleText2 = "FYYFHP YMJ JFXY BFQQ TK YMJ HFXYQJ FY IFBS"

bigram_score = bigramScorer.score(sampleText1)
trigram_score = trigramScorer.score(sampleText1)
quadgram_score = quadgramScorer.score(sampleText1)


def swapRows(keyMatrix):
    firstSwap = random.randint(0,4)
    secondSwap = random.randint(0,4)


def breakPlayfair():
    bestScoreLocal = quadgramScorer.score(ctext10)
    bestScoreGlobal = bestScoreLocal

    bestKeyLocal = "ABCDEFGHIJKLMNOPQRSTUVWXY"
    bestKeyGlobal = bestKeyLocal

    ciphertext = ctext10

    keyMatrix
    for T in range(0, TEMP):
        for C in range(0, COUNT):
            deciphered = playfairDecrypt(ciphertext, keyMatrix)
            score = quadgramScorer.score(deciphered)
            dF = score - bestScoreLocal

            if dF >= 0:
                bestScoreLocal = score
            elif T > 0:
                prob = math.exp(dF / T)

            if bestScoreLocal > bestScoreGlobal:
                bestScoreGlobal = bestScoreLocal
