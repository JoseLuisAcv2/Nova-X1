# -*- coding: utf-8 -*-
#
#	TELEGRAM BOT
#
#		Name:			Nova
#		Username:		Nova_X1_Bot
#	
#		- Description:
#				Contains global commands as specified by Telegram:
#					- /start
#					- /help
#					- /settings
#
#	By Jose Acevedo 
#	Copyright 2016.

def handleStart(msg, chatID, bot):

	grettings = "Welcome human " + msg["from"]["first_name"] + "." + \
	" May I introduce myself, my name is Nova X1 and I'm designed to serve all your requests.\n" + \
	"For a complete list of my commands execute /help."
	bot.sendMessage(chatID, grettings)
	
def handleHelp(chatID, bot):
	msg = "Available commands:\n\n"
	msg += "/ask [question] Ask a question and discover the unknown. (Beta release).\n\n"
	msg += "/emotionAnalyzer [text] Extract the emotional state from within a text." \
	" Only in English.\n\n"
	msg += "/rankText [text] Extract relevancy-ranked list of keywords from within a text." \
	" Best performance in English language.\n\n"
	msg += "/CodeforcesUpcomingContests Display list of upcoming Codeforces contests.\n\n"
	msg += "/fuckoff [name] Tell someone to fuck off.\n\n"
	msg += "/quote [category] Send random famous quote. Current categories: famous - movies.\n\n"
	msg += "/fact Send random real world fact.\n\n"
	msg += "/gif [keyword] Send random Gif related to keyword argument.\n\n"
	msg += "/yoda [text] Restructure text in a way Master Yoda would say it. Only in English.\n\n"
	bot.sendMessage(chatID, msg)
	
def handleSettings(chatID, bot):
	msg = "You cannot change me, human."
	bot.sendMessage(chatID, msg)
