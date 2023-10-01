#include <stdio.h>
#include <stdbool.h>
void PRIME(int N) {
    bool Prime[N + 1];
    for (int i = 0; i <= N; i++) {
        Prime[i] = true;
    }
    Prime[0] = Prime[1] = false;

    for (int p = 2; p * p <= N; p++) {
        if (Prime[p]) {
            for (int i = p * p; i <= N; i += p) {
                Prime[i] = false;
            }
        }
    }
    printf("Prime numbers up to %d are:\n", N);
    for (int i = 2; i <= N; i++) {
        if (Prime[i]) {
            printf("%d ", i);
        }
    }
    printf("\n");
}

int main() {
    int N;

    printf("Enter a value for N: ");
    scanf("%d", &N);

    if (N <= 1) {
        printf("N must be greater than 1.\n");
        return 1;
    }

    PRIME(N);

    return 0;
}
