#include <time.h>
#include <stdio.h>
#include <stdlib.h>

int main() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);

	time_t t = time(NULL);
	srand(1699115700);
	printf("%d\n" t);
	printf("%lld", ((long long)rand() << 32) | rand());
    return 0;
}
