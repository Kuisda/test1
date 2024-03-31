#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> ans;
        for(int i=0; i<nums.size()-2;i++){
            if(i > 0 && nums[i-1] == nums[i]){
                continue;
            }
            int right = nums.size()-1;
            for(int left = i+1;left < nums.size();++left){
                if(left > i+1 && nums[left] == nums[left-1]){
                    continue;
                }
                while(left < right && nums[i] + nums[right] + nums[left] > 0){
                    right--;
                }
                if(left == right) break;
                if(nums[i] + nums[right] + nums[left] == 0){
                    ans.emplace_back(vector<int>{nums[i],nums[right],nums[left]});
                }
            }
        }
        return ans;
    }
};