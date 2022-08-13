//
// Author - Shuber Ali Mirza
// ID ----- 20027047
// bst.c -- Contains BST functions
//

#include <stddef.h> // NULL
#include <sys/mman.h> // mmap(), munmap()
#include "bst.h" // "Tree" and "TreeNode" structs
#include "extra.h" // strComp

// Main New function
Tree* treeNew(void){
    Tree* tree = mmap(NULL, sizeof(Tree*),
                      PROT_READ | PROT_WRITE,
                      MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    tree->root = mmap(NULL, sizeof(TreeNode*),
                      PROT_READ | PROT_WRITE,
                      MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    return tree;
}

// Makes new node once parent is found in treePut function
static TreeNode* treeNewNode(const char* key, const void* value){
    TreeNode* new = mmap(NULL, sizeof(TreeNode*),
                         PROT_READ | PROT_WRITE,
                         MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    new->key = key;
    new->val = value;
    
    return new;
}

// Main Put function
int treePut(Tree* tree, const char* key, const void* value){
    int res = 0;
    TreeNode* cur = tree->root;
    while(res == 0){
        if(cur->key == NULL){
            cur->key = key;
            cur->val = value;
            res = 1;
        } else if(strComp(cur->key, key) == 0){
            return 0;
        } else if(strComp(cur->key, key) > 0 && cur->left == NULL){
            TreeNode* new = treeNewNode(key, value);
            cur->left = new;
            res = 1;
        } else if(strComp(cur->key, key) > 0 && cur->left != NULL){
            cur = cur->left;
        } else if(strComp(cur->key, key) < 0 && cur->right == NULL){
            TreeNode* new = treeNewNode(key, value);
            cur->right = new;
            res = 1;
        } else if(strComp(cur->key, key) < 0 && cur->right != NULL){
            cur = cur->right;
        }
    }
    return res;
}

// FREE RECURSIVE
static void treeFreeNode(TreeNode* node){
    if(node){
        treeFreeNode(node->left);
        treeFreeNode(node->right);
        munmap(node, sizeof(TreeNode*));
        node = NULL;
    }
}

// Main Free function
void treeFree(Tree* tree){
    treeFreeNode(tree->root);
    munmap(tree, sizeof(Tree*));
}

// CONTAINS RECURSIVE
static void treeContainsNode(TreeNode* node, const char* key, int* res){
    if(node){
        if(strComp(node->key, key) == 0){
            *res = 1;
        } else if(strComp(node->key, key) > 0){
            treeContainsNode(node->left, key, res);
        } else{
            treeContainsNode(node->right, key, res);
        }
    }
}

// Main Contains function
int treeContains(Tree* tree, const char* key){
    int* pRes = mmap(NULL, sizeof(int*),
                     PROT_READ | PROT_WRITE,
                     MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    int res;
    *pRes = 0;
    treeContainsNode(tree->root, key, pRes);
    res = *pRes;
    munmap(pRes, sizeof(int*));
    
    return res;
}

// GET RECURSIVE
static void* treeGetNode(TreeNode* node, const char* key){
    if(node){
        if(strComp(node->key, key) == 0){
            return (void*)(node->val);
        } else if(strComp(node->key, key) > 0){
            treeGetNode(node->left, key);
        } else{
            treeGetNode(node->right, key);
        }
    }
}

// Main Get function
void* treeGet(Tree* tree, const char* key){
    TreeNode* cur = NULL;
    cur = treeGetNode(tree->root, key);
    return cur;
}

// Gets Successor of node with two children about to be removed
static TreeNode* treeGetSucc(TreeNode* delNode){
    TreeNode* succParent = delNode;
    TreeNode* succ = delNode->right;
    while(succ->left){
        succParent = succ;
        succ = succ->left;
    }
    if(succ->right && succ != delNode->right){
        succParent->left = succ->right;
        succ->right = NULL;
    } else if(!succ->right && succ != delNode->right){
        succParent->left = NULL;
    }
    return succ;
}

// Checks how many children the node that needs to be removed has and gets successor accordingly
static void treeRemoveChild(TreeNode* parent, TreeNode* child, char* whichChild, int* res){
    // leaf node
    if(child->left == NULL && child->right == NULL){
        if(strComp(whichChild, "left") == 0){
            munmap(parent->left, sizeof(TreeNode*));
            parent->left = NULL;
        } else{
            munmap(parent->right, sizeof(TreeNode*));
            parent->right = NULL;
        }
        *res = 1;
    }
    // only right child
    else if(child->left == NULL && child->right != NULL){
        TreeNode* temp = child->right;
        if(strComp(whichChild, "left") == 0){
            munmap(parent->left, sizeof(TreeNode*));
            parent->left = temp;
        } else{
            munmap(parent->right, sizeof(TreeNode*));
            parent->right = temp;
        }
        *res = 1;
    } 
    // only left child
    else if(child->left != NULL && child->right == NULL){
        TreeNode* temp = child->left;
        if(strComp(whichChild, "left") == 0){
            munmap(parent->left, sizeof(TreeNode*));
            parent->left = temp;
        } else{
            munmap(parent->right, sizeof(TreeNode*));
            parent->right = temp;
        }
        *res = 1;
    }
    // both children
    else{
        TreeNode* succ = treeGetSucc(child);
        if(succ != child->right){
            succ->right = child->right;
        }
        succ->left = child->left;
        if(strComp(whichChild, "left") == 0){
            munmap(parent->left, sizeof(TreeNode*));
            parent->left = succ;
        } else{
            munmap(parent->right, sizeof(TreeNode*));
            parent->right = succ;
        }
        *res = 1;
    }
}

// REMOVE RECURSIVE
static void treeRemoveNode(TreeNode* parent, const char* key, int* res){
    if(parent){
        TreeNode* left = parent->left;
        TreeNode* right = parent->right;
        // left child
        if(left && strComp(parent->key, key) > 0){
            if(strComp(left->key, key) == 0){
                treeRemoveChild(parent, left, "left", res);
            }
            // recurring left
            else{
                treeRemoveNode(left, key, res);
            }
        }
        // right child
        else if(right && strComp(parent->key, key) < 0){
            if(strComp(right->key, key) == 0){
                treeRemoveChild(parent, right, "right", res);
            }
            // recurring right
            else{
                treeRemoveNode(right, key, res);
            }
        }
    }
}

// Main Remove function
int treeRemove(Tree* tree, const char* key){
    int* cur = mmap(NULL, sizeof(int*),
                    PROT_READ | PROT_WRITE,
                    MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    *cur = 0;
    int res;
    treeRemoveNode(tree->root, key, cur);
    res = *cur;
    munmap(cur, sizeof(int*));
    cur = NULL;
    return res;
}