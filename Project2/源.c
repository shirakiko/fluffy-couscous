#include<stdio.h>
int main() 
{

	int change = 0, amount = 0, price = 0;

	
	scanf_s("%d", &amount);
	printf("�ܽ��Ϊ%dԪ\n", amount);
	

	scanf_s("%d", &price);
	printf("���Ϊ%dԪ\n", price);
	change = amount - price;

	printf("����%dԪ\n", change);

	return 0;
}