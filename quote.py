# -*- coding: utf-8 -*-
#
#	TELEGRAM BOT
#
#		Name:			Nova
#		Username:		Nova_X1_Bot
#	
#		- Command: /quote
#		- Description:
#				Send random famous quote. Current categories: famous - movies.
#					
#	By Jose Acevedo 
#	Copyright 2016.

import random
import unirest

def handleQuote(msg, chatID, bot):

	# Handle commands issued with no arguments
	try:
		text = msg["text"].split(' ',1)[1]
	except:
		text = ""
	
	# No arguments: Random between famous and movis
	if text == "":
		category = random.choice(["famous","movies"])
	# Specified famous
	elif text.upper() == "FAMOUS":
		category = "famous"
	# Specified movies
	elif text.upper() == "MOVIES":
		category = "movies"
	# Strings doesn't match valid arguments. Random argument generated.
	else:
		category = random.choice(["famous","movies"])
		
	# Fetch random quote
	response = unirest.post("https://andruxnet-random-famous-quotes.p.mashape.com/?cat="+category,headers={"X-Mashape-Key": "DuskHHYl5DmshhsjvJ4LaVXZinfpp1KnC92jsndIqrz6pC0CDa","Content-Type": "application/x-www-form-urlencoded","Accept": "application/json"}).body
	
	quote = response["quote"]
	author = response["author"]
	message = quote + "\n" + " - " + author
	bot.sendMessage(chatID, message)
