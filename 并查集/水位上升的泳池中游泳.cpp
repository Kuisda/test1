#include<iostream>
#include<vector>
#include<tuple>
#include<cmath>
#include<algorithm>
using namespace std;

class Set
{
	private:
		vector<int> union_set;
		vector<int> size;
		int setcount;
	public:
		void makeSet(int len)
		{
			for(int i=0;i<len;i++)
			{
				union_set.emplace_back(i);
			}
			size.resize(len,1);
			setcount=len;
		}
		
		int find_op(int x)
		{
			if(x!=union_set[x])
			{
				union_set[x]=find_op(union_set[x]);
			}
			return union_set[x];
		}
		
		void union_op(int x,int y)
		{
			x=find_op(x);
			y=find_op(y);
			if(x!=y)
			{
				if(size[x]<size[y])
				{
					swap(x,y);
				}
				union_set[y]=union_set[x];
				size[x]+=size[y];
				--setcount;
			}
		}
		bool connected(int x,int y)
		{
			x=find_op(x);
			y=find_op(y);
			return x==y;
		}
};

bool cmp(tuple<int,int,int>& a,tuple<int,int,int>& b)
{
	return get<2>(a)<get<2>(b);
}


class Solution 
{
public:
    int swimInWater(vector<vector<int>>& grid) 
	{
		int m=grid.size();
		int n=grid[0].size();
		
		vector<tuple<int,int,int>> edge;
		for(int i=0;i<m;i++)
		{
			for(int j=0;j<n;j++)
			{
				int id=i*n+j;
				if(i>0)
				{
					edge.emplace_back(id-n,id,max(grid[i][j],grid[i-1][j])); 
				}
				if(j>0)
				{
					edge.emplace_back(id-1,id,max(grid[i][j],grid[i][j-1]));
				}
			}
		}
		
		sort(edge.begin(),edge.end(),cmp);
		Set uf;
		uf.makeSet(m*n);
		int ans=0;
		for(auto i=edge.begin();i!=edge.end();i++)
		{
			uf.union_op(get<0>(*i),get<1>(*i));
			if(uf.connected(0,m*n-1))
			{
				ans=get<2>(*i);
				break;
			}
		}
		return ans;
    }
};


