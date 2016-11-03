#
#	TELEGRAM BOT
#
#		Name:			Nova
#		Username:		Nova_X1_Bot
#	
#		Log functions
#		Command logfile: commandLog.txt
#		Message logfile: messageLog.txt
#
#	By Jose Acevedo 
#	Copyright 2016.

import sys
import datetime

COMMANDLOGFILE = "commandLog.txt"
MESSAGELOGFILE = "messageLog.txt"

def extractMsg(msg):
	# Date
	log = "[" + str(datetime.datetime.utcfromtimestamp(msg["date"])) + "]:\n"

	# Info about user
	log += "FROM: "
	for key, value in msg["from"].iteritems():
		log += str(key) + " = " + str(value) + ", "
	log += "\n"
	# Info about chat
	log += "CHAT: "
	for key, value in msg["chat"].iteritems():
		log += str(key) + " = " + str(value) + ", "
	log += "\n"	
		
	# Message
	log += "MESSAGE = " + msg["text"] + "\n"

	return log

# Log information about requested command
def logCommand(msg):
	with open(COMMANDLOGFILE,'a') as logFile:
		logFile.write(extractMsg(msg))
		
# Log information about message sent
def logMessage(msg):
	with open(MESSAGELOGFILE,'a') as logFile:
		logFile.write(extractMsg(msg))
