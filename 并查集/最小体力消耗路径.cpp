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
	    int Setcount; 
	public:
		void makeSet(int len);
		void union_op(int x,int y);
		int find_op(int target);
		bool connected(int x,int y);
};

void Set::makeSet(int len)
{
	for(int i=0;i<len;i++)
	{
		union_set.emplace_back(i);
	}
	size.resize(len,1); 
	Setcount=len;
}


int Set::find_op(int target)
{
	if(target!=union_set[target])
	{
		union_set[target]=find_op(union_set[target]);
	}
	return union_set[target];
}

void Set::union_op(int x,int y)
{
	x=find_op(x);
	y=find_op(y);
	
	if(x!=y)
	{
		if(size[x]<size[y])
		{
			swap(x,y);
		}
		union_set[y]=x;   //表示y树的父节点是x,这里写union_set[x]也行，因为两者是相等的 
		size[x]+=size[y];
		--Setcount;
	}
}

bool Set::connected(int x,int y)
{
	x=find_op(x);
	y=find_op(y);
	return x==y;
}

bool cmp(tuple<int,int,int>& a,tuple<int,int,int>& b)
{	 
	return get<2>(a)<get<2>(b);
}


class Solution 
{	
public:
    int minimumEffortPath(vector<vector<int>>& heights) 
	{
		int m=heights.size();
		int n=heights[0].size();
		
		vector<tuple<int,int,int>> edge;
		for(int i=0;i<m;i++)
		{
			for(int j=0;j<n;j++)
			{
				int id=i*n+j;
				if(i>0)
				{
					edge.emplace_back(id-n,id,abs(heights[i][j]-heights[i-1][j]));
				}
				if(j>0)
				{
					edge.emplace_back(id-1,id,abs(heights[i][j]-heights[i][j-1]));
				}
			}
		}
		sort(edge.begin(),edge.end(),cmp);
		Set uf;
        uf.makeSet(m*n);
        int ans=0;
		for(auto i=0;i!=edge.size();i++)
		{
			uf.union_op(get<0>(edge[i]),get<1>(edge[i]));
			if(uf.connected(0,m*n-1))
			{
				ans=get<2>(edge[i]);
				break;
			}
		}
		
		return ans; 
    }
};








