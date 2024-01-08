#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;

//以point[i]为拐点，有m个点到point[i]的距离相等，则可以构成的元组数量为m*(m-1)
//使用一个哈希表<距离，点数量>保存每个节点到point[1]的距离,由于每个节点不同且选不同的点作为拐点时算作一种新情况，所以不会重复

class Solution {
public:
    int distance(vector<int> pos1, vector<int> pos2){
        return (pos1[0] - pos2[0])*(pos1[0] - pos2[0]) + (pos1[1] - pos2[1])*(pos1[1] - pos2[1]);
    }
    
    int numberOfBoomerangs(vector<vector<int>>& points) {
        int ans = 0;
        for(auto &p:points){
            unordered_map<int,int>map;
            for(auto &q:points){
                int dis = distance(p,q);
                map[dis]++;
            }
            for(auto iter = map.begin(); iter != map.end();iter++){
                int m = iter->second;
                ans += m*(m-1);
            }
        }
        return ans;
    }  
};

int main()
{
    vector<int>a{0,0};
    vector<int>b{1,0};
    vector<int>c{2,0};

    vector<vector<int>> points{a,b,c};
    Solution S;
    cout<< S.numberOfBoomerangs(points);

}