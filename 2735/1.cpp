#include<iostream>
#include<vector>
#include<numeric>
#include<algorithm>
using namespace std;

/*
    题目解读:
        可以通过增加成本x实现nums上每个位置对应成本右移，每个pos上的成本相加要最小，
    最小成本位置为pos，pos上的成本就是最小的。
    pos的下一位的最小成本则是min{nums[pos]+x,nums[pos+1]}
    以此类推
*/


class Solution {
public:
    long long minCost(vector<int>& nums, int x) {
        int n = nums.size();
        vector<int> f(nums);
        long long ans = accumulate(f.begin(),f.end(),0LL);//这个是对应一次都不右移的情况
        //右移次数最后只要加个最大值即可，这个次数k取值范围是[0,n-1]
        for(int k = 1;k < n;k++){
            for(int i = 0;i < n;i++){
                //这里其实算是左移了，但是左移和右移实际上都是一样的
                //左移k次后此时i位置的值为原来(i+k) % n位置的值
                f[i] = min(f[i], nums[(i + k) % n]);
            }
            ans = min(ans,static_cast<long long>(k)*x + accumulate(f.begin(),f.end(),0LL));
        }
        return ans;
    }
};

int main()
{
    Solution c;
    vector<int> nums{20,1,15};
    cout<<c.minCost(nums,5);
}