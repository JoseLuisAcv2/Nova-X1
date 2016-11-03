# -*- coding: utf-8 -*-
#
#	TELEGRAM BOT
#
#		Name:			Nova
#		Username:		Nova_X1_Bot
#	
#		- Command:		/ask
#		- Description:
#				Search Quora.com for an answer to query
#
#	By Jose Acevedo 
#	Copyright 2016.

import random
import urllib
from bs4 import BeautifulSoup

# Specifies min and max length of text retrieved from the web to be sent as a message.
# Too small may retrieve undesired headers.
# Too big may cause problems with Telegram API.
MIN_LENGTH_FILTER=100
MAX_LENGTH_FILTER=800

notFoundAns = [
"Not found.",
"I couldn't find an answer to such a question...",
"That's not an easy one.",
"Not in my database. I need to collect more data from humans.",
"There are many things unknown in this universe. This is one of those.",
"Try again later :(",
"Try reformulating the question."
]

# Function to handle queries
def handleAsk(msg, chatID, bot):

	if "reply_to_message" in msg:
		query = msg["reply_to_message"]["text"]
	else:
		try:
			query = msg["text"].split(' ',1)[1]
		except:
			query = ""

	formattedQuery = ""
		
	for i in range(len(query)):
		if query[i] == ' ':
			formattedQuery += '-'
		else:	
			formattedQuery += query[i]
			
	url = "https://www.quora.com/"+formattedQuery
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html, "html.parser")    
    
	answer = ""
	box=soup.findAll("span", attrs={"class":"rendered_qtext"})
	for i in range(len(box)):
		if MIN_LENGTH_FILTER < len(box[i].text) and len(box[i].text) < MAX_LENGTH_FILTER:
			answer=box[i].text.strip()
			break
	
	# Results not found
	if answer == "":
		answer = random.choice(notFoundAns)
	
	bot.sendMessage(chatID, answer)
