# IMPORTS
import os
import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import Flask, request
import schedule
import requests
import datetime
import re
import math


bot_id = 'b42a0deb7c875a3eb503a0f45d'
GIPHY_API_KEY = "5c585a9b6f854781adcf89ab7a2c9533"
URL  = 'https://api.groupme.com/v3/bots/post'

app = Flask(__name__)

# Called whenever the app's callback URL receives a POST request
# That'll happen every time a message is sent in the group
@app.route('/', methods=['POST'])
def webhook():
	data = request.get_json()
	msg = data['text']
	if '!cheesecake' in msg:
		cheesecakeFunction()
	if '!cost' in msg:
		reply(getLoanSharkMoney())
	if '!countdown' in msg:
		reply(getCountDown())
	# if '!birthday' in msg:
	# 	birthdayFunction()
	return "ok", 200

# def birthdayFunction():
# 	BOT_ID = '93915624936df56152233e3708'
# 	GIPHY_API_KEY = "5c585a9b6f854781adcf89ab7a2c9533"
# 	GIPHY_ENDPOINT = "https://api.giphy.com/v1/gifs/random?api_key=5c585a9b6f854781adcf89ab7a2c9533&tag=birthday&rating=G"
# 	URL  = 'https://api.groupme.com/v3/bots/post'
# 	r = requests.get(GIPHY_ENDPOINT)
# 	data = r.json()["data"]
# 		#giphy will provide data as dict if there is a result or empty list if none
# 	# if type(data) is dict:
# 	name = "@Mark Ser , Happy Birthday!!!!"
# 	image = data["images"]["downsized_large"]["url"]
# 	send_message_with_image(response,["48724659"],[[0,9]],image)

def getTime():
	today = datetime.date.today()
	someday = datetime.date(2017, 7, 20)
	diff = someday - today
	tempTime = diff.days
	return tempTime

def getCountDown():
	today = datetime.date.today()
	futureTime = datetime.date(2018, 7, 20);
	diff = today - futureTime
	tempTime = diff.days
	message = "@Justin Kwon "+ tempTime + " till we get our cheesecake"
	send_message(message,["28150490"],[[0,12]])

def cheesecakeFunction():
	today = datetime.date.today()
	someday = datetime.date(2017, 7, 20)
	diff = today - someday
	tempTime = str(diff.days)
	cheesecake = "@Justin Kwon "+ "it's been "+ tempTime + " days since you've promised us cheesecake"
	send_message(cheesecake,["28150490"],[[0,12]])

def getLoanSharkMoney():
	today = datetime.date.today()
	someday = datetime.date(2017, 7, 20)
	diff = someday - today
	tempTime = diff.days

	principal = 262.32
	interestRate = 2000
	interest = (((interestRate/100)/365)+1)
	temp = interest**tempTime
	number = (principal*temp)

	numOfCheesecakes = number/8
	output = "Total cost for 30 people = $262.32 \nWith loan shark interest = $"+ str(number) + "\nThis means that Justin can buy ~" + str(numOfCheesecakes) + " cheesecakes"
	output = str(output)
	return output

def send_message_with_image(msg, usrID, locid,image):
	bot_id = 'b42a0deb7c875a3eb503a0f45d'
	GIPHY_API_KEY = "5c585a9b6f854781adcf89ab7a2c9533"
	URL  = 'https://api.groupme.com/v3/bots/post'
	data ={
	"bot_id" : bot_id,
	"text" : msg,
	'attachments': [
	{
	'loci':locid,
	'type':'mentions',
	'user_ids':usrID,
	}
	'type':'image',
	'url':image
	]
	}
	requests.post(URL, json=data)


def send_message(msg, usrID, locid):
	bot_id = 'b42a0deb7c875a3eb503a0f45d'
	GIPHY_API_KEY = "5c585a9b6f854781adcf89ab7a2c9533"
	GIPHY_ENDPOINT = "http://api.giphy.com/v1/gifs/translate"
	URL  = 'https://api.groupme.com/v3/bots/post'
	data ={
	"bot_id" : bot_id,
	"text" : msg,
	'attachments': [
	{
	'loci':locid,
	'type':'mentions',
	'user_ids':usrID,
	}
	]
	}
	requests.post(URL, json=data)
  # # params = json.dumps(data).encode('utf8')
  # request = Request(url,urlencode(data).encode('utf8'))
  # response = urlopen(request).read().decode()
def reply(msg):
	bot_id = 'b42a0deb7c875a3eb503a0f45d'
	GIPHY_API_KEY = "5c585a9b6f854781adcf89ab7a2c9533"
	GIPHY_ENDPOINT = "http://api.giphy.com/v1/gifs/translate"
	URL  = 'https://api.groupme.com/v3/bots/post'
	data ={
	'bot_id'		: bot_id,
	'text'			: msg,
	}
	request = Request(URL, urlencode(data).encode())
	json = urlopen(request).read().decode()
# Uploads image to GroupMe's services and returns the new URL
# def upload_image_to_groupme(imgURL):
# 	imgRequest = requests.get(imgURL, stream=True)
# 	filename = 'temp.png'
# 	postImage = None
# 	if imgRequest.status_code == 200:
# 		# Save Image
# 		with open(filename, 'wb') as image:
# 			for chunk in imgRequest:
# 				image.write(chunk)
# 		# Send Image
# 		headers = {'content-type': 'application/json'}
# 		url = 'https://image.groupme.com/pictures'
# 		files = {'file': open(filename, 'rb')}
# 		payload = {'access_token': 'eo7JS8SGD49rKodcvUHPyFRnSWH1IVeZyOqUMrxU'}
# 		r = requests.post(url, files=files, params=payload)
# 		imageurl = r.json()['payload']['url']
# 		os.remove(filename)
# 		return imageurl

# Checks whether the message sender is a bot
def sender_is_bot(message):
	return message['sender_type'] == "bot"
