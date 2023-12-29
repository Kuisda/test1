#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int buyChoco(vector<int>& prices, int money) {
        int minNum = 101,se_minNum;
        for(auto first = prices.begin();first!=prices.end();first++){
            if(*first < minNum){
                se_minNum = minNum;
                minNum = *first;
            }
            else if(*first < se_minNum){
                se_minNum = *first;
            }
        }
        return minNum+se_minNum<=money ? money - minNum - se_minNum : money;
    }
};

int main(){
    Solution c;
    vector<int> prices{1,2,2};
    cout<<c.buyChoco(prices,3);
}