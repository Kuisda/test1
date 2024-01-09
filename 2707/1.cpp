#include<iostream>
#include<string>
#include<vector>
#include<unordered_map>
using namespace std;

//d[i]表示s[0...i-1]的子问题
//d[i]取两种情况的最小值:
//1.s[i-1]是额外字符，则d[i] = d[i-1] + 1
//2.遍历[0,i-1],s[j,i-1]是否存在于dictionary中，若存在则d[i] = min d[j]

class Solution {
public:
    int minExtraChar(string s, vector<string>& dictionary) {
        int n =s.size();
        int d[n+1];
        d[0] = 0;
        unordered_map<string,int>mp;
        for(auto str : dictionary){
            mp[str]++;
        }
        for(int i=1;i<=n;i++){
            d[i] = d[i-1] + 1;
            for(int j=i-1;j>=0;j--){
                if(mp.count(s.substr(j,i-j))){//子字符串 s[j...i−1]是否在mp中
                    d[i] = min(d[i],d[j]);
                }
            }
        }
        return d[n];
    }
};
