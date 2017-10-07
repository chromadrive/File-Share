import requests
import random


def randomWordList():
	word_site = "https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-usa-no-swears-medium.txt"
	response = requests.get(word_site)
	WORDS = response.content.splitlines()
	return WORDS

def generate_room_code():
	return random.choice(randomWordList()).decode("utf-8")

