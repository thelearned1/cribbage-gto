import pytest
import scorer

run_score_cases = [
	{'score': 0, 'cards': [3, 2, 2, 2, 2], 'name': 'four of a kind and an almost-run'},
	{'score': 0, 'cards': [6, 5, 3, 2, 10], 'name': 'two almost-runs'},
	{'score': 0, 'cards': [8, 8, 4, 2, 0], 'name': 'no runs at all'},
	{'score': 6, 'cards': [4, 4, 3, 2, 10], 'name': 'double run of three [high pair]'},
	{'score': 6, 'cards': [4, 3, 3, 2, 10], 'name': 'double run of three [middle pair]'},
	{'score': 6, 'cards': [0, 4, 3, 2, 2], 'name': 'double run of three [low pair]'},
	{'score': 3, 'cards': [3, 2, 1, 10, 10], 'name': 'single run of three with unrelated pair'},
	{'score': 4, 'cards': [10, 4, 3, 2, 1], 'name': 'single run of four'},
	{'score': 8, 'cards': [9, 8, 7, 7, 6], 'name': 'double run of four [low-middle pair]'},
	{'score': 12, 'cards': [9, 8, 8, 7, 7], 'name': 'quadruple run of three [low and middle pairs]'},
	{'score': 9, 'cards': [9, 8, 8, 8, 7], 'name': 'triple run of three [middle pair]'},
	{'score': 12, 'cards': [9, 8, 8, 7, 7], 'name': 'quadruple run of three [low and middle pairs]'},
]

@pytest.mark.parametrize("case", run_score_cases, ids=[case['name'] for case in run_score_cases])
def test_run_scorer(case):
	calculated_score = scorer.score_runs(sorted(case['cards']))
	assert calculated_score == case['score']

pair_score_cases = [
	{'score': 0, 'cards': [6, 5, 3, 2, 10], 'name': 'no pairs 1'},
	{'score': 0, 'cards': [0, 1, 2, 3, 4], 'name': 'no pairs 2'},
	{'score': 0, 'cards': [10, 4, 3, 2, 1], 'name': 'no pairs 3'},
	{'score': 2, 'cards': [8, 8, 4, 2, 0], 'name': 'one pair 1'},
	{'score': 2, 'cards': [4, 4, 3, 2, 10], 'name': 'one pair 2'},
	{'score': 2, 'cards': [4, 3, 3, 2, 10], 'name': 'one pair 3'},
	{'score': 2, 'cards': [0, 4, 3, 2, 2], 'name': 'one pair 4'},
	{'score': 2, 'cards': [3, 2, 1, 10, 10], 'name': 'one pair 5'},
	{'score': 2, 'cards': [9, 8, 7, 7, 6], 'name': 'one pair 6'},
	{'score': 4, 'cards': [9, 8, 8, 7, 7], 'name': 'two pair 1'},
	{'score': 4, 'cards': [9, 8, 8, 7, 7], 'name': 'two pair 2'},
	{'score': 6, 'cards': [9, 8, 8, 8, 7], 'name': 'three of a kind'},
	{'score': 8, 'cards': [9, 9, 8, 8, 8], 'name': 'three of a kind and one pair 1'},
	{'score': 8, 'cards': [9, 9, 9, 8, 8], 'name': 'three of a kind and one pair 2'},
	{'score': 12, 'cards': [3, 2, 2, 2, 2], 'name': 'four of a kind and an almost-run'},
]

@pytest.mark.parametrize("case", pair_score_cases, ids=[case['name'] for case in pair_score_cases])
def test_pair_scorer(case):
	calculated_score = scorer.score_pairs(case['cards'])
	assert calculated_score == case['score']

fifteen_score_cases = [
	{'score': 0, 'cards': [6, 5, 3, 2, 10], 'name': 'no fifteens'},
	{'score': 16, 'cards': [10, 4, 4, 4, 4], 'name': 'best possible hand'},
	{'score': 4, 'cards': [10, 10, 2, 0, 0], 'name': 'aces 1'},
	{'score': 8, 'cards': [10, 10, 3, 0, 0], 'name': 'aces 2'},
	{'score': 8, 'cards': [6, 6, 7, 7, 8], 'name': 'sevens and eights'},
	{'score': 2, 'cards': [0, 0, 0, 1, 10], 'name': 'whole hand 17'}
]

@pytest.mark.parametrize("case", fifteen_score_cases, ids=[case['name'] for case in fifteen_score_cases])
def test_fifteen_scorer(case):
	calculated_score = scorer.score_fifteens(sorted(case['cards']))
	assert calculated_score == case['score']