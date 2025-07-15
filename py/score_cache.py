
import csv 
import os
import hand_to_int
import card

filename = 'cribbage_scores.csv'

CACHED_SUITLESS_SCORES = {}
CACHED_SUITFUL_SCORES = {}

def cache_scores(d):
	with open(filename, 'w') as outfile:
		fieldset = ['key', 'card 0', 'card 1', 'card 2', 'card 3', 'card 4', 'score']
		writer = csv.DictWriter(outfile, fieldnames=fieldset, extrasaction='ignore')
		writer.writeheader()

		for key, value in d.items():
			value['key'] = key
			hand = hand_to_int.shand_to_sint(key)
			for i in range(len(hand)):
				value[f"card {i}"] = hand[i]
			writer.writerow(value)

def load_scores_cache():
	if not os.path.isfile(filename):
		raise FileNotFoundError("could not find cache file --- has cache_values been executed?")
	with open(filename, 'r') as infile:
		reader = csv.DictReader(infile)
		for row in reader:
			CACHED_SUITLESS_SCORES[int(row['key'])] = int(row['score'])

def get_score(sorted_hand):
	i = hand_to_int.hand_to_int(sorted_hand)
	if i in CACHED_SUITLESS_SCORES:
		return CACHED_SUITLESS_SCORES[i]
	else:
		raise ValueError(f"is sorted_hand unsorted? got {sorted_hand}, converted to int {i}")

def sget_score(sorted_hand):
	i = hand_to_int.shand_to_sint(sorted_hand)
	if i in CACHED_SUITFUL_SCORES:
		return CACHED_SUITFUL_SCORES[i]
	
	return None 
	
def sset_cache(sorted_hand, score):
	i = hand_to_int.shand_to_sint(sorted_hand)
	CACHED_SUITFUL_SCORES[i] = score