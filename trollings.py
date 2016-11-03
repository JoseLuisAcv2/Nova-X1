# -*- coding: utf-8 -*-
#
#	TELEGRAM BOT
#
#		Name:			Nova
#		Username:		Nova_X1_Bot
#
#		- Description:
#				Module to handle responses to particular users.
#
#	By Jose Acevedo 
#	Copyright 2016.

import random

messages = {}

# @pablod_bc
messages["pablod_bc"] = [
"Niggah.",
"What's up my nigger?",
"Shut up.",
"...",
"Calling the police...",
"That's my niggah!",
"I'm not answering you."
]

# Genesis Kuffaty
messages["Genesis_Kuffaty"] = [
"Who's the beta?",
"Who is the B?"
]

def handleTrollings(msg, chatID, bot):

	text = ""

	if msg["from"]["username"] == "pablod_bc":
		if random.randint(1,5) == 1:
			text = random.choice(messages["pablod_bc"])
	elif msg["from"]["first_name"] == "Genesis":
		if random.randint(1,5) == 1:
			text = random.choice(messages["Genesis_Kuffaty"])
			
	if text != "":
		bot.sendMessage(chatID, text)
