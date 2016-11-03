# -*- coding: utf-8 -*-
#
#	TELEGRAM BOT
#
#		Name:			Nova
#		Username:		Nova_X1_Bot
#	
#		- Command:		/emotionAnalyzer
#		- Description:
#				Analyze given text and extract positive/negative sentiment.
#
#	By Jose Acevedo 
#	Copyright 2016.

import json
import unirest
from xml.etree.ElementTree import fromstring, ElementTree

def handleEmotionAnalyzer(msg, chatID, bot):

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
			
	response = unirest.get("https://alchemy.p.mashape.com/text/TextGetTextSentiment?	outputMode=json&showSourceText=0&text="+formattedText,headers={"X-Mashape-Key":"DuskHHYl5DmshhsjvJ4LaVXZinfpp1KnC92jsndIqrz6pC0CDa","Accept": "text/plain"})

	response = response.body
	response = ElementTree(fromstring(response)).getroot()

	if response[0].text == "OK":
		msg = text + "\n---------------------------\n"
		try:
			msg += "- Type = " + response[4][1].text + "\n"
		except:
			msg += "- Type = Neutral\n"
		try:
			msg += "- Score = " + response[4][0].text
		except:
			msg += "- Score = 0.0"
	else:
		msg = "This is some kind of higher-order thinking I cannot analyze."

	bot.sendMessage(chatID, msg)

