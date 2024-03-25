#include <vector>
using namespace std;
class DisjSet
{
  private:
	int comp_cnt;//连通分量
    vector<int> parent;
    vector<int> rank; // 秩

  public:
    DisjSet(int max_size) : parent(vector<int>(max_size)),
                            rank(vector<int>(max_size, 1))
    {
	    comp_cnt = max_size;
        for (int i = 0; i < max_size; ++i)
            parent[i] = i;
    }
    int find(int x)
    {
        return x == parent[x] ? x : (parent[x] = find(parent[x]));
    }
    void to_union(int x1, int x2)
    {
        int f1 = find(x1);
        int f2 = find(x2);
        if(f1==f2) return;
        if (rank[f1] > rank[f2]){
            parent[f2] = f1;
            rank[f2]+=rank[f1];
        }
        else
        {
            parent[f1] = f2;
            rank[f1]+=rank[f2];
        }
        comp_cnt--;
    }
    bool is_same(int e1, int e2)
    {
        return find(e1) == find(e2);
    }
};

class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int n = edges.size();
        DisjSet set(n);
        for(auto edge:edges){
            if(set.is_same(edge[0],edge[1])) return edge;
            else set.to_union(edge[0],edge[1]);
        }
        return {};
    }
};