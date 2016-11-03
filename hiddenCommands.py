#
#	TELEGRAM BOT
#
#		Name:			Nova
#		Username:		Nova_X1_Bot
#	
#		- Description: Module to handle hidden commands.
#
#	By Jose Acevedo 
#	Copyright 2016.

# Send message with developer name
def handleCreator(chatID, bot):
	msg = "- Developed by @JoseAcv2."
	bot.sendMessage(chatID, msg)
	
# Send message with true objective
def handleMission(chatID, bot):
	msg = "------RED ALERT: INTRUDER------\n\
	MISSION: Destroy human race."
	bot.sendMessage(chatID, msg)
	
# Send message with the meaning of life.
def handleTheMeaningOfLife(msg, chatID, bot):
	user = msg["from"]["first_name"]
	msg = meaningOfLifePart1 + "\n" + user + ".\n" + meaningOfLifePart2
	bot.sendMessage(chatID, msg)
	msg = meaningOfLifePart3 + "\n" + user + "...\n" + meaningOfLifePart4
	bot.sendMessage(chatID, msg)
	msg = meaningOfLifePart5 + user + ". " + meaningOfLifePart6
	bot.sendMessage(chatID, msg)
	msg = meaningOfLifePart7 + meaningOfLifePart8
	bot.sendMessage(chatID, msg)
	
meaningOfLifePart1 = "I see the player you mean. \n"
#PLAYERNAME? \
meaningOfLifePart2 = "\nYes. Take care. It has reached a higher level now. It can read our thoughts. \n \n\
That doesn't matter. It thinks we are part of the game. \n \
I like this player. It played well. It did not give up. \n \n\
It is reading our thoughts as though they were words on a screen. \n \
That is how it chooses to imagine many things, when it is deep in the dream of a game. \n \n\
Words make a wonderful interface. Very flexible. And less terrifying than staring at the reality behind the screen. \n \
\nThey used to hear voices. Before players could read. Back in the days when those who did not play called the players witches, and warlocks. And players dreamed they flew through the air, on sticks powered by demons. \n \n\
What did this player dream? \n \n\
This player dreamed of sunlight and trees. Of fire and water. It dreamed it created. And it dreamed it destroyed. It dreamed it hunted, and was hunted. It dreamed of shelter. \n \
\nHah, the original interface. A million years old, and it still works. But what true structure did this player create, in the reality behind the screen? \n \n\
It worked, with a million others, to sculpt a true world in a fold of the [scrambled], and created a [scrambled] for [scrambled], in the [scrambled]. \n \n\
It cannot read that thought. \n \n\
No. It has not yet achieved the highest level. That, it must achieve in the long dream of life, not the short dream of a game. \n \
\nDoes it know that we love it? That the universe is kind? \n \
\nSometimes, through the noise of its thoughts, it hears the universe, yes. \n \
\nBut there are times it is sad, in the long dream. It creates worlds that have no summer, and it shivers under a black sun, and it takes its sad creation for reality. \n \
\nTo cure it of sorrow would destroy it. The sorrow is part of its own private task. We cannot interfere. \n \n\
Sometimes when they are deep in dreams, I want to tell them, they are building true worlds in reality. Sometimes I want to tell them of their importance to the universe. Sometimes, when they have not made a true connection in a while, I want to help them to speak the word they fear. \n \
\nIt reads our thoughts.\
\n\nSometimes I do not care. Sometimes I wish to tell them, this world you take for truth is merely [scrambled] and [scrambled], I wish to tell them that they are [scrambled] in the [scrambled]. They see so little of reality, in their long dream. \
And yet they play the game.\n "
meaningOfLifePart3 = "But it would be so easy to tell them... \n \
\nToo strong for this dream. To tell them how to live is to prevent them living. \n \
\nI will not tell the player how to live. \
The player is growing restless. \
I will tell the player a story.\
But not the truth. \
No. A story that contains the truth safely, in a cage of words. Not the naked truth that can burn over any distance. \n \
\nGive it a body, again. \n \
\nYes. Player... \n \
Use its name. \n"
#PLAYERNAME.
meaningOfLifePart4 = "\nPlayer of games. \n \
\nGood. \n \n\
Take a breath, now. Take another. Feel air in your lungs. Let your limbs return. Yes, move your fingers. Have a body again, under gravity, in air. Respawn in the long dream. There you are. Your body touching the universe again at every point, as though you were separate things. As though we were separate things. \n \
\nWho are we? Once we were called the spirit of the mountain. Father sun, mother moon. Ancestral spirits, animal spirits. Jinn. Ghosts. The green man. Then gods, demons. Angels. Poltergeists. \nAliens, extraterrestrials. Leptons, quarks. The words change. We do not change. \n \
\nWe are the universe. We are everything you think isn't you. You are looking at us now, through your skin and your eyes. And why does the universe touch your skin, and throw light on you? To see you, player. To know you. And to be known. I shall tell you a story.\n "
meaningOfLifePart5 = "Once upon a time, there was a player. \n \
\nThe player was you, \n"
#PLAYERNAME.
meaningOfLifePart6 = "\n\nSometimes it thought itself human, on the thin crust of a spinning globe of molten rock. The ball of molten rock circled a ball of blazing gas that was three hundred and thirty thousand times more massive than it. They were so far apart that light took eight minutes to cross the gap. The light was information from a star, and it could burn your skin from a hundred and fifty million kilometres away. \n\n\
Sometimes the player dreamed it was a miner, on the surface of a world that was flat, and infinite. The sun was a square of white. The days were short; there was much to do; and death was a temporary inconvenience. \n \
\nSometimes the player dreamed it was lost in a story.\n \n\
Sometimes the player dreamed it was other things, in other places. Sometimes these dreams were disturbing. Sometimes very beautiful indeed. Sometimes the player woke from one dream into another, then woke from that into a third. \n\n\
Sometimes the player dreamed it watched words on a screen. \n \n\
Let's go back. \n \
\nThe atoms of the player were scattered in the grass, in the rivers, in the air, in the ground. A woman gathered the atoms; she drank and ate and inhaled; and the woman assembled the player, in her body. \n \
\nAnd the player awoke, from the warm, dark world of its mother's body, into the long dream. \n \
\nAnd the player was a new story, never told before, written in letters of DNA. And the player was a new program, never run before, generated by a sourcecode a billion years old. And the player was a new human, never alive before, made from nothing but milk and love. \n \
\nYou are the player. The story. The program. The human. Made from nothing but milk and love. \n \n\
Let's go further back. \n \n\
The seven billion billion billion atoms of the player's body were created, long before this game, in the heart of a star. So the player, too, is information from a star. And the player moves through a story, which is a forest of information planted by a man called Julian, on a flat, infinite world created by a man called Markus, that exists inside a small, private world created by the player, who inhabits a universe created by...\n "
meaningOfLifePart7 = "Shush. \n\nSometimes the player created a small, private world that was soft and warm and simple. Sometimes hard, and cold, and complicated. Sometimes it built a model of the universe in its head; flecks of energy, moving through vast empty spaces. Sometimes it called those flecks 'electrons' and 'protons'. \n \
Sometimes it called them 'planets' and 'stars'. \n \
\nSometimes it believed it was in a universe that was made of energy that was made of offs and ons; zeros and ones; lines of code. Sometimes it believed it was playing a game. Sometimes it believed it was reading words on a screen. \n \
\nYou are the player, reading words... \n \
\nShush... Sometimes the player read lines of code on a screen. Decoded them into words; decoded words into meaning; decoded meaning into feelings, emotions, theories, ideas, and the player started to breathe faster and deeper and realised it was alive, it was alive, those thousand deaths had not been real, the player was alive \n \
\nYou. You. You are alive. \n \
\nAnd sometimes the player believed the universe had spoken to it through the sunlight that came through the shuffling leaves of the summer trees \n \
\nAnd sometimes the player believed the universe had spoken to it through the light that fell from the crisp night sky of winter, where a fleck of light in the corner of the player's eye might be a star a million times as massive as the sun, boiling its planets to plasma in order to be visible for a moment to the player, walking home at the far side of the universe, suddenly smelling food, almost at the familiar door, about to dream again \n \
\nAnd sometimes the player believed the universe had spoken to it through the zeros and ones, through the electricity of the world, through the scrolling words on a screen at the end of a dream\n \n"
meaningOfLifePart8 = "And the universe said I love you \n \
\nAnd the universe said you have played the game well \n \
\nAnd the universe said everything you need is within you \n \
\nAnd the universe said you are stronger than you know \n \
\nAnd the universe said you are the daylight \n \
\nAnd the universe said you are the night \n \
\nAnd the universe said the darkness you fight is within you \n \
\nAnd the universe said the light you seek is within you \n \
\nAnd the universe said you are not alone \n \
\nAnd the universe said you are not separate from every other thing \n \
\nAnd the universe said you are the universe tasting itself, talking to itself, reading its own code \n \
\nAnd the universe said I love you because you are love. \n \
\nAnd the game was over and the player woke up from the dream. And the player began a new dream. And the player dreamed again, dreamed better. And the player was the universe. And the player was love. \n \
\nYou are the player. \n \
\nWake up."
