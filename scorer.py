import partition
import card as card_transformer
import hand_to_int
import score_cache

def score_runs (sorted_cards):
	current_run = {}
	longest_run = {}

	for card in sorted_cards:
		# defaultdict doesn't make sense here because we want to rely on
		# len(run_details.keys()) for run size
		if card not in current_run:
			if card-1 not in current_run:
				if len(current_run.keys()) >= 3:
					longest_run = current_run
					break
				else: 
					current_run = {}
			current_run[card] = 1
		else: 
			current_run[card]+=1

	print (current_run)

	if len(current_run.keys()) >= 3:
		longest_run = current_run
	# return real_run	
	
	score = len(longest_run.keys())
	for count in longest_run.values():
		score*=count

	return score

def score_pairs (sorted_cards):
	COUNT_TO_SCORE_TABLE = {
		1: 0,
		2: 2,
		3: 6,
		4: 12
	}
	num_in_a_row = 1
	runs = []
	for card1, card2 in zip(sorted_cards[:-1], sorted_cards[1:]):
		if card1 == card2:
			num_in_a_row+=1
		else: 
			runs.append(num_in_a_row)
			num_in_a_row=1

	runs.append(num_in_a_row)

	score_total = 0
	for run_length in runs:
		score_total+=(COUNT_TO_SCORE_TABLE[run_length])
	return score_total

def score_fifteens (sorted_cards):
	sorted_fixed_cards = [
		(card+1 if card+1 < 10 else 10) for card in sorted_cards
	]
	num_fifteens = 0
	for prt in partition.iter_partitions(sorted_fixed_cards):
		if sum(prt) == 15:
			num_fifteens+=1
	return num_fifteens*2

def score_hand (sorted_cards):
	return (
		score_runs(sorted_cards)+
		score_pairs(sorted_cards)+
		score_fifteens(sorted_cards)
	)

def score_sflush (hand, cut_index, is_crib=False):
	first_suit = card_transformer.suit_of(hand[0])
	cut_matches = True
	is_flush = True
	for i in range (1, len(hand)):
		suit = card_transformer.suit_of(hand[i])
		if suit != first_suit:
			if i == cut_index:
				cut_matches = False
			is_flush = False

	if is_crib:
		return 5 if is_flush and cut_matches else 0
	else:
		if is_flush:
			return 5 if cut_matches else 4
		else:
			return 0
	
def score_sknobs (hand, cut_index, is_crib=False, crib_allows_knobs=True):
	for i in range(1, len(hand)):
		suit = card_transformer.suit_of(hand[i])
		if card_transformer.rank_of(hand[i]) == 10 and i != cut_index: # is a jack
			if suit == card_transformer.suit_of(hand[cut_index]) and (not is_crib or crib_allows_knobs):
				return 1
	return 0

def score_shand (hand, cut_index, is_crib=False, crib_allows_knobs=True):
	score = score_cache.sget_score(hand)
	if score is not None:
		return score
	
	return (
		score_cache.get_score([card_transformer.rank_of(card) for card in hand])
		+ score_sflush(hand, cut_index, is_crib)
		+ score_sknobs(hand, cut_index, is_crib, crib_allows_knobs)
	)