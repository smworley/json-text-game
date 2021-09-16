# StoryNode class declaration 
class StoryNode:
	textBody = "null"               # display story text 
	optionBody = "null"             # display option text 
	options = {"null":{"null"}}     # option to storynode mapping
	terminator = "null"             # boolean. true if leaf. 

	def action(self):
		# print the node's textBody 
		print(self.textBody)
		if(self.terminator != True):
			# prompt for the next choice if there's more possible nodes. 
			print(self.optionBody)
			choice = input("Your choice: ")
			nextNodeIndex = self.options[choice]['nextnode']
			return nextNodeIndex 
	
	def __init__(self, json_node):
		# constructor to initialize a story node from a json file 
		self.textBody= json_node['textbody']
		try:
			self.optionBody= json_node['optionbody']
		except KeyError:
			self.optionBody= "null"
		try:
			self.options= json_node['options']
			self.terminator = False
		except KeyError:
            # if no further options, it's a leaf. 
			self.options= "null"
			self.terminator = True

import json

#load the configuration file 
config = json.load(open("config.json", "r"))
# load the json game file 
with open(config["gamefile"], "r") as game_file:
	 data = json.load(game_file)

	# intialize the first node (node 0)
	 start = StoryNode(data['game']["0"])
	 nextNodeIndex = start.action()
	 nextNode = StoryNode(data['game'][nextNodeIndex])
	 previousNode = start

	# continue prompting for nodes while terminator = false. 
	 while(True):
		 currentNode = nextNode 
		 if(currentNode.terminator==True):
			 currentNode.action()
			 break
		 nextNodeIndex = currentNode.action()
		 nextNode = StoryNode(data['game'][nextNodeIndex])
		 previousNode = currentNode

