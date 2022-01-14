#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

class Set
{
	private:
	    vector<int> union_set;
	    vector<int> size;    //权重，小树合并到大树去，如果没有的话 ，【01，02，03】这种就不能并到一起去 
	    int len;
	    int Setcount; //连通分量 
	public:
		void makeSet(int len);
		void union_op(int x,int y);
		int find_op(int target);
		int makeConnected(int n, vector<vector<int>>& connections);
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
		union_set[y]=x;   //表示y树的父节点是x 
		size[x]+=size[y];
		--Setcount;
	}
}

int Set::makeConnected(int n,vector<vector<int>>& connections)
{
	if(connections.size()<n-1)
	{
		return -1;
	}
	
	len=n;
	this->makeSet(n);
	for(int i=0;i<connections.size();i++)
	{
		this->union_op(connections[i][0],connections[i][1]);
	}
	
	return Setcount-1;
}

int main()
{
	int n;
	cin>>n;
	int arc;
	cin>>arc;
	vector<vector<int>> co;
	for(int i=0;i<arc;i++)
	{
		vector<int> s;
		for(int j=0;j<2;j++)
		{
			int temp;
			cin>>temp;
			s.emplace_back(temp);
		}
		co.emplace_back(s);
	}
	Set c;
	cout<<c.makeConnected(n,co);
}



