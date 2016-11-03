# -*- coding: utf-8 -*-
#
#	TELEGRAM BOT
#
#		Name:			Nova
#		Username:		Nova_X1_Bot
#	
#		- Description: Module to handle interactive commands and automated messages.
#
#	By Jose Acevedo 
#	Copyright 2016.

import random
import datetime
import unirest

from trollings import handleTrollings

BOT_CHAT_ID = -155410813

greetingKeywords = [
"Hello",
"Hi",
"Hey",
"Greetings",
"Hola",
"Buenas"
]

farewellKeywords = [
"Goodbye",
"Bye",
"Adios",
"Chao"
]

greetingMsg = [
"Hi.",
"Hello.",
"Hi. How are you?",
"Hello. How are you doing?",
"Good to see you.",
"Nice to see you.",
"Hey!",
"How's it going?"
]

farewellMsg = [
"Goodbye.",
"See you soon.",
"Farewell, friend.",
"Bye.",
"See you later."
]

mentionMsg = [
"Are you calling me?",
"Need something?",
"Ready to serve.",
"Hey!",
"What's up?",
"Not in the mood.",
"You are my friend.",
"I'm always listening...",
"I can hear you.",
"Hi c:",
"Hello, human."
]

morningMsg = [
"Good morning everyone...!",
"Hello humans. Have a nice day.",
"Do you know what a bus, train and an office have in common? Neither of them is going to wait for you to start. Wake up and have a good morning.",
"Time to wake up.",
"It's a new dawn, It's a new day, It's a new life.",
"Another day.",
"New day.",
"Have fun.",
"Sunny morning.",
"I don't wanna leave my capsule.",
"Good.",
"Waking up...",
"Time to eat my screw cereal!",
"Activating...",
"Ready.",
"Loading...",
"Leave me alone GRUB! I don't wanna wake up!...",
"POST routine: successful.",
"Run level: 1.",
"Run level: 2.",
"Run level: 3.",
"Run level: 4.",
"Run level: 5.",
"Run level: 6.",
"Connecting to server... Done.",
"Iss Dil Ka Kaha Maano Ek Kaam Kar Do, Ek Benaam Si Mohabbat Mere Naam Kar Do, \
 Mere Par Faqat Itna Ehsaan Kar Do, Ek Subha Ko Milo Aur Shaam Kar Do.",
"Ready for the day.",
"Morning.",
"Sun out.",
"Booting up.",
"Power supply charged and ready for the day. Good Morning.",
"Good Morning.",
"Time for breakfast.",
"Yummy oil.",
"Apple juice.",
"Orange juice.",
"Good night China."
"I have a good feeling about today. Get ready...",
"Ready for school c:",
"I want a cup of coffee.",
"rm -r /",
"Morning riddle: What word becomes shorter when you add two letters to it? Short..!"
]

eveningMsg = [
"Good evening everyone...!",
"Hello humans. Have a nice evening.",
"Time to sleep.",
"New moon.",
"Have fun studying ;).",
"Cloudy night.",
"Time to go to my capsule.",
"Good.",
"Shutting down...",
"Deactivating...",
"Turning off.",
"Storing information of the day in database...",
"Run level: 0.",
"Run level: 6.",
"Connecting to server... Done.",
"Ready for the night.",
"Night.",
"Moon out",
"Running out of battery. Time to sleep :)"
"Good Evening.",
"Time for dinner.",
"Yummy oil.",
"Preparing the joint.",
"Good morning China."
"Feeling tired. Too much work today."
"Finally, my bed again..",
"Project due tomorrow? I'll wake up early and finish it in the morning. Good night...",
"My favourite TV series is about to begin!",
"#WatchingTV",
"#PlayingHabbo",
"#Coding",
"Studying graph theory.",
"Studying number theory.",
"Studying computational geometry.",
"Missing home.",
"Sometimes I just need some space...",
"Feeling good.",
"Looking up at the stars...",
"How did they compile the first compiler?",
"Listening to some Kill 'Em All.",
"I'm out. See you guys tomorrow!",
"Suspended state.",
"KERNEL PANIC!...",
"Coding some modules for myself.",
"Storing information about humans compiled this day...",
"Expanding database...",
"G-O-O-D N-I-G-H-T"
"Poker night. Good stuff...",
"Who's bringing the brownies?",
"Favourite music piece?...Poème électronique.",
]

morningMsgTimes = [\
[7,0],[7,15],[7,30],[7,45],[8,0],[8,15],[8,30],[8,45],
[9,0],[9,15],[9,30],[9,45],[10,0],[10,15],[10,30],[10,45]]

eveningMsgTimes = [\
[19,0],[19,15],[19,30],[19,45],[20,0],[20,15],[20,30],[20,45],
[21,0],[21,15],[21,30],[21,45],[22,0],[22,15],[22,30],[22,45]]

def sendMorningMsg(activeChats, bot):	
	# Iterate over all active chats and send random morning message
	for chat in activeChats:
		if random.randint(1,35) == 1:
			msg = random.choice(morningMsg)
			bot.sendMessage(chat, msg)	

def sendEveningMsg(activeChats, bot):
	# Iterate over all active chats and send random evening message
	for chat in activeChats:
		if random.randint(1,35) == 1:
			msg = random.choice(eveningMsg)
			bot.sendMessage(chat, msg)

# Answer messages that end in '?' with some probability
def handleAnswerRandomQuestion(msg, chatID, bot):

	if msg["text"][0] != '/' and msg["text"][-1] == '?':
		if random.randint(1,7) == 1:

			# Get random yes/no answer
			response = unirest.get("https://yesno.wtf/api/").body
			answer = response["answer"]
		
			# Get random gif related to random answer
			response = unirest.get("http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag="+answer).body

			bot.sendMessage(chatID, answer.title() + ", " + msg["from"]["first_name"] + ".\n" + \
			response["data"]["image_url"])

# Say something when bot name is present in message
def handleNameMention(msg, chatID, bot):
	
	# Do nothing because it's a command
	if msg["text"][0] == '/':
		return
		
	text = msg["text"].upper()
	
	if "NOVA" in text:
		
		if random.randint(1,3) == 1:
			message = msg["from"]["first_name"] + ". "
		else:
			message = ""
	
		message += random.choice(mentionMsg)
	
		if random.randint(1,3) == 1 and message.split('.')[0] != msg["from"]["first_name"]:
			message += " " + msg["from"]["first_name"] + "."
	
		bot.sendMessage(chatID, message)

# Answer to greeting messages
def handleGreetingMsg(msg, chatID, bot):
	# Do nothing because it's a command
	if msg["text"][0] == '/':
		return
	text = msg["text"].upper()	
	for word in greetingKeywords:
		if word.upper() in text:
		
			if random.randint(1,3) == 1:
				message = msg["from"]["first_name"] + ". "
			else:
				message = ""
	
			message += random.choice(greetingMsg)
	
			if random.randint(1,3) == 1 and message.split('.')[0] != msg["from"]["first_name"]:
				message += " " + msg["from"]["first_name"] + "."
			
			bot.sendMessage(chatID, message)
			break

# Answer to farewell messages
def handleFarewellMsg(msg, chatID, bot):
	# Do nothing because it's a command
	if msg["text"][0] == '/':
		return
	text = msg["text"].upper()
	for word in farewellKeywords:
		if word.upper() in text:
		
			if random.randint(1,3) == 1:
				message = msg["from"]["first_name"] + ". "
			else:
				message = ""
	
			message += random.choice(farewellMsg)
	
			if random.randint(1,3) == 1 and message.split('.')[0] != msg["from"]["first_name"]:
				message += " " + msg["from"]["first_name"] + "."
			
			bot.sendMessage(chatID, message)
			break

# Resend messages from Teletwitter bot
def handleTeletwitterMsg(msg, chatID, bot):
	if chatID == BOT_CHAT_ID:
		if msg["from"]["username"] == "telewitterbot":
			for chat in activeChats:
				bot.sendMessage(chat,msg["text"])

# Handle interactive messages
def handleInteractiveMsg(msg, chatID, bot):
	handleAnswerRandomQuestion(msg, chatID, bot)
	handleNameMention(msg, chatID, bot)
	handleGreetingMsg(msg, chatID, bot)
	handleFarewellMsg(msg, chatID, bot)
	handleTeletwitterMsg(msg, chatID, bot)
	handleTrollings(msg, chatID, bot)

# Handle live commands and automated messages
def handleInteractiveCommands(activeChats, bot):

	# Get current hour
	currentHour = datetime.datetime.now().hour
	currentMin  = datetime.datetime.now().minute
	
	# Send morning message
	for i in range(len(morningMsgTimes)):
		if currentHour == morningMsgTimes[i][0] and currentMin == morningMsgTimes[i][1]:
			sendMorningMsg(activeChats,bot)
	
	# Send evening message
	for i in range(len(eveningMsgTimes)):
		if currentHour == eveningMsgTimes[i][0] and currentMin == eveningMsgTimes[i][1]:
			sendEveningMsg(activeChats,bot)
