import requests
import random
from flask import request

id_dict= {}

def randomWordList():
	word_site = "https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-usa-no-swears-medium.txt"
	response = requests.get(word_site)
	WORDS = response.content.splitlines()
	return WORDS

def generate_room_code():
	return random.choice(randomWordList()).decode("utf-8")

def randomIdList():
	word_site = "https://raw.githubusercontent.com/chromadrive/File-Share/master/PokemonList.txt"
	response = requests.get(word_site)
	WORDS = response.content.splitlines()
	return WORDS




def get_user_info():
	user_agent = request.headers.get('User-Agent')
	return user_agent

def get_user_id():
	user_agent = request.headers.get('User-Agent')
	if user_agent in id_dict:
		return id_dict[user_agent]
	else:
		new_id = random.choice(randomIdList()).decode("utf-8")
		id_dict[user_agent] = new_id
		return  new_id
