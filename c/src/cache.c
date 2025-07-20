#include "cache.h"
static const char cache_filename[] = "cribbage_scores.cge";

static int ESTIMATED_SCORE_COUNT = 2598960;

__attribute__((constructor))
int
load_cache () {
	FILE * fptr = fopen(cache_filename, "rb");

	if (NULL == fptr) {
		fprintf(stderr, "could not build score cache: file %s does not exist\n", cache_filename);
		exit(1);
	}

	int object_count = 0;
	while (true) {

		if (object_count >= ESTIMATED_SCORE_COUNT) {
			uint16_t * backup = CACHED_SCORE_TABLE;
			CACHED_SCORE_TABLE = malloc(sizeof(uint16_t)*2*ESTIMATED_SCORE_COUNT);
			memcpy(CACHED_SCORE_TABLE, backup, sizeof(uint16_t)*ESTIMATED_SCORE_COUNT);
			free(backup);
		}

		int * hand;
		uint16_t * score;
		if (fread(hand, sizeof(int), 1, fptr) < 1) {
			break;
		}
		if (fread(score, sizeof(uint16_t), 1, fptr) < 1) {
			fprintf(
				stderr, 
				"could not build score cache: failed loading object %d (file pointer %ld)\n",
				object_count,
				ftell(fptr)
			);
			exit(1);
		}
		CACHED_SCORE_TABLE[*hand] = *score;
		object_count++;
	}

	fclose(fptr);
	return object_count;
}

__attribute__((destructor))
void 
cleanup () {
	free(CACHED_SCORE_TABLE);
}