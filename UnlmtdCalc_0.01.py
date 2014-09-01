#!/bin/python
#
# UnlmtdCalc Cinema Film Calculator														
# This application takes the value of a Cineworld Unlimited Card and works out depending on what ticket tier you choose:              
#	 _   _       _           _      _  ____      _      
#	| | | |_ __ | |_ __ ___ | |_ __| |/ ___|__ _| | ___ 
#	| | | | '_ \| | '_ ` _ \| __/ _` | |   / _` | |/ __|
#	| |_| | | | | | | | | | | || (_| | |__| (_| | | (__ 
# 	 \___/|_| |_|_|_| |_| |_|\__\__,_|\____\__,_|_|\___|
#
#
#	 Created By ZephrFish
# 	 August 2014
#
# What Does it Do?
# 1. How Many films you'd need to go and see in a year to get your money's worth
# 2. Asks you what films you want to see and then works out if you'd be cheaper off getting a card
# 3. prints out how much x amount of films will cost you
# 4. prints out savings from getting a card(based upon a 12 Month Membership)
# Future: API calls, Personalisaton, Potentially other cinema apps like Vue and Odeon too

# Call Imports
import sys


# Initial Banner
print """     
          _   _       _           _      _  ____      _      
         | | | |_ __ | |_ __ ___ | |_ __| |/ ___|__ _| | ___ 
         | | | | '_ \| | '_ ` _ \| __/ _` | |   / _` | |/ __|
         | |_| | | | | | | | | | | || (_| | |__| (_| | | (__ 
          \___/|_| |_|_|_| |_| |_|\__\__,_|\____\__,_|_|\___|

	Designed and Created by ZephrFish
	Created:  Ausgust 2014
	Revision: 0.01"""
print """


"""
# Get cost of Cineworld Unlimited Pass
pass_cost = float(12 * 16.40)
print "The current cost as of August 2014 for an Unlimited pass is roughly %d pounds for one year" % float(pass_cost)

# Ask user for cost of single ticket
single = float(input("How much does one ticket cost you? "))
print "A single ticket will cost you %r pounds." % float(single)  

# Calculate how many films or sittings a user needs to go to to get money's worth
worth = int(pass_cost)/int(single)
print "Based upon the cost of a single ticket and the cost of the pass for one year you would need to see %d films in one year to get your money's worth" % worth

# Get what films a user wants to see
filmList = []
userQuit = 0

while userQuit == 0:
    inputText=raw_input('Enter a film you would like to see at the cinema or "q" to finish:')
    if inputText == 'q':
         break 
    else:
         filmList.append(inputText)

# Print out the films a user has chosen
print "You want to see the following films: %r" % filmList

# Work out the amount it costs for all films in list
total = len(filmList) * float(single)
print "It will cost you %d pounds to see all the films you have selected" % total


