#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
//����Ѿ��������ȼۣ��ٳ��ֵ������������������ǰ�����ȼۣ����ڹ�����2���ȼ� 
class Solution
{   public:
		int numEquivDominoPairs(vector<vector<int>>& dominoes) 
		{
			int len=dominoes.size();
			int count=0;
			vector<int> num(100); //���г��ֵĶ�Ԫ�鶼ӳ�䵽10*x+y�ϣ���֤ǰһ��Ⱥ�һ��󣩣������ͽ��ȼ۵Ķ�Ԫ��ӳ�䵽��ͬһ��λ�ã��������ֵ������λ��������num��100���� 
			for(auto i:dominoes)
			{
				int val=i[0]<i[1]?i[1]*10+i[0]:i[0]*10+i[1];
				count+=num[val];
				num[val]++; 
			}
			
			return count; 

        }
		
}; 
