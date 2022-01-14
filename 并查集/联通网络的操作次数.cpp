#include<iostream>
#include<vector>
using namespace std;

class Solution {
private:
	vector<bool> visit;
	vector<vector<int>> Matrix;
    void DFS(int v)
    {
    	visit[v]=true;
		
		for(int i=0;i<Matrix.size();i++)
		{
			if(Matrix[v][i]==1&&!visit[i]) DFS(i);
		}
	}
public:
    int makeConnected(int n, vector<vector<int>>& connections) 
	{
		if(connections.size()<n-1) 
		{
			return -1;
		}
		else
		{
			for(int i=0;i<n;i++)
			{
				vector<int> a(n,0);
				Matrix.emplace_back(a);
			}
			
			for(int i=0;i<connections.size();i++)
			{
				Matrix[connections[i][0]][connections[i][1]]=1;
				Matrix[connections[i][1]][connections[i][0]]=1;
			}
			
			visit.resize(n,false);
			
			int sum=0;
			for(int i=0;i<n;++i)
			{
				if(!visit[i])
				{
					sum++;
					DFS(i);
				}
			}
			
			
			return sum-1;
		}
    }
};


/*int main()
{
	int n;
	int
}*/









