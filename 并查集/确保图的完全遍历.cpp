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
		int ans=0;                  //ɾ���ı��� 
		
		for(const auto& edge:edges)  //����Ҫ����������ĵ���ӱߣ�Ϊ��ʹ��ӵı���С������ӹ����ߣ���Ϊ����ͬʱ�������������鼯����Ч�ʸ��� 
		{
			if(edge[0]==3)
			{
				if(a1.union_op(edge[1],edge[2])==false)//����±ߵ����߽ڵ��Ѿ�����ͨ״̬�£��� ˵������±��ǿ�ɾ���ģ�ans++ 
				{
					ans++;
				}
				else
				{
					b1.union_op(edge[1],edge[2]);//�����ߵ����ö��������鼯�Ƕ��е� 
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
		
		if(a1.setcount!=1||b1.setcount!=1) return -1;//��������˻��ǲ���ͨ 
		
		return ans;
    }
};
