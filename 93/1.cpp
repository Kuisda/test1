#include<vector>
#include<string>
using namespace std;
class Solution {
private:
    vector<string> ans;
    vector<string> tmp;
public:
    string buildString(vector<string> a){
        string ss = "";
        int n = a.size();
        for(int i=0;i<n;i++){
            ss += a[i];
            if(i!=n-1){
                ss+='.';
            }
        }
        return ss;
    }
    bool Judge(string s,int start,int length){
        if(length==1)return true;
        if(s[start]=='0') return false;
        if(length > 3) return false;
        if(stoi(s.substr(start,length)) > 255)return false;
        return true;
    }
    void backtracking(string s,int idx,int split_time){
        if(idx >= s.size()) return;//对应只只分成三段但是已经遍历完的情况
        if(split_time == 3 && Judge(s,idx,s.size()-idx)){
            tmp.emplace_back(s.substr(idx));
            ans.emplace_back(buildString(tmp));
            tmp.pop_back();
            return;
        }

        if(split_time == 3)return;
        for(int i=idx;i<s.size();i++){
            if(Judge(s,idx,i-idx+1)){
                tmp.emplace_back(s.substr(idx,i-idx+1));
            }else{
                continue;
            }
            backtracking(s,i+1,split_time+1);
            tmp.pop_back();
        }
    }
    vector<string> restoreIpAddresses(string s) {
        backtracking(s,0,0);
        return ans;
    }
};

int main(){
    Solution c;
    string s = "101023";
    c.restoreIpAddresses(s);
}