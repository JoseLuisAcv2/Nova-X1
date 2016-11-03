#
#	TELEGRAM BOT
#
#		Name:			Nova
#		Username:		Nova_X1_Bot
#	
#		- Command:		/yoda
#		- Description:
#				Rearrange text in a way Yoda would say it. 
#
#		NOTE: Only works in English.
#
#	By Jose Acevedo 
#	Copyright 2016.

import urllib2

def handleYodaCommand(msg, chatID, bot):

	if "reply_to_message" in msg:
		text = msg["reply_to_message"]["text"]
	else:
		try:
			text = msg["text"].split(' ',1)[1]
		except:
			return
			
	formattedText = ""
	for i in range(len(text)):
		if text[i] == ' ':
			formattedText += '+'
		else:
			formattedText += text[i]
			
	req = urllib2.Request("https://yoda.p.mashape.com/yoda?sentence="+formattedText, \
	headers={"X-Mashape-Key":"DuskHHYl5DmshhsjvJ4LaVXZinfpp1KnC92jsndIqrz6pC0CDa", \
	"Accept": "text/plain"})

	response = urllib2.urlopen(req).read()
	bot.sendMessage(chatID, response)
