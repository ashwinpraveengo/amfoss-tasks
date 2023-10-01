#include <iostream>
#include <vector>
using namespace std;
void SieveOfEratosthenes(int N) {
    vector<bool> isPrime(N + 1, true);
    isPrime[0] = isPrime[1] = false;

    for (int p = 2; p * p <= N; p++) {
        if (isPrime[p]) {
            for (int i = p * p; i <= N; i += p) {
                isPrime[i] = false;
            }
        }
    }
    cout << "Prime numbers up to " << N << " are:" << endl;
    for (int i = 2; i <= N; i++) {
        if (isPrime[i]) {
            cout << i << " ";
        }
    }
    cout << endl;
}
int main() {
    int N;

    cout << "Enter a value for N: ";
    cin >> N;

    if (N <= 1) {
        cout << "N must be greater than 1." << endl;
        return 1;
    }
    SieveOfEratosthenes(N);
    return 0;
}
