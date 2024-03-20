#include<vector>
#include<string>
#include<limits.h>
using namespace std;
//记录字母表中出现的最小次数
//只要最小次数不为0，说明这个字母一定出现在所有的word中
class Solution {
public:
    vector<string> commonChars(vector<string>& words) {
        vector<int> minfreq(26,INT_MAX);
        vector<int> freq(26,0);
        for(string word:words){
            fill(freq.begin(),freq.end(),0);
            for(auto ch:word){
                freq[ch-'a']++;
            }

            for(int i=0;i<26;i++){
                minfreq[i] = min(minfreq[i],freq[i]);
            }
        }
        vector<string> ans;
        for(int i=0;i<26;i++){
            for(int j=0;j<minfreq[i];j++){
                ans.emplace_back(string(1, i + 'a'));
            }
        }
        return ans;
    }
};