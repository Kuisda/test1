#include<iostream>
#include<string>
#include<unordered_map>
#include<vector>
using namespace std;


class Solution {
public:
    int countWords(vector<string>& words1, vector<string>& words2) {
        unordered_map<string,int> mp1,mp2;
        for(auto s : words1){
            /*
            if(mp1.find(s)==mp1.end()){
                mp1.emplace(s,1);
            }
            else{
                mp1[s]+=1;
            }
            */
           mp1[s]++;
        }
        for(auto s: words2){
            if(mp2.find(s)==mp2.end()){
                mp2.emplace(s,1);
            }
            else{
                mp2[s]+=1;
            }
        }
        int ans = 0;
        for(auto iter = mp1.begin();iter != mp1.end();++iter){
            if(iter->second==1 && mp2.find(iter->first)!=mp2.end() && mp2[iter->first]==1){
                ans+=1;
            }
        }
        return ans;
    }
};


int main(){
    vector<string> words1{"leetcode","is","amazing","as","is"};
    vector<string> words2{"amazing","leetcode","is"};
    Solution c;
    cout << c.countWords(words1,words2);
}