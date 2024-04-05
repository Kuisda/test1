#include<deque>
#include<vector>
using namespace std;

class monotonic_queue{
    private:
        deque<int> q;
    public:
        void pop(int value){
            while(!q.empty() && q.front() == value){
                q.pop_front();
            }
        }
        void push(int value){
            while(!q.empty() && value > q.back()){
                q.pop_back();
            }
            q.push_back(value);
        }
        int front(){
            return q.front();
        }
};

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        monotonic_queue q;
        vector<int> ans;
        for(int i=0;i<k;i++){
            q.push(nums[i]);
        }
        ans.emplace_back(q.front());
        for(int i=k;i<nums.size();i++){
            q.pop(nums[i-k]);
            q.push(nums[i]);
            ans.emplace_back(q.front());
        }
        return ans;
    }
};


int main(){
    Solution c;
    vector<int> nums= {-7,-8,7,5,7,1,6,0};
    c.maxSlidingWindow(nums,4);
}