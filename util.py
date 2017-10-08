import requests
import random
from flask import request



def randomWordList():
	word_site = "https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-usa-no-swears-medium.txt"
	response = requests.get(word_site)
	WORDS = response.content.splitlines()
	return WORDS

def generate_room_code():
	return random.choice(randomWordList()).decode("utf-8")

def get_user_info():
	user_agent = request.headers.get('User-Agent')
	return user_agent

def get_user_id():
	user_agent = request.headers.get('User-Agent')
	user_info = user_agent.split("/")
	user_id = user_info[-1]
	return user_id
