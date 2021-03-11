sentence=input("Enter a sentence:")

from collections import Counter
def letter_frequency(sentence):
	return Counter(sentence)
#sentence ="I never give up on this coding thing"

print(letter_frequency(sentence))