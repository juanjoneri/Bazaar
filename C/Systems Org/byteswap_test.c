#include <stdio.h>
#include <stdint.h>
#include <assert.h>

void byteswap(uint32_t *x);

int main() {
    uint32_t x = 0x3d744b26;
    byteswap(&x);
    assert(x == 0x264b743d);
    puts("All tests passed");
    return 0;
}
