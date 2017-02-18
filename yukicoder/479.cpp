#include <vector>
#include <iostream>
#include <utility>

/*
  n-th node costs 2^(n+1) yen, while buying all (0...n-1)th nodes costs 2^n-1 yen.
*/

using namespace std;

int main(void)
{
	// input
	int n, m;
	cin >> n >> m;
	cin.ignore();
	vector<vector<int>> adj_list(n);

	for ( int i = 0; i < m; ++i )
	{
		int node0, node1;
		cin >> node0 >> node1;
		cin.ignore();
		if ( node0 < node1 )
		{
			swap(node0, node1);
		}
		adj_list.at(node0).push_back(node1);
	}

	vector<bool> buy_flag(n, 0);
	for ( int i = n - 1; i >= 0; --i )
	{
		if ( buy_flag.at(i) == 1)
			continue;
		for ( const auto node: adj_list.at(i) )
		{
			buy_flag.at(node) = 1;
		}
	}

	// output
	bool noshow_zero = true;
	for ( auto i = n - 1; i >= 0; --i )
	{
		if ( noshow_zero )
		{
			if ( buy_flag.at(i) == 0)
				continue;
			else
				noshow_zero = false;
		}
		cout << buy_flag.at(i);
	}
	cout << endl;

	return 0;
}
