import requests
import random
from flask import request

id_dict= {}

def randomWordList():
	word_site = "http://gist.githubusercontent.com/chromadrive/ec81de2c59c7f9ffb2115205fe490876/raw/8cdc4e3fd3aae5fea395cdb556ba9d2be2f7a201/common_words.txt"
	response = requests.get(word_site)
	WORDS = response.content.splitlines()
	return WORDS

def generate_room_code():
	return random.choice(randomWordList()).decode("utf-8")

def randomIdList():
	word_site = "http://gist.githubusercontent.com/chromadrive/2188d4a82914b7032236fc55ee8c57f6/raw/a907484c2f57c053574d283c662f0514dc0f943a/berkeley_buildings.txt"
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
