#ifndef _SCORER_H_
#include <stdbool.h>
#include <ctype.h>
#include "cache.h"
#include "hand_to_int.h"
#define KNOBS_BITMASK      0x0800
#define FOUR_FLUSH_BITMASK 0x0040
#define FIVE_FLUSH_BITMASK 0x0020
#define BASE_SCORE_BITMASK 0x001F

inline __attribute__((always_inline)) int
score_hand(int identifier, int starter_index, bool is_crib) {
  uint16_t score = CACHED_SCORE_TABLE[identifier];
  /*
   * since we already need a register
   * for the shifted value
   * this may save an instruction
   */
  uint16_t score_shifted = score >> starter_index;
  bool is_4flush = (!is_crib) && (score_shifted & FOUR_FLUSH_BITMASK);
  bool is_5flush = (score & FIVE_FLUSH_BITMASK);
#ifdef KNOBS_IN_CRIB
  bool has_knobs = !!(score_shifted & KNOBS_BITMASK);
#else
  bool has_knobs = !!((!is_crib) && (score_shifted & KNOBS_BITMASK));
#endif
  return (score & BASE_SCORE_BITMASK) + (is_5flush ? 5 : (is_4flush ? 4 : 0)) + has_knobs;
}

#endif 
