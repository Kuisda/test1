#include<vector>
#include<algorithm>
using namespace std;
class Solution {
public:
    int longestMonotonicSubarray(vector<int>& nums) {
        int pos=0,len = 1;
        int Upmaxlen = 1,Downmaxlen = 1;
        for(int i=1;i<nums.size();i++) {
            if(nums[i] > nums[i-1]){
                len++;
                Upmaxlen = max(Upmaxlen,len);
            }else{
                pos = i;
                len = 1;
            }
        }
        pos = 0,len = 1;
        for(int i=1;i<nums.size();i++) {
            if(nums[i] < nums[i-1]){
                len++;
                Downmaxlen = max(Downmaxlen,len);
            }else{
                pos = i;
                len = 1;
            }
        }
        return max(Upmaxlen,Downmaxlen);
    }
};