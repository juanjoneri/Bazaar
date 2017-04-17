#include <stdio.h>
#include <stdint.h>
#include <assert.h>

uint64_t gcd(uint64_t x, uint64_t y);

int main() {
    assert(gcd(309,66) == 3);
    assert(gcd(66, 309) == 3);
    assert(gcd(3113041662, 11570925) == 462837);
    assert(gcd(427366239731, 4273650023214) == 6499);
    assert(gcd(427366239731687, 4268765973650023214) == 1);
    puts("All tests passed");
    return 0;
}
