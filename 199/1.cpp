#include<vector>
#include<queue>
#include<unordered_map>
#include<algorithm>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
//维护一个记录<高度，val>的mp
//max_depth 记录最终树高度，用于遍历mp
//记录当前节点高度，添加val到mp，保证层序遍历先入左子树，这样保证了同一层最后一个覆盖到mp上的val一定是同层最右节点

class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        unordered_map<int,int> rightMostValueAtDepth;
        int maxDepth = -1;
        queue<pair<TreeNode*,int>> q;
        vector<int> ans;
        if(!root) return ans;
        q.push(pair<TreeNode*,int>(root,0));
        while(!q.empty()){
           auto p = q.front();
           q.pop();
           TreeNode * node = p.first;
           int depth = p.second;
           maxDepth = max(maxDepth,depth);

           rightMostValueAtDepth[depth] = node->val;

           if(node->left) q.push(pair<TreeNode*,int>(node->left,depth+1));
           if(node->right) q.push(pair<TreeNode*,int>(node->right,depth+1));
        }
        for(int depth=0;depth<=maxDepth;depth++){
            ans.emplace_back(rightMostValueAtDepth[depth]);
        }

        return ans;

    }
};