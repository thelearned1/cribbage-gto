import card as card_transformer
from scorer import score_shand, score_hand
from hand_to_int import shand_to_sint
from itertools import combinations
import score_cache

score_cache.load_scores_cache()

d = {}
for h in combinations(range(52), 5):
	hand = list(h)
	hand.sort()
	unsuited_hand = [card_transformer.rank_of(card) for card in hand]

	h = shand_to_sint(hand)
	d[h] = 0
	base_score = score_cache.get_score(unsuited_hand)

	for cut_index in range(len(hand)):
		out = {
			'key': shand_to_sint(hand),
			'base_score': score_shand(hand, cut_index, True, False),
			'base_score': score_shand(hand, cut_index, False, False)
		}
		
	d[shand_to_sint(hand)] = out

# score_cache.cache_scores(d)

__all__ = None