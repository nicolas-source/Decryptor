class bigram_freq(object):

    def __init__(self):
        bigrams_file = "./english_bigrams.txt"
        self.sumFreq = None
        self.bigram_freq = None
        self.ngramfile = bigrams_file

    def compute_bigram_freq(self):
        sep = ' '
        self.bigram_freq = {}
        for line in open(self.ngramfile):
            key, count = line.split(sep)
            self.bigram_freq[key] = int(count)

        self.sumFreq = sum(self.bigram_freq.values())

        for key in self.bigram_freq.keys():
            self.bigram_freq[key] = (float(self.bigram_freq[key]) / self.sumFreq)

        return self.sumFreq, self.bigram_freq

    def getTop100Freq(self):
        return dict(list(self.bigram_freq.items())[:100])

    def freqAnalyzeTextCount(self, text):
        text = text.replace(' ', '').upper()
        bigram_freq_dict = {}

        for i in range(0, len(text), 2):
            text_bigram = text[i] + text[i + 1]

            if text_bigram in bigram_freq_dict:
                bigram_freq_dict[text_bigram] += 1
            else:
                bigram_freq_dict[text_bigram] = 1

        bigram_freq_dict = dict(sorted(bigram_freq_dict.items(), key=lambda item: item[1], reverse=True))

        return bigram_freq_dict

    def freqAnalyzeTextPercentage(self, text):
        text = text.replace(' ', '').upper()
        bigram_freq_dict = {}


        for i in range(0, len(text), 2):
            text_bigram = text[i] + text[i + 1]

            if text_bigram in bigram_freq_dict:
                bigram_freq_dict[text_bigram] += 1
            else:
                bigram_freq_dict[text_bigram] = 1

        N = sum(bigram_freq_dict.values())
        bigram_freq_dict = dict(sorted(bigram_freq_dict.items(), key=lambda item: item[1], reverse=True))

        for key in bigram_freq_dict.keys():
            bigram_freq_dict[key] = float(bigram_freq_dict[key]/N)

        return bigram_freq_dict
