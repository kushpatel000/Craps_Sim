'''
Player plays Pass Line and inside place bets
Minimum bet on the pass line
2x on the odds

'''



class InsideOnly:

	def __init__(self,rules):
		self.table_min  = rules[0]
		self.field_pays = rules[1]
		self.odds_rate  = {4:2/1,5:3/2,6:6/5,8:6/5,9:3/2,10:2/1}
		self.place_rate = {4:9,5:7,6:7,8:7,9:7,10:9}

		self.name   = 'Inside Only'
		self.coffer = 500
		
		self.place_bets = [0]*12
		self.pass_line  = 0
		self.pass_odds  = 0

		self.base_bet()

	def base_bet(self):
		if self.coffer > self.table_min:
			self.coffer -= self.table_min
			self.pass_line = self.table_min

	def set_place_bets(self,point):
		# define the bets by unit count
		if self.coffer > self.table_min*2:
			self.pass_odds = 2
			self.coffer -= self.table_min*2

		for pb in [6,8,5,9]:
			if self.coffer < self.table_min: break

			elif self.place_bets[pb] > 0: continue
			elif point == pb: continue

			if pb == 6 or pb == 8:
				self.coffer -= int(self.table_min*6/5)
			else: # 5,9
				self.coffer -= self.table_min
			self.place_bets[pb] = 1


	def update(self,call,button,dice) -> None:
		if call == '7_11':
			self.coffer += self.pass_line
		elif call == 'craps':
			self.pass_line = 0
			self.base_bet()
		elif call == 'point_set':
			self.set_place_bets(button)
		elif call == 'crap_out':
			self.pass_line  = 0
			self.pass_odds  = 0
			self.place_bets = [0]*12
			self.base_bet()
		elif call == 'come_out':
			self.coffer += 2*self.pass_line
			self.pass_line = 0

			rate = self.odds_rate[button]+1
			self.coffer += int(self.table_min*self.pass_odds*rate)
			self.pass_odds = 0
		else:
			rate = self.place_rate[button]
			self.coffer += self.place_bets[button]*rate