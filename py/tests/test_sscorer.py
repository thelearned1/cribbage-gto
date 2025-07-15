import pytest
import scorer
import score_cache

score_shand_cases = [
	{
		'name': '', 
		'hand': [], 
		'score': 0, 
		'no_knobs_crib_score': 0, 
		'knobs_crib_score': 0, 
		'starter_index': 0
	},
] 

@pytest.fixture(scope="module", autouse=True)
def build_cache():
	score_cache.load_scores_cache()

@pytest.mark.parametrize("case", score_shand_cases, ids=[case['name'] for case in score_shand_cases])
def test_score_shand(case):
	score_cache.build_cache()
	pass