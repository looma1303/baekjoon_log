#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>


int main() {
	int i, j, q, k, star_count;
	scanf("%d", &j);
	q = j;
	j = j * 2 - 1;
	for (i = 1; i <= j; i++) {
		if (i <= q) {
			star_count = 1 + 2 * (i-1);
		}

		else {
			star_count = star_count - 2;
		}



		for (k = 1; k <=  (j-star_count)/2; k++) {
			printf(" ");

		}

		for (k = 1; k <= star_count; k++) {
			printf("*");
		}


		if (i == j) {
			continue;
		}

		else {
			printf("\n");
		}


	}

	return 0;
}
