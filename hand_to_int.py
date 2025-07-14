import card 

_SUITED_HAND_BASE = 64
_UNSUITED_HAND_BASE = 16

def _hand_to_int (hand, base, hand_size):
	total = 0
	for i in range(hand_size):
		total+=(base**i)*hand[hand_size-1-i]
	return total
	
def _int_to_hand (total, base, hand_size):
	hand = [0]*hand_size
	for i in reversed(range(hand_size)):
		dividend = (base**i) 
		value = total // dividend
		hand[hand_size-1-i] = value
		total-=(value*dividend)
	return hand

def hand_to_int (hand):
	return _hand_to_int(hand, _UNSUITED_HAND_BASE, 5)

def int_to_hand (total):
	return _int_to_hand(total, _UNSUITED_HAND_BASE, 5)

def shand_to_sint (hand):
	return _hand_to_int (hand, _SUITED_HAND_BASE, 5)

def sint_to_shand (hand):
	return _int_to_hand (hand, _SUITED_HAND_BASE, 5)

def shand_to_int (hand):
	unsuited_hand = [
		card.rank_of(crd) for crd in hand
	]
	return hand_to_int(unsuited_hand)