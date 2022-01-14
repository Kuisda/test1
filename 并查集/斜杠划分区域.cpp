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
		 int size=N*N*4;          //把每个方格分成了四块，以每个三角形为基础单元，所以共有N*N*4块
		 this->makeSet(size);
		 for(int i=0;i<N;i++)
		 {
		 	for(int j=0;j<N;j++)
		 	{
		 		int index=4*(i*N+j);
		 		if(grid[i][j]=='/')                      //每个1*1的小方块根据分块的斜线将相连的小三角形链接 
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
					int down=4*((i+1)*N+j);           //小方块间链接，无论两个小方块的划线怎么样上方方块的2号一定和下方0号相连 
					union_op(index+2,down); 
				}
				if(j+1<N)
				{
					int right=4*(i*N+(j+1));
					union_op(index+1,right+3);//左边方块的1号三角形和右方方块3号位的三角形相连 
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








