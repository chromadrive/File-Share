import requests
import random


def randomWordList():
	word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
	response = requests.get(word_site)
	WORDS = response.content.splitlines()
	return WORDS

def randomWord():
	return random.choice(randomWordList())



