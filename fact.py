#
#	TELEGRAM BOT
#
#		Name:			Nova
#		Username:		Nova_X1_Bot
#	
#		- Command: /fact
#		- Description:
#				Send random fact. Subjects: date, math, trivia and year.
#
#	By Jose Acevedo 
#	Copyright 2016.

import random
import unirest

def handleFact(msg, chatID, bot):
	
	# Choose from 4 possible categories
	factType = random.choice(["trivia","math","date","year"])
	
	# Fetch fact in plain text
	response = unirest.get("https://numbersapi.p.mashape.com/random/"+factType+"?fragment=false&json=true",headers={"X-Mashape-Key":"DuskHHYl5DmshhsjvJ4LaVXZinfpp1KnC92jsndIqrz6pC0CDa","Accept": "text/plain"}).body
	
	# Handle "year" type facts
	if response["type"] == "year":
		if "year" in response:
			fact = "Year: " + str(response["year"]) + "\n" + response["text"].title() + "."
		else:
			fact = response["text"].title() + "."
	# Handle "math" type facts
	elif response["type"] == "math":
		fact = response["text"].title() + " is " + str(response["number"]) + "."
	# Handle "trivia" type facts
	elif response["type"] == "trivia":
		fact = response["text"].title() + " is " + str(response["number"]) + "."
	# Handle "date" type facts
	else:
		if "year" in response:
			fact = "Year: " + str(response["year"]) + "\n" + response["text"].title() + "."
		else:
			fact = response["text"].title() + "."

	bot.sendMessage(chatID, fact)
