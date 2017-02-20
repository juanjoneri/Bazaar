#include <stdio.h>

int power (int base, int n);

int main ()
{
	int base, n;
	printf("imput base:\n");
	scanf("%d", &base);
	printf("imput exponent:\n");
	scanf("%d", &n);

	printf("%d ^ %d = %d \n",base, n, power(base, n));
	return 0;
}

int power (int base, int n)
{
	int i, p;
	p = 1;

	for (i = 1; i <=n; ++i){
		p = p * base;
	}
	return p;
}
