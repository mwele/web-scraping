from nltk import bigrams
bigrams = bigrams(text6)
bigramsDist = FreqDist(bigrams)
bigramDist[("Sir", "Robin")]
from nltk import ngrams
fourgrams = ngrams(text6, 4)
fourgramsDist = FreqDist(fourgrams)
fourgramsDist[("father", "smelt", "of", "elderberries")]
from nltk.book import *
from nltk import ngrams
fourgrams = ngrams(text6, 4)
for fourgram in fourgrams:
if fourgram[0] == "coconut":
print(fourgram)
from nltk.book import *
len(text6)/len(words)
from nltk import FreqDist
fdist = FreqDist(text6)
fdist.most_common(10)