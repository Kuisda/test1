#include<vector>
#include<algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> ans;
        sort(nums.begin(), nums.end());
        int n = nums.size();
        for(int first=0;first<n-3;first++){
            if(first != 0 && nums[first] == nums[first-1]){
                continue;
            }
            for(int second = first+1;second < n -2;second++){
                if(second != first+1 && nums[second] == nums[second-1]){
                    continue;
                }

                int right = n - 1;
                for(int left = second+1;left < right;left++){
                    if(left != second+1 && nums[left] == nums[left-1]){
                        continue;
                    }
                    while(left < right && (long)nums[first] + nums[second] + nums[left] + nums[right] > target){
                        right--;
                    }
                    if(left == right) break;
                    if((long)nums[first] + nums[second] + nums[left] + nums[right] == target){
                        ans.emplace_back(vector<int>{nums[first],nums[second],nums[left],nums[right]});
                    }
                }
            }
        }
        return ans;
    }
};


int main(){
    Solution c;
    vector<int> nums{-2,-1,-1,1,1,2,2};
    c.fourSum(nums,0);
}