#
#	TELEGRAM BOT
#
#		Name:			Nova
#		Username:		Nova_X1_Bot
#	
#		- Command:		/CodeforcesUpcomingContests
#		- Description:
#				Displays information about upcoming Codeforces contests. 
#
#	By Jose Acevedo 
#	Copyright 2016.

import time
import json
import urllib2
import datetime

# Handle Codeforces upcoming contests command
def handleCodeforcesUpcomingContestsCommand(chatID, bot):

		# Fetch Codeforces data
		response = urllib2.urlopen("http://codeforces.com/api/contest.list?gym=false")
		response = json.load(response)

		if response["status"] == "OK":
			
			contestsInfoMsg = "Upcoming contests:\n"
			contestList = response["result"]
	
			for i in range(len(contestList)):
				contest = contestList[i]
				if contest["phase"] == "BEFORE":
				
					# Contest name
					contestsInfoMsg += "\n - " + contest["name"] + "\n"

					# Contest start time given in seconds
					if "startTimeSeconds" in contest:
						contestsInfoMsg += "   Start time: " + str(datetime.datetime.utcfromtimestamp(contest["startTimeSeconds"]))[:-3] + "\n"

					# Contest duration given in seconds
					contestDuration = contest["durationSeconds"]
					hh = contestDuration/3600
					mm = (contestDuration - hh*3600)/60
					contestsInfoMsg += "   Duration: " + str(hh) + "h " + str(mm) + "m\n"

					# Contest author
					if "preparedBy" in contest:
						contestsInfoMsg += "   Author: " + contest["preparedBy"] + "\n"

					# Contest kind
					if "kind" in contest:
						contestsInfoMsg += "   Kind: " + contest["kind"] + "\n"

			bot.sendMessage(chatID, contestsInfoMsg)
	
		else:
			bot.sendMessage(chatID, "Unable to fetch upcoming contest :(")	

