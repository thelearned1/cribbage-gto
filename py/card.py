
SUITS = [
	{'name': 'clubs', 'descriptor': 'of clubs', 'symbol': 'C', 'usymbol': '♣'},
	{'name': 'diamonds', 'descriptor': 'of diamonds', 'symbol': 'D', 'usymbol': '♦'},
	{'name': 'hearts', 'descriptor': 'of hearts', 'symbol': 'H', 'usymbol': '♥'},
	{'name': 'spades', 'descriptor': 'of spades', 'symbol': 'S', 'usymbol': '♠'},
]

RANKS = [
	{'name': 'ace', 'symbol': 'A', 'value': 0},
	{'name': '2', 'symbol': '2', 'value': 1},
	{'name': '3', 'symbol': '3', 'value': 2},
  {'name': '4', 'symbol': '4', 'value': 3},
	{'name': '5', 'symbol': '5', 'value': 4},
	{'name': '6', 'symbol': '6', 'value': 5},
	{'name': '7', 'symbol': '7', 'value': 6},
	{'name': '8', 'symbol': '8', 'value': 7},
	{'name': '9', 'symbol': '9', 'value': 8},
	{'name': '10', 'symbol': '10', 'value': 9},
	{'name': 'jack', 'symbol': 'J', 'value': 10},
	{'name': 'queen', 'symbol': 'Q', 'value': 11},
	{'name': 'king', 'symbol': 'K', 'value': 12},
]

def suit_of(card: int):
	if card > 51 or card < 0:
		raise ValueError(f"Input must be in the range [0, 52) (got {card})")
	return card // 13

def rank_of(card: int):
	if card > 51 or card < 0:
		raise ValueError(f"Input must be in the range [0, 52) (got {card})")
	return card % 13


def card_data(card: int):
	if card > 51 or card < 0:
		raise ValueError(f"Input must be in the range [0, 52) (got {card})")
	
	suit = SUITS[(suit_of(card))]
	rank = RANKS[(rank_of(card))]
	return {'suit': suit, 'rank': rank}

def card_to_symbol(card: int):
	data = card_data(card)
	return data['rank']['symbol']+data['suit']['usymbol']

def card_to_rank_value(card: int):
	return card_data(card)['rank']['value']

__all__ = [
	'card_data',
	'card_to_symbol',
	'card_to_rank_value',
	'suit_of',
	'rank_of'
]