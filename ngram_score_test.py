from ngram_score import ngram_score


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






