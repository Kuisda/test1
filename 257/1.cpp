#include<vector>
#include<string>
using namespace std;
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    void construct_path(TreeNode *root,vector<int>& path,vector<string>& paths){
        path.emplace_back(root->val);
        if(root->left == nullptr && root->right == nullptr){
            string s;
            for(int i=0;i<path.size()-1;i++){
                s += to_string(path[i]);
                s += "->";
            }
            s += to_string(path[path.size()-1]);
            paths.emplace_back(s);
            return;
        }
        if(root->left){
            construct_path(root->left,path,paths);
            path.pop_back();
        }
        if(root->right){
            construct_path(root->right,path,paths);
            path.pop_back();
        }
    }
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<int> path;
        vector<string> paths;
        if(!root) return paths;
        construct_path(root,path,paths);
        return paths;
    }
};