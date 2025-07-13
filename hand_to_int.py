def hand_to_int (hand):
	total = 0
	for i in range(5):
		total+=(16**i)*hand[4-i]
	return total
	
def int_to_hand (total):
	hand = [0, 0, 0, 0, 0]
	for i in reversed(range(5)):
		dividend = (16**i) 
		value = total // dividend
		hand[4-i] = value
		total-=(value*dividend)
	return hand