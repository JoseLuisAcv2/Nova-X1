# -*- coding: utf-8 -*-
#
#	TELEGRAM BOT
#
#		Name:			Nova
#		Username:		Nova_X1_Bot
#	
#		- Command:		/fuckoff
#		- Description:
#				Sends a message telling people to fuck off.
#
#	By Jose Acevedo 
#	Copyright 2016.

from foaas import fuck

# Function to get and send random sentence
def handleFuckOff(msg, chatID, bot):
	
	# Message with no arguments
	if len(msg["text"].split()) == 1:
		text = fuck.random(from_=".").text[:-4]
	# Message with 1 argument
	else:
		text = fuck.random(name=msg["text"].split()[1], from_=".").text[:-4]
		
	bot.sendMessage(chatID, text)
