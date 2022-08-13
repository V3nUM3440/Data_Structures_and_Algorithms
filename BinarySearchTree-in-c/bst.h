//
// Author - Shuber Ali Mirza
// ID ----- 20027047
// bst.h -- Contains BST function declarations from bst.c, and "Tree" and "TreeNode" structs
//

#ifndef BST
#define BST

typedef struct TreeNode{
    const char* key;
    const void* val;
    struct TreeNode* left;
    struct TreeNode* right;
} TreeNode;

typedef struct Tree{
    TreeNode* root;
} Tree;

Tree* treeNew(void);
int treePut(Tree* tree, const char* key, const void* value);
void treeFree(Tree* tree);
int treeContains(Tree* tree, const char* key);
void* treeGet(Tree* tree, const char* key);
int treeRemove(Tree* tree, const char* key);

#endif // BST