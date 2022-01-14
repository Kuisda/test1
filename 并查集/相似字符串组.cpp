#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

class Set
{
	private:
	    vector<int> union_set;
	    vector<int> size; 
	public:
		int Setcount;
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


class Solution 
{
private:
	bool judge(string a,string b)
	{
		int ans=0;
		for(int i=0;i<a.length();i++)
		{
			ans+=(a[i]!=b[i]);
		}
		return ans<=2;
	}
public:
    int numSimilarGroups(vector<string>& strs) 
	{
		Set uf;
		uf.makeSet(strs.size());
		for(int i=0;i<strs.size()-1;i++)
		{
			for(int j=i+1;j<strs.size();j++)
			{
				if(judge(strs[i],strs[j]))
				{
					uf.union_op(i,j);
				}
			}
		}
		
		return uf.Setcount;

    }
};
