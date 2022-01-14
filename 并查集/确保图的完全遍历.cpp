#include<iostream>
#include<vector> 
#include<algorithm>
using namespace std;

class union_find
{
	public:
	vector<int> set;
	vector<int> pow;
	int setcount;
	void makeSet(int len)
	{
		for(int i=0;i<len;i++)
		{
			set.emplace_back(i);
		}
		pow.resize(len,1);
		setcount=len;
	}
	int find_op(int x)
	{
		int father=set[x];
		if(father==x) return father;
		else 
		{
			set[x]=find_op(father);
			return set[x];
		}
	}
	
	bool union_op(int x,int y)
	{
		x=find_op(x);
		y=find_op(y);
		
		if(x==y) return false;
		
		if(pow[x]<pow[y])
		{
			swap(x,y);
		}
		set[y]=set[x];
		pow[x]+=pow[y];
		--setcount;
		return true;
	}
}; 


class Solution 
{
public:
    int maxNumEdgesToRemove(int n, vector<vector<int>>& edges) 
	{
		for(auto& edge:edges)
		{
			edge[1]--;
			edge[2]--;
		}
		
		union_find a1,b1;
		a1.makeSet(n);
		b1.makeSet(n);
		int ans=0;                  //删除的边数 
		
		for(const auto& edge:edges)  //考虑要给各个分离的点添加边，为了使添加的边最小，先添加公共边（因为可以同时作用于两个并查集）的效率更高 
		{
			if(edge[0]==3)
			{
				if(a1.union_op(edge[1],edge[2])==false)//如果新边的两边节点已经在联通状态下，就 说明这个新边是可删除的，ans++ 
				{
					ans++;
				}
				else
				{
					b1.union_op(edge[1],edge[2]);//公共边的作用对两个并查集是都有的 
				}
			}
		}
		
		for(const auto& edge:edges)
		{
			if(edge[0]==1)
			{
				if(a1.union_op(edge[1],edge[2])==false)
				{
					ans++;
				}
			}
		}
		
		for(const auto& edge:edges)
		{
			if(edge[0]==2)
			{
				if(b1.union_op(edge[1],edge[2])==false)
				{
					ans++;
				}
			}
		}
		
		if(a1.setcount!=1||b1.setcount!=1) return -1;//如果都连了还是不连通 
		
		return ans;
    }
};
