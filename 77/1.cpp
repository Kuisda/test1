#include<vector>
using namespace std;

class Solution {
public:
    void backtracking(vector<vector<int>> &ans,vector<int> &vec,int n,int pos,int k){
        if(k==0){
            ans.emplace_back(vec);
            return;
        }
        if(pos > n) return;
        if(n-pos+1 < k)return;
        for(int i=pos;i<=n;i++){
            vec.emplace_back(i);
            backtracking(ans,vec,n,i+1,k-1);
            vec.pop_back();
        }
    }
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> ans;
        vector<int> vec;
        backtracking(ans,vec,n,1,k);
        return ans;
    }
};


int main(){
    Solution c;
    c.combine(4,2);
}