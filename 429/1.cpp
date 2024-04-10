#include<vector>
#include<queue>
using namespace std;
class Node {
public:
    int val;
    vector<Node*> children;
    Node() {}
    Node(int _val) {
        val = _val;
    }
    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};


class Solution {
public:
    vector<vector<int>> levelOrder(Node* root) {
        vector<vector<int>> ans;
        queue<Node*> q;
        if(!root) return ans;
        q.push(root);
        while(!q.empty()){
            int n = q.size();
            vector<int> nums;
            for(int i=0;i<n;i++){
                Node * node = q.front();
                q.pop();
                nums.emplace_back(node->val);
                for(int i=0;i<node->children.size();i++){
                    q.push(node->children[i]);
                }
            }
            ans.emplace_back(nums);
        }
        return ans;
    }
};