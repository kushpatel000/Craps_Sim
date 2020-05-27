import Strategies.inside_only
from typing import List
import random

## Simple Functions ############
def roll2d6() -> List[int]:
	return [ random.randint(1,6), random.randint(1,6) ]
################################

## Basic Parameters ############
# -- adjust these --
n_shooters = 10
table_minimum = 5
# ------------------

# -- Lists ---------
field = {2:2,3:1,4:1,9:1,10:1,11:1,12:2} # dictionary including payouts
place = [4,5,6,8,9,10]
craps = [2,3,12]
seven_yo = [7,11]
# ------------------
################################


## Initials Conditions #########
button = False
call = "comeout"
shooter = 0
################################

## Counters Conditions #########
n_rolls = 0
################################

## Initialize Players ##########
rules = [table_minimum,field]
players = []
players.append( Strategies.inside_only.InsideOnly(rules) )
################################



## Play the game ###############
while shooter < n_shooters:
	n_rolls += 1
	[d1,d2] = roll2d6()
	roll = d1+d2

	# point not set
	if not button:
		# 7 or 11: winner
		if roll in seven_yo:
			call = '7_11'

		# 2, 3, or 12: craps
		elif roll in craps:
			call = 'craps'

		# place, set point
		else:
			button = roll
			call = 'point_set'

	# point previously set
	else:
		# 7, crap out
		if roll == 7:
			button = False
			shooter += 1
			call = 'crap_out'

		# point
		elif roll == button:
			call = 'come_out'

		# anything else
		else:
			call = str(roll)


	# update players
	for p in players:
		p.update(call,button,[d1,d2])
	if call == 'come_out': button = False



print("Final Coffers:")
for plr in players:
	print( "{0:15s} - {1:5d}".format(plr.name,plr.coffer) )

