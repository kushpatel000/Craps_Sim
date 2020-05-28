'''
Once the point is set, single unit on each place bet.
Power press (or is it parley?) twice. Then collect.

'''



class TripleLux:

	def __init__(self,rules):
		self.table_min  = rules[0]
		self.field_pays = rules[1]
		self.place_rate = {4:9,5:7,6:7,8:7,9:7,10:9}

		self.name   = 'Triple Lux'
		self.coffer = 500
		
		self.place_bets = [0]*12
		self.parleys = {
			4:  [2,6],
			5:  [2,5],
			6:  [2,3],
			8:  [2,3],
			9:  [2,5],
			10: [2,6]}

	def set_place_bets(self):
		# define the bets by unit count
		if self.coffer > self.table_min*2:
			self.pass_odds = 2
			self.coffer -= self.table_min*2

		for pb in [6,8,5,9,4,10]:
			if self.coffer < self.table_min: break

			elif self.place_bets[pb] > 0: continue

			if pb == 6 or pb == 8:
				self.coffer -= int(self.table_min*6/5)
			elif pb == 5 or pb == 9:
				self.coffer -= self.table_min
			else: # 4,10
				self.coffer -= self.table_min
			self.place_bets[pb] = 1


	def update(self,call,button,dice) -> None:
		roll = dice[0]+dice[1]
		if call == '7_11':
			pass
		elif call == 'craps':
			pass
		elif call == 'point_set':
			self.set_place_bets()
		elif call == 'crap_out':
			self.place_bets = [0]*12
		elif call == 'come_out':
			pass
		elif call[0:5] == 'place':
			rate = self.place_rate[roll]
			self.coffer += self.place_bets[roll]*rate

			if self.place_bets[roll] == 1:
				self.place_bets[roll] = 3
				if roll == 6 or roll == 8:
					self.coffer -= 2*self.table_min*6/5
				else:
					self.coffer -= 2*self.table_min
			elif self.place_bets[roll] == 3:
				self.place_bets[roll] += self.parleys[roll][1]
				if roll == 6 or roll == 8:
					self.coffer -= self.parleys[roll][1]*self.table_min*6/5
				else:
					self.coffer -= self.parleys[roll][1]*self.table_min*6/5
		
		self.coffer = int(self.coffer)						
				
