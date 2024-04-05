#include<vector>
#include<queue>
#include<unordered_map>
using namespace std;

class cmp{
    public:
        bool operator()(const pair<int,int>& a,const pair<int,int>& b){
            return a.second > b.second;
        }
};

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> mp;
        for(int num : nums){
            if(mp[num])mp[num]++;
            else mp[num] = 1;
        }

        priority_queue<pair<int,int>,vector<pair<int,int>>,cmp> p;

        for(auto i = mp.begin();i!=mp.end();i++){
            p.emplace(*i);
            if(p.size() > k){
                p.pop();
            }
        }
        vector<int> ans;
        while(!p.empty()){
            ans.emplace_back(p.top().first);
            p.pop();
        }
        return ans;

    }
};