#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std; 

class Solution 
{private:
	vector<int> pow;
	vector<int> set;
	int SetCount;
	void makeSet(int len)
	{
		for(int i=0;i<len;i++)
		{
			set.emplace_back(i);
		}
		pow.resize(len,1);
		SetCount=len;
	}
	int  find_op(int x)
	{
		int father=set[x];
		if(father==x)
		{
			return x;
		}
		else
		{
			father=find_op(father);
			set[x]=father;
			return father;
		}
	}
	
	void union_op(int x,int y)
	{
		x=find_op(x);
		y=find_op(y);
		
		if(x!=y)
		{
			if(pow[x]<pow[y])
			{
				swap(x,y);
			}
			set[y]=set[x];
			pow[x]+=pow[y];
			SetCount--;
		}
	}
	
	
public:
    int regionsBySlashes(vector<string>& grid) 
	{
		 int N=grid.size();
		 int size=N*N*4;          //��ÿ������ֳ����Ŀ飬��ÿ��������Ϊ������Ԫ�����Թ���N*N*4��
		 this->makeSet(size);
		 for(int i=0;i<N;i++)
		 {
		 	for(int j=0;j<N;j++)
		 	{
		 		int index=4*(i*N+j);
		 		if(grid[i][j]=='/')                      //ÿ��1*1��С������ݷֿ��б�߽�������С���������� 
		 		{
		 			this->union_op(index,index+3);
		 			this->union_op(index+1,index+2);
				}
				else if(grid[i][j]=='\\')
				{
					this->union_op(index,index+1);
					this->union_op(index+2,index+3);
				}
				else
				{
					union_op(index,index+1);
					union_op(index+1,index+2);
					union_op(index+2,index+3);
				}
				
				if(i+1<N) 
				{
					int down=4*((i+1)*N+j);           //С��������ӣ���������С����Ļ�����ô���Ϸ������2��һ�����·�0������ 
					union_op(index+2,down); 
				}
				if(j+1<N)
				{
					int right=4*(i*N+(j+1));
					union_op(index+1,right+3);//��߷����1�������κ��ҷ�����3��λ������������ 
				}
			}
		 }
		return SetCount;  
    }
};


int main()
{
	int n;
	cin>>n;
	vector<string> grid;
	for(int i=0;i<n;i++)
	{
		string s;
		cin>>s;
		grid.emplace_back(s);
	}
	Solution c;
	c.regionsBySlashes(grid);
}








