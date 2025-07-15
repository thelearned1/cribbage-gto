#include 

int
score_hand(int identifier, int starter_index, bool is_crib) {
  uint16_t score = CACHED_SCORE_TABLE[identifier];
  uint8_t base_score = score & (BASE_SCORE_BITMASK);
  bool has_5flush = score & (FIVE_FLUSH_BITMASK);
  bool has_4flush = (score & (FOUR_FLUSH_BITMASK << starter_index)) && (!is_crib);
  bool has_knobs = (score & (KNOBS_BITMASK << starter_index)) && (!is_crib || RULESET.knobs_in_crib);
  base_score += (has_5flush ? 5 : (has_4flush ? 4 : 0));
  base_score += (has_knobs ? 1 : 0);
  return base_score;
}