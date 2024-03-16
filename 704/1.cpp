#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0,right = nums.size()-1;
        while(left<= right){
            int mid = (left + right)/2;
            if(nums[mid]==target)return mid;
            else if(nums[mid]>target) right = mid - 1;
            else left = mid + 1;
        }
        return -1;
    }
};

int main(){
    Solution c;
    vector<int> nums{5};
    c.search(nums,5);
}