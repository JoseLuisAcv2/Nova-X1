# -*- coding: utf-8 -*-
#
#	TELEGRAM BOT
#
#		Name:			Nova
#		Username:		Nova_X1_Bot
#	
#		- Command: /gif
#		- Description:
#				Send random GIF image related to command argument.
#					
#	By Jose Acevedo 
#	Copyright 2016.

import unirest

# Hanldle command to send random Gif related to some keyword passed as argument
def handleGif(msg, chatID, bot):

	# Handle commands issued with no arguments
	try:
		tag = msg["text"].split(' ',1)[1:]
	except:
		tag = ""
	
	formattedTag = ""
	for i in range(len(tag)):
		if tag[i] == ' ':
			formattedTag += '+'
		else:
			formattedTag += tag[i]
	
	# No arguments: Random trending Gif
	if formattedTag == "":
		response = unirest.get("http://api.giphy.com/v1/gifs/trending?api_key=dc6zaTOxFJmzC&limit=1").body	
		bot.sendMessage(chatID, response["data"][0]["url"])
	# Gif related to keyword
	else:
		response = unirest.get("http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag="+formattedTag).body
		bot.sendMessage(chatID, response["data"]["image_url"])
