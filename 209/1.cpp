#include <iostream>
#include <vector>
using namespace std;


class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int left = 0,right = 0;
        int sum = 0;
        int minlen = nums.size()+1;
        while(right <nums.size()){
            sum += nums[right];
            while(sum >=target){
                minlen = min(minlen,right-left+1);
                sum-=nums[left];
                left++;
            }
            right++;
        }
        return minlen==nums.size()+1? 0:minlen;
    }
};