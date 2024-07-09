
 // Definition for a binary tree node.
//   struct TreeNode {
//       int val;
//       TreeNode *left;
//       TreeNode *right;

//       TreeNode() : val(0), left(nullptr), right(nullptr) {}
//       TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
//       TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
//   };

class Solution {
public:
    vector<int>ans;
    void bfs(TreeNode* node){
        queue<TreeNode*>que;
        que.push(node);
        int level = 0;
        int l = 1;
        while(que.size() != 0){
            TreeNode* curr = que.front();
            que.pop();
            l--;

            if(curr->left){
                que.push(curr->left);
            }
            if(curr->right){
                que.push(curr->right);
            }

            if(l == 0 && que.size()){
                l = que.size();
                int val = que.back()->val;
                ans.push_back(val);
            }
        }
    }
    
    vector<int> rightSideView(TreeNode* root) {
        if(!root){
            return {};
        }
        ans.push_back(root->val);
        bfs(root);
        return ans;
    }
};