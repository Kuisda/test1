#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;


class Solution {
public:
    int minOperationsMaxProfit(vector<int>& customers, int boardingCost, int runningCost) {
        int cur_profit = 0,max_profit = 0;
        int max_turn = -1;
        int surplus_customer = 0;
        int i = 0;
        while(1)
        {
            if(i>=customers.size()&&surplus_customer==0)break;

            int cur_customer = surplus_customer;
            if(i<customers.size()){
                cur_customer += customers[i];
            }
            if(cur_customer < 4){
                cur_profit +=cur_customer * boardingCost - runningCost;
                surplus_customer = 0;
            }
            else{
                cur_profit +=4 * boardingCost - runningCost;
                surplus_customer = cur_customer - 4;
            }
            if(max_profit < cur_profit){
                max_profit = cur_profit;
                max_turn = i+1;
            }
            i++;
        }
        return max_turn;

    }
};

int main()
{
    vector<int> customer{8,3};
    Solution c;
    cout << c.minOperationsMaxProfit(customer,5,6);

}