#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
//如果已经有两个等价，再出现第三个，则第三个都与前两个等价，等于贡献了2个等价 
class Solution
{   public:
		int numEquivDominoPairs(vector<vector<int>>& dominoes) 
		{
			int len=dominoes.size();
			int count=0;
			vector<int> num(100); //所有出现的二元组都映射到10*x+y上（保证前一项比后一项大），这样就将等价的二元组映射到了同一个位置，并且其键值都是两位数，落在num【100】内 
			for(auto i:dominoes)
			{
				int val=i[0]<i[1]?i[1]*10+i[0]:i[0]*10+i[1];
				count+=num[val];
				num[val]++; 
			}
			
			return count; 

        }
		
}; 
