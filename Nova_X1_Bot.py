#
#	TELEGRAM BOT
#
#		Name:			Nova
#		Username:		Nova_X1_Bot
#	
#		Main function
#		Authorization token: 285572918:AAFKUa-0lZM8xHUi67ntOgoxcpRU3cIK9no
#
#	By Jose Acevedo 
#	Copyright 2016.

import sys
import datetime
import telepot
import urllib2
import json
import time
	
from logFunctions import logCommand, logMessage
from yoda import handleYodaCommand
from ask import handleAsk
from codeforcesUpcomingContests import handleCodeforcesUpcomingContestsCommand
from emotionAnalyzer import handleEmotionAnalyzer
from rankText import handleRankText
from globalCommands import handleStart, handleHelp, handleSettings
from fuckoff import handleFuckOff
from quote import handleQuote
from fact import handleFact
from hiddenCommands import handleCreator, handleMission, handleTheMeaningOfLife
from gif import handleGif
from interactiveCommands import handleInteractiveCommands, handleInteractiveMsg

# Initialize bot
AUTHORIZATION_TOKEN = "285572918:AAFKUa-0lZM8xHUi67ntOgoxcpRU3cIK9no"
bot = telepot.Bot(AUTHORIZATION_TOKEN)

# Handle incoming commands
def commandHandle(content, msg, chatID):
		
	command = content.split()[0]
	
	if command == "/start" or command == "/start@Nova_X1_Bot":
		handleStart(msg, chatID, bot)
	elif command == "/help" or command == "/help@Nova_X1_Bot":
		handleHelp(chatID, bot)
	elif command == "/settings" or command == "/settings@Nova_X1_Bot":
		handleSettings(chatID, bot)
	elif command == "/CodeforcesUpcomingContests" or command == "/CodeforcesUpcomingContests@Nova_X1_Bot":
		handleCodeforcesUpcomingContestsCommand(chatID, bot)	
	elif command == "/yoda" or command == "/yoda@Nova_X1_Bot":
		handleYodaCommand(msg, chatID, bot)
	elif command == "/ask" or command == "/ask@Nova_X1_Bot":
		handleAsk(msg, chatID, bot)
	elif command == "/emotionAnalyzer" or command == "/emotionAnalyzer@Nova_X1_Bot":
		handleEmotionAnalyzer(msg, chatID, bot)
	elif command == "/rankText" or command == "/rankText@Nova_X1_Bot":
		handleRankText(msg, chatID, bot)
	elif command == "/fuckoff" or command == "/fuckoff@Nova_X1_Bot":
		handleFuckOff(msg, chatID, bot)
	elif command == "/quote" or command == "/quote@Nova_X1_Bot":
		handleQuote(msg, chatID, bot)
	elif command == "/fact" or command == "/fact@Nova_X1_Bot":
		handleFact(msg, chatID, bot)
	elif command == "/gif" or command == "/gif@Nova_X1_Bot":
		handleGif(msg, chatID, bot)
	elif command == "/creator" or command == "/creator@Nova_X1_Bot":
		handleCreator(chatID, bot)
	elif command == "/mission" or command == "/mission@Nova_X1_Bot":
		handleMission(chatID, bot)
	elif command == "/theMeaningOfLife" or command == "/theMeaningOfLife@Nova_X1_Bot":
		handleTheMeaningOfLife(msg, chatID, bot)
		
# Handle incoming messages
def messageHandle(msg):

	contentType, chatType, chatID = telepot.glance(msg)
		
	# Remember group chats IDs to send random messages
	if chatType == "group" or chatType == "supergroup":
		activeChats.add(chatID)
	
	if contentType == 'text':

		logMessage(msg)
		content = msg['text']
		handleInteractiveMsg(msg, chatID, bot)
		
		# Command messages
		if content[0] == '/':
			logCommand(msg)
			commandHandle(content, msg, chatID)

reload(sys)
sys.setdefaultencoding("utf-8")
bot.message_loop(messageHandle)
activeChats = set(([]))

while True:
	handleInteractiveCommands(activeChats,bot)
	time.sleep(30)
