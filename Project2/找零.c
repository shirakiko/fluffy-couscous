#include<stdio.h>
int main() 
{

	int change = 0, amount = 0, price = 0;

	
	scanf_s("%d", &amount);
	printf("总金额为%d元\n", amount);
	

	scanf_s("%d", &price);
	printf("金额为%d元\n", price);
	change = amount - price;

	printf("找您%d元\n", change);

	return 0;
}