from ngram_score import ngram_score


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

# bigram_score = bigramScorer.score(sampleText2)
# trigram_score = trigramScorer.score(sampleText2)
# quadgram_score = quadgramScorer.score(sampleText2)

print(bigram_score)
print(trigram_score)
print(quadgram_score)