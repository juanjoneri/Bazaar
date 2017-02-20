#include <stdio.h>

float division (float n, float d);

int main ()
{
    float n, d;

    printf("imput numerador\n");
    scanf("%f",&n);
    printf("imput denominador\n");
    scanf("%f", &d);
    printf("%.1f / %.1f = %.3f \n", n, d, division(n, d));

}

float division (float n, float d)
{
    return n/d;
}
