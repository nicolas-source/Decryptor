from ngram_score import ngram_score

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

bigrams = "./english_bigrams.txt"
trigrams = "./english_trigrams.txt"
quadgrams = "./english_quadgrams.txt"

bigramScorer = ngram_score(bigrams)
trigramScorer = ngram_score(trigrams)
quadgramScorer = ngram_score(quadgrams)

sampleText1 = "HIDE THE GOLD IN THE TREE STUMP"
sampleText2 = "BMODZ BXDNA BEKUD MUIXM MOUVI F"

bigram_score = bigramScorer.score(sampleText1)
trigram_score = trigramScorer.score(sampleText1)
quadgram_score = quadgramScorer.score(sampleText1)

bigram_score_C = bigramScorer.score(sampleText2)
trigram_score_C = trigramScorer.score(sampleText2)
quadgram_score_C = quadgramScorer.score(sampleText2)

print(bigram_score)
print(trigram_score)
print(quadgram_score)

print(bigram_score_C)
print(trigram_score_C)
print(quadgram_score_C)

print(quadgramScorer.score("ATTACK THE EAST WALL OF THE CASTLE AT DAWN".replace(" ", "")))
print(quadgramScorer.score("FYYFHP YMJ JFXY BFQQ TK YMJ HFXYQJ FY IFBS".replace(" ", "")))

print(quadgramScorer.score(ctext10))
print(quadgramScorer.score(ptext10))

print(quadgramScorer.score("AWEBAWEBAWEBAWBAWEBAWEBAEWB"))
print(quadgramScorer.score("thethethethetreeisonthehouse".upper()))

print(quadgramScorer.score(ctext0))
print(quadgramScorer.score(ptext0.upper()))

print(quadgramScorer.score("FYYFHP YMJ JFXY BFQQ TK YMJ HFXYQJ FY IFBS".replace(" ", "")))
print(quadgramScorer.score("ATTACK THE EAST WALL OF THE CASTLE AT DAWN".replace(" ", "")))

# bigram = bigram_freq()
# bigram.compute_bigram_freq()
# print(bigram.getTop100Freq())
# print(bigram.freqAnalyzeTextPercentage(ptext0.upper()))
# print(bigram.freqAnalyzeTextPercentage(ctext0))