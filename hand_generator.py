import card as card_transformer
from scorer import score_hand
from hand_to_int import hand_to_int
import score_cache

d = {}
for c1 in range(0,13):
	c1a = (16**4)*c1
	for c2 in range(c1, 13):
		c2a = (16**3)*c2
		for c3 in range(c2, 13):
			c3a = (16**2)*c3
			for c4 in range(c3, 13):
				c4a = 16*c4
				for c5 in range(c4, 13):
					hand = sorted([c1, c2, c3, c4, c5])
					if all(map(lambda x: x == hand[0], hand)):
						print(f"skipping 5-of-a-kind {hand}")
						continue 
					
					out = {
						'key': hand_to_int(hand),
						'score': score_hand(hand)
					}
					d[hand_to_int(hand)] = out

score_cache.cache_scores(d)

__all__ = None