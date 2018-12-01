#include <iostream>
using namespace std;

int main()
{
	int fib[2] = {1,2};
	int current;
	int total = 2;
	while (current < 4000000)
	{
		current = fib[0] + fib[1];
		if (current%2 == 0)
		{
			total += current;
		}
		fib[0] = fib[1];
		fib[1] = current;
	}
	cout << total << endl;
	return 0;
}
