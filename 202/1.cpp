#include<unordered_set>
#include<iostream>
using namespace std;


class Solution {
public:
    int cal(int n){
        int sum = 0;
        while(n){
            int tmp = n%10;
            sum += tmp*tmp;
            n/=10;
        }
        return sum;
    }
    bool isHappy(int n) {
        unordered_set<int> myset;
        myset.emplace(n);
        while(1){
            int tmp = cal(n);
            if(tmp == 1) return true;
            if(myset.count(tmp)!=0)return false;
            myset.emplace(tmp);
            n = tmp;
        }
    }
};

int main(){
    Solution c;
    cout<<c.isHappy(19);
}