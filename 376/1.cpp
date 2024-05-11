#include<vector>
using namespace std;

class Solution {
public:
    /*
        dp[i]表示[0,i]上，以nums[i]结尾的符合要求的最长子序列
        按照题目要求，单独的一个数可以作为子序列，所以dp初始化为1.
        flag[n]作为辅助数组，记录最长子序列dp[i]的第i个位置的num[i]与子序列的倒数第二个数的差是正还是负
        flag[n]初始化为0，如果flag[j]==0，说明它作为一个序列的起始，此时只要nums[i]!=nums[j]，就可以构成长度为2的子序列
        dp[i] = max(dp[i],dp[j]+1){(dp[i]-dp[j])*flag[j]==-1&&j在[0,i-1]区间上}

    */
    int wiggleMaxLength(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(n,1);
        vector<int> flag(n,0);
        for(int i=1;i<n;i++){
            for(int j=0;j<i;j++){
                //dp[j]有flag
                if((nums[i]-nums[j])*flag[j]<0){
                    if(dp[i]<dp[j]+1){
                        dp[i] = dp[j]+1;
                        flag[i] = -flag[j];
                    }
                    //dp[j]没有flag，作为序列起始
                }else if(flag[j]==0 && nums[i]-nums[j]!=0){
                    dp[i] = dp[j]+1;
                    flag[i] = nums[i]-nums[j];
                }
    
            }
        }
        return dp[n-1];
    }
};

int main(){
    Solution c;
    vector<int> nums{1,7,4,9,2,5};
    c.wiggleMaxLength(nums);
}