#include<vector>
#include<algorithm>
using namespace std;

class Solution {
private:
    vector<vector<int>> ans;
    vector<int> tmp; 
    
public:
    void backtracking(vector<int>& candidates,int target,int idx){
        if(target<0|| idx >= candidates.size()) return;
        if(target==0){
            ans.emplace_back(tmp);
            return;
        }

        for(int i=idx;i<candidates.size() && candidates[i] <= target;i++){
            if(i>idx && candidates[i]==candidates[i-1])continue;
            tmp.emplace_back(candidates[i]);
            backtracking(candidates,target-candidates[i],i+1);
            tmp.pop_back();
        }
    }
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(),candidates.end());
        backtracking(candidates,target,0);
        return ans;
    }
};

int main(){
    Solution c;
    vector<int> candidates{10,1,2,7,6,1,5};
    c.combinationSum2(candidates,8);
}