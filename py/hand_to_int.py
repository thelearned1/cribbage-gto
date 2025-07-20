import card 
import math

_SUITED_CARDS = 52
_UNSUITED_CARDS = 13
_CARDS_PER_HAND = 5

_SUITED_CNS = [-1] * (_CARDS_PER_HAND*_SUITED_CARDS)
_UNSUITED_CNS = [-1] * (_CARDS_PER_HAND*_UNSUITED_CARDS)
_SUITED_CNS_INDICES = [-1] * len(_SUITED_CNS)
_UNSUITED_CNS_INDICES = [-1] * len(_UNSUITED_CNS)
for k in range(_CARDS_PER_HAND):
	for (n, cache, index_lookup) in [
		(_SUITED_CARDS, _SUITED_CNS, _SUITED_CNS_INDICES),
		(_UNSUITED_CARDS, _UNSUITED_CNS, _UNSUITED_CNS_INDICES)
	]:
		for c_k in range(n):
			c = math.comb(c_k, k+1)
			idx = (k*n)+c_k
			cache[idx] = c
			base = (k*n)-1
			# print(base)
			if base < 0:
				continue 
			while (cache[base] > c):
				base-=1
			index_lookup[idx] = base
			
def _int_to_hand (total, base, cache=None, index_cache=None):
	output_hand = [-1] * _CARDS_PER_HAND
	if not (cache and index_cache):
		cache, index_cache = (
			base == _UNSUITED_CARDS and (_UNSUITED_CNS, _UNSUITED_CNS_INDICES)
		) or (
			base == _SUITED_CARDS and (_SUITED_CNS, _SUITED_CNS_INDICES)
		) or (
			(None, None)
		)

	idx = len(cache)-1
	for k in reversed(range(_CARDS_PER_HAND)):
		if idx < 0:
			output_hand[k] = idx+base 
			continue
		
		while (cache[idx] > total):
			idx-=1
		output_hand[k]=idx % base
		#print(f"total: {total}, new total: {total-cache[idx]}, idx: {idx}")
		total-=cache[idx]
		idx=index_cache[idx]

	return output_hand

def _hand_to_int (hand, base, cache=None):
	cache = cache or (
		base == _UNSUITED_CARDS and _UNSUITED_CNS
	) or (
		base == _SUITED_CARDS and _SUITED_CNS
	)
	total = 0
	for k in range(_CARDS_PER_HAND):
		total+=cache[(k*base)+hand[k]]
	return total

def _hand_to_int_duplicates(hand, base, hand_size):
	total = 0
	for i in range(hand_size):
		total+=(base**i)*hand[hand_size-1-i]
	return total

def _int_to_hand_duplicates(total, base, hand_size):
	hand = [0]*hand_size
	for i in reversed(range(hand_size)):
		dividend = (base**i) 
		value = total // dividend
		hand[hand_size-1-i] = value
		total-=(value*dividend)
	return hand

def hand_to_int (hand):
	return _hand_to_int_duplicates(hand, _UNSUITED_CARDS, _CARDS_PER_HAND)

def int_to_hand (total):
	return _int_to_hand_duplicates(total, _UNSUITED_CARDS, _CARDS_PER_HAND)

def shand_to_sint (hand):
	return _hand_to_int (hand, _SUITED_CARDS)

def sint_to_shand (hand):
	return _int_to_hand (hand, _SUITED_CARDS)

def shand_to_int (hand):
	unsuited_hand = [
		card.rank_of(crd) for crd in hand
	]
	return hand_to_int(unsuited_hand)