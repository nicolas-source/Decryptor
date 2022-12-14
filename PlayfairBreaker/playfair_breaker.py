# cite: https://dev.to/karanmunjani/encryption-using-playfair-cipher-in-python-24l4
import math
import random

import numpy as np
from ngram_score import ngram_score
from freq_analysis import bigram_freq

key1 = "monarchybdefgiklpqstuvwxz"
key2 = "playfirexmbcdghknoqstuvwz"

ptext0 = "Certainlycommaansweredthescarecrowdothowdoyoudoimpretxtywelxlcommathankyoucomxmarepliedxdorothypolitelydothowdoyoudoimnotfexelingwellcommasaidthescarecrowcomxmawithasmilecomxmaforitisverytediousbeingperchedupherenightanddaytoscareawaycrowsdotcantyougetdownaskedxdorothydotnocomxmaforthispoleisxstuckupmybackdotifyouwillpleasetakeawaythepoleishalxlbegreatlyobligedtoyoudotdorothyreachedupbotharmsandliftedthefigureofxfthepolecomxmaforcommabeingstufxfedwithstrawcomxmaitwasquitelightdotthankyouverymuchcomxmasaidthescarecrowcomxmawhenhehadbexensetdownonthegrounddotifeellikeanewmandotdorothywaspuzxzledatthiscomxmaforitsoundedquexertohearastufxfedmanspeakcommaandtosexehimbowandwalkalongbesideherdotwhoareyouaskedthescarecrowxwhenhehadstretchedhimselfandyawneddotandwhereareyougoingmynameisdorothycommasaidthegirlcommaandiamgoingtotheemeraldcitycommatoaskthegreatoztosendmebacktokansasdotwhereistheemeraldcityheinquiredxdotandwhoisozwhycomxmadontyouknowshereturnedcomxmainsurprisedotnocommaindeeddotidontknowanythingdotyouseecommaiamstufxfedcommasoihavenobrainsatalxlcommaheansweredsadlydotohcomxmasaiddorothycommaimawfulxlysorxryforyoudotdoyouthinkcommaheaskedcommaifigototheemeraldcitywithyoucomxmathatozwouldgivemesomebrainsicanxnotxtelxlcommashereturnedcommabutyoumaycomewithmecommaifyoulikedotifozwilxlnotgiveyouanybrainsyouwillbenoworseoffthanyouarenowdotxthatistruecomxmasaidthescarecrowdotyouseecommahecontinuedconfidentialxlycomxmaidontmindmylegsandarmsandbodybeingstuffedcommabecauseicanxnotgethurtdotifanyonetreadsonmytoesorsticksapinintomecommaitdoesntmatxtercommaforicantfeelitdotbutidonotwantpeopletocalxlmeafoolcomxmaandifmyheadstaysstuffedwithstrawinsteadofwithbrainscommaasyoursiscommahowamievertoknowanythingiunderstandhowyoufexelcomxmasaidthelittlegirlcommawhowastrulysorryforhimdotifyouwilxlcomewithmeilxlaskoztodoallhecanforyoudotxthankyoucomxmaheansweredgratefullydotxtheywalkedbacktotheroadxdotdorothyhelpedhimoverthefencecommaandtheystartedalongthepathofyelxlowbrickfortheemeraldcitydottotodidnotlikethisadditiontothepartyatfirstdothesmelledaroundthestuffedmanasifhesuspectedtheremightbeanestofratsinthestrawcomxmaandheoftengrowledinanunfriendlywayatthescarecrowdotdontmindtotocommasaiddorothytohernewfriendxdotheneverbitesdotohcomxmaimnotafraidcommarepliedthescarecrowdothecanthurtthestrawdotdoletmecarxrythatbasketforyoudotishallnotminditcomxmaforicantgetxtiredxdotilxltellyouasecretcommahecontinuedcommaashewalkedalongdotthereisonlyonethingintheworldiamafraidofdotwhatisthataskeddorothythemunchkinfarmerwhomadeyounocomxmaansweredthescarecrowitsalightedmatch"
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

ctext0 = "XCLEITISOXZCTKVIRNRDRPLAXRTGDREFDQOYLADQOYZYRZHQEKDREMXHERSTFTZCTKLAVIVZZFFGTMTKDRARWTYEOYFDLADVHFTLTRZOHCDYEPYZZFOYBTQYCLCMTRWBPQTRFTZCTKLVWHLAXRTGDREFDQFGTMTKQWLAVLTBRTFGTMTKOGLWLTYNRDHXRPQHLUWMWBVGRDTORPRKDTDRBWAOLIWYHPHXYFTGDRPIVHEFDQRYHCTGIXZYFKCEOYQBVLPMYEOYFDLAZOHCQYFGTMTKOGLEATRVHFTWYSLXFMBZKEZNGTPZHCQLZYRBTHRARTVLCEPATPIPHXDTGDRTNLAISTUICPDRILSHZQHTPCHEYZZFOYEHDFHCDZDRGTDTZRKWHCAIUELVWYHTLCRPLACRQALFCDSCLCDTGDRTFGTMTKOGFEZCTKWMWBVFMLSCRCPETLYLELPIFGTMTKTLIPFNLBECHTAOEHHCLAVIVZZFPXSDUZTOFGTMTKLVWHLAXRTGDREFDQFGTMTKIDXWDTAIZWCMXWRXEHDQQYIXDTPFZFWYOYLTRCTRHTPMVIRETKWYHCOYFDLADNVLKRYMHURPILLANLFGTMTKOGLWXLZFWYRPBFCMRDCHDTPLVLMLSCRCZEVIRVTPGMZCTKVIHEYFCMTDBTQZIPWYIPUAIHYQKQXRWHTDRDOYEIDYPLXDZFVLPMHEDTFXPLCXFDNEIDXWDTAIYRELCETORPATXUTRLGWYHVQBRPOYLIWYIDRDTPDRZYFKHQQVXZIVTCNLOYFDLAOXZCTKLVWHLACPWLFTZCTKVIHWKTQGWBACHCDTCTRDIHOETLOXZCTKCHVLAMDTPFTPCHHMYFXWZEMWGTAMZGVILVRYHCIDRDTWLXDTCTRDIHOETLZDTWBNLBDRYEOYLIWYIDHQFYDBDZFGTMTKOYIXZYZBQYNRDTDRMLSWRPFGTMTKWBULDWLWRXOYXIGFZCTKWBPRRPOYLTOYIXVBDQVIHXATQVOYXHZFRXCXZCTKTIXUMLSCRCOEZCTKFYTAPKXWZQLPWBLVLISTFTZCTKDTVIRNRDRPLVHRZOHCYDFGTMTKLVWHOYFDLAOXZCTKBTPISLSTSHFYSESDOGSDZFOYEHYZZFLAWBGMZCTKDTVLPMOEZCTKQLQAHCHCDTCTRDIHOETLDNTLDZZFFGTMTKLAILYHQDLROPNACTXRZCMWLPWBLNTGXSQYEMECSTFTZCTKLYRDCELFWXOEZCTKMZXHZFTKOXZCRETLZTCXZCTKQLZYLRBARPHCQLYHQWSTSIHCAQPXZYLKXVWUITXYZYRBTHUIXWDQDFRXGOLCAIXVZFPLXWDQOYEMLAILNLELRMFGTMTKLVWHLAXRTGDREFDQOYXHZFRXCXZCTKDTFGIXWBRMOEYQLQPRIXTISTSHFGTMTKWHYQETWBZEHSCPLVWYPLXUVIZWYOZNTWQVLXLSRCOEZCTKWMTGLUTWTGXSQYCACEZLLEOYLTLGXVYQCEDRPHFYBXHXDCFYFULTMGLVAWBWIXZCCXZCTKTLOYXRIXTKEMECFEZCTKOGLWTGIXRCTRTLOYMILMWHYQHCIPIXWRDGRTCHTGSTUTTPOGHFFGTMTKVIHWUCZDTPYRLIVYLXLSRCPETLYLELPIWBLXTPOYRQTLZILPWBFXZCTKVLZYLFLNFXZCTKDYIPTBXPRDCHVBDQVIHXATQVBLWYRDLXVIODDQZYLSCMTRFGTMTKLVWHLATRTLLHCPWLFTZCTKIDDQVLELLRVYDFSDOGLDBTOYLTSOZFQWSTFTZCRETLZTTWSTHIUVYHCHOYIHHACXVIOGSDZFOYEMLAVIVZZFFGTMTKDTVIRNRDRPPFILCRLRSHOYEMLAXDIPUARPIKMGCHLARDHGYEOYEHDFHCDZDTRARPATCZPXLEDTRCQXCXZCTKVIHEDTVYLILERPIHYQACDTGPLAGODXSTFHQILWMGOGLEDTCTRDIHOETLZOHCCHCHHWYWHCHTPMLANLPHHWLTYQCHLARWPLXHILLQFUEHHCDTUXTRRTHPFDSBHEDTLXLSRCZEVIVLQLDTULRVCXECHEDTDRTBAOMITPWXLXGOLPXLWBLAXRELPIFGTMTKVIODCDLCXWPFDQRTHWIVBSQSLWXWHRDNVHILLAXRTGDREFDQOYEHYQETWBHEHCGFZCTKLVWHOYFDLAHXYDRDWXQRLWXWYEOYLAXWXPRDIWECRYHCYDFGTMTKBTQYLISFITOEZCTKDRARWTHEDTFXPLCXFDEPHCDTTGIXZLLELAXRELPIOYEHHFCETCTGSESDLAILIKUVCEOGSDZFOYLTLYIHSIHCTBWYTLFGTMTKOGLWTGIXPCEMLTDRYEOYLTSTHLTRSHZFVLCXDREXZCTKDTFGIXWBRMOEZCTKVLDTIPUARPIHYQPOHCLARDTWFYISZYWXLAWBAQIXDTQDFRHWKTGLLPWHGOOYEIAILTLXAILIUVRPOYFDLAHXDTUZQXZAWBLGUERDIDZCPHXDZFQYFGTMTKVIRNRDRPLAXRTGDREFDQTLLVHTAOECZEILTO"

ptext10 = "hide the gold in the trexe stump"

ctext10 = "BMODZ BXDNA BEKUD MUIXM MOUVI F"


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
    np_char1 = np.array(ptext[0])
    np_char2 = np.array(ptext[1])

    result1 = ""
    result2 = ""

    char1_loc = np.argwhere(keyMatrix == np_char1)[0]
    char2_loc = np.argwhere(keyMatrix == np_char2)[0]

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


def generateKeyMatrix(key):
    key = key.replace(" ", "")
    key = key.upper()
    keyMatrix = np.array(
        [["z", "z", "z", "z", "z"], ["z", "z", "z", "z", "z"], ["z", "z", "z", "z", "z"], ["z", "z", "z", "z", "z"],
         ["z", "z", "z", "z", "z"]])
    j = 0
    k = 0
    for i in range(0, len(key)):
        if j == 5:
            j = 0
            k = k + 1

        keyMatrix[k][j] = key[i]
        j = j + 1

    return keyMatrix


def playfairDecrypt(ctext, keyMatrix):
    ctext = ctext.replace(" ", "").upper()

    result = ""
    for i in range(0, len(ctext) - 1, 2):
        result += playfairDecryptBigram(ctext[i] + ctext[i + 1], keyMatrix)

    return result


def swapRows(keyMatrix):
    firstSwap = random.randint(0, 4)
    secondSwap = random.randint(0, 4)
    tempSwap = np.copy(keyMatrix[firstSwap, :])
    keyMatrix[firstSwap, :] = np.copy(keyMatrix[secondSwap, :])
    keyMatrix[secondSwap, :] = np.copy(tempSwap)

    return keyMatrix


def swapCols(keyMatrix):
    firstSwap = random.randint(0, 4)
    secondSwap = random.randint(0, 4)
    tempSwap = np.copy(keyMatrix[:, firstSwap])
    keyMatrix[:, firstSwap] = np.copy(keyMatrix[:, secondSwap])
    keyMatrix[:, secondSwap] = np.copy(tempSwap)

    return keyMatrix


def swapLetters(keyMatrix):
    firstSwap = [random.randint(0, 4), random.randint(0, 4)]
    secondSwap = [random.randint(0, 4), random.randint(0, 4)]
    tempSwap = np.copy(keyMatrix[firstSwap[0]][firstSwap[1]])
    keyMatrix[firstSwap[0]][firstSwap[1]] = np.copy(keyMatrix[secondSwap[0]][secondSwap[1]])
    keyMatrix[secondSwap[0]][secondSwap[1]] = np.copy(tempSwap)

    return keyMatrix


# Debug
# keyMatrix = [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [2, 2, 2, 2, 2], [0, 0, 0, 0, 0]]
# keyMatrix = [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
# keyMatrix = [[0, 1, 2, 3, 4], [10, 11, 12, 13, 14], [20, 21, 22, 23, 24], [30, 31, 32, 33, 34], [40, 41, 42, 43, 44]]
# keyMatrix = np.array(keyMatrix)
#
# print(swapLetters(keyMatrix))

def keySwapStochastic(keyMatrix):
    choice = random.randint(1, 50)
    if choice == 1:
        return swapRows(keyMatrix)
    if choice == 2:
        return swapCols(keyMatrix)
    if choice == 3:
        # flips vertically
        return np.flip(keyMatrix, axis=0)
    if choice == 4:
        # flips horizontally
        return np.flip(keyMatrix, axis=1)
    if choice == 5:
        # flips vertically and horizontally
        return np.flip(keyMatrix)
    else:
        return swapLetters(keyMatrix)


def breakPlayfair():
    startingKey = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    ciphertext = ctext0

    parentKey = generateKeyMatrix(startingKey)

    parentDecipheredText = playfairDecrypt(ciphertext, parentKey)
    parentKeyScore = quadgramScorer.score(parentDecipheredText.replace('X', ''))

    SEED = 1
    random.seed(SEED)
    TEMP = 10 + 0.087 * (len(ciphertext) - 84)
    TEMP = 30.0
    STEP = 0.2
    COUNT = 0
    MAX_COUNT = 10000
    bestKeyscore = -9999999999
    bestKey = ""
    while TEMP >= 0:
        TEMP = TEMP - STEP
        COUNT = 0
        while COUNT < MAX_COUNT:
            childKey = keySwapStochastic(parentKey)
            childDecipheredText = playfairDecrypt(ciphertext, childKey)
            childKeyScore = quadgramScorer.score(childDecipheredText.replace('X', ''))
            scoreDiff = parentKeyScore - childKeyScore

            # parentKeyScore > childKeyScore
            if scoreDiff > 0:
                parentKey = childKey

            # parentKeyScore <= childKeyScore
            if scoreDiff <= 0:
                # calculate probability from equation;
                # get a random number from 0 to 1;
                # if the probability is greater than the random
                # number make the child the parent;
                # else increment the counter;
                try:
                    probability = 1 / (math.exp(-scoreDiff / TEMP))
                except OverflowError:
                    probability = 0
                if probability > random.uniform(0.0, 1.0):
                    parentKey = childKey
                else:
                    COUNT += 1
            if childKeyScore > bestKeyscore:
                bestKeyscore = childKeyScore
                bestKey = np.copy(childKey)
            COUNT += 1

        print("TEMP: " + str(TEMP))
        # print("parentKeyScore: " + str(parentKeyScore))
        print("childKeyScore: " + str(childKeyScore))
        print("bestKeyscore: " + str(bestKeyscore))
        print("bestKey: " + str(bestKey))
        print("COUNT: " + str(COUNT))
        print()

    return parentKey, parentKeyScore


quadgrams = "./english_quadgrams.txt"
quadgramScorer = ngram_score(quadgrams)

print(breakPlayfair())
