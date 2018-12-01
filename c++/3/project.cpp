#include <iostream>
using namespace std;

int main()
{
	long int target = 600851475143;
	int currentHigh;
	for (int i = 1; i < target / 2; i++)
	{
		if (target % i == 0)
		{
			bool isPrime = true;
			for (int o = 2; o < i / 2; o++)
			{
				if (i % o == 0)
				{
					isPrime = false;
				}
			}
			if (isPrime)
			{
				currentHigh = i;
			}
		}
	}
	cout << currentFactor << endl;
	return 0;
}
