# -*- coding: utf-8 -*-
#
#	TELEGRAM BOT
#
#		Name:			Nova
#		Username:		Nova_X1_Bot
#	
#		- Command:		/rankText
#		- Description:
#				Extract a relevancy-ranked list of topic keywords from within a text.
#
#	By Jose Acevedo 
#	Copyright 2016.

import json
import unirest

# Extract keywords from the given message
def handleRankText(msg, chatID, bot):

	if "reply_to_message" in msg:
		text = msg["reply_to_message"]["text"]
	else:
		try:
			text = msg["text"].split(' ',1)[1]
		except:
			text = ""

	formattedText = ""
	for i in range(len(text)):
		if text[i] == ' ':
			formattedText += '+'
		else:
			formattedText += text[i]
			
			
	response = unirest.get("https://alchemy.p.mashape.com/text/TextGetRankedKeywords?outputMode=json&text="+formattedText,headers={"X-Mashape-Key":"DuskHHYl5DmshhsjvJ4LaVXZinfpp1KnC92jsndIqrz6pC0CDa","Accept": "application/json"})
	response = response.body

	message = text + "\n\n" + "------Ranked Keywords------\n"
	for i in range(len(response["keywords"])):
		message += "- " + response["keywords"][i]["text"] + " = " + \
		response["keywords"][i]["relevance"] + ".\n"
	
	bot.sendMessage(chatID, message)
