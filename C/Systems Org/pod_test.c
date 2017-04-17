#include <stdio.h>
#include <stdint.h>
#include <assert.h>

double power_of_difference(double x, double y, int32_t b);

int main() {
    assert(power_of_difference(5, 5, 20) == 0);
    assert(power_of_difference(50, 45, 10) == 9765625);
    assert(power_of_difference(206, 204, 20) == 1048576);
    assert(power_of_difference(206, 204, -3) == 0.125);
    assert(power_of_difference(-30, -26, -4) == 0.00390625);
    assert(power_of_difference(16.5, 15, 3) == 3.375);
    puts("All tests passed");
    return 0;
}
