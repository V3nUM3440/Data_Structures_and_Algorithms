//
// Author - Shuber Ali Mirza
// ID ----- 20027047
// main.c - Contains main function that tests the bst
//

#include <stdio.h> // printf
#include "bst.h" // BST functions, "Tree" struct
#include "extra.h" // "example" struct

int main(){
    // NEW: returns "Tree" struct
    Tree* tree = treeNew();
    
    // PUT: takes "Tree" struct, char* key, and void* value
    printf("# --------------------- Putting --------------------- #\n");
    printf("1 on success, 0 on failure\n");
    int x = 10;
    printf("Put Key-> Gang\t\tValue-> int:\t%d\n", treePut(tree, "Gang", (void*)&x));
    char* str = "Panda";
    printf("Put Key-> Duck\t\tValue-> char*:\t%d\n", treePut(tree, "Duck", (void*)str));
    float new = 15.5;
    void* f = &new;
    printf("Put Key-> Shuber\tValue-> float:\t%d\n", treePut(tree, "Shuber", f));
    char c = 'a';
    void* ch = &c;
    printf("Put Key-> Man\t\tValue-> char:\t%d\n", treePut(tree, "Man", ch));
    unsigned int u = 100;
    void* uptr = &u;
    printf("Put Key-> Trench\tValue-> uint:\t%d\n", treePut(tree, "Trench", uptr));
    str = "something";
    printf("Put Key-> Bat\t\tValue-> char*:\t%d\n", treePut(tree, "Bat", (void*)str));
    c = 'C';
    void* p = &c;
    printf("Put Key-> Forget\tValue-> char:\t%d\n", treePut(tree, "Forget", p));
    example lol;
    lol.x = 10;
    lol.y = "lol";
    void* lel = &lol;
    printf("Put Key-> Zrrrrr\tValue-> struct:\t%d\n", treePut(tree, "Zrrrrr", lel));
    // Unsuccessful if key already exists
    printf("Put Key-> Zrrrrr\tValue-> struct:\t%d\n", treePut(tree, "Zrrrrr", lel));
    printf("Fails because key already exists\n");
    
    printf("\n# --------------------- Current Configuration --------------------- #\n");
    // Since these are hardcoded, if something didn't work correctly, you would get seg fault
    printf("Root:\t\t\tKey-> %s\tValue(int)-> %d\n", tree->root->key, *(int*)treeGet(tree, "Gang"));
    printf("Left:\t\t\tKey-> %s\tValue(char*)-> %s\n", tree->root->left->key, (char*)treeGet(tree, "Duck"));
    printf("Right:\t\t\tKey-> %s\tValue(float)-> %.2f\n", tree->root->right->key, *(float*)treeGet(tree, "Shuber"));
    printf("Right Left:\t\tKey-> %s\tValue(char)-> %c\n", tree->root->right->left->key, *(char*)treeGet(tree, "Man"));
    printf("Right Right:\t\tKey-> %s\tValue(uint)-> %u\n", tree->root->right->right->key, *(unsigned int*)treeGet(tree, "Trench"));
    printf("Left Left:\t\tKey-> %s\tValue(char*)-> %s\n", tree->root->left->left->key, (char*)treeGet(tree, "Bat"));
    printf("Left Right:\t\tKey-> %s\tValue(char)-> %c\n", tree->root->left->right->key, *(char*)treeGet(tree, "Forget"));
    example e = *(example*)treeGet(tree, "Zrrrrr");
    printf("Right Right Right:\tKey-> %s\tValue(struct[int])-> %d\n", tree->root->right->right->right->key, e.x);
    
    printf("\n\n                   Gang              \n");
    printf("                /        \\              \n");
    printf("             Duck         Shuber         \n");
    printf("           /     \\      /     \\        \n");
    printf("         Bat   Forget  Man    Trench     \n");
    printf("                                   \\    \n");
    printf("                                  Zrrrrr \n");
    
    // CONTAINS: takes "Tree" struct and char* key, returns 1 on success and 0 on failure
    printf("\n# --------------------- Contains --------------------- #\n");
    printf("1 on success, 0 on failure\n");
    printf("Contains 10:\t\t%d\n", treeContains(tree, "10"));
    printf("Contains Bat:\t\t%d\n", treeContains(tree, "Bat"));
    printf("Contains Forget:\t%d\n", treeContains(tree, "Forget"));
    printf("Contains two:\t\t%d\n", treeContains(tree, "two"));
    printf("Contains shuber:\t%d\n", treeContains(tree, "shuber"));
    printf("Contains Duck:\t\t%d\n", treeContains(tree, "Duck"));
    printf("Contains MAN:\t\t%d\n", treeContains(tree, "MAN"));
    
    // GET: takes "Tree" struct and char* key, returns void* of value stored in node on success, else returns NULL
    printf("\n# --------------------- Get --------------------- #\n");
    printf("void* on success, NULL on failure\n");
    printf("Get Forget:\tValue(char)-> %c\n", *(char*)(treeGet(tree, "Forget")));
    example panda = *(example*)(treeGet(tree, "Zrrrrr"));
    printf("Get Zrrrrr:\tValue(struct[char*])-> %s\n", panda.y);
    printf("Get abcd:\tValue(pointer)-> %p\n", treeGet(tree, "abcd"));
    
    // REMOVE: takes "Tree" struct and char* key, returns 1 on success and 0 on failure
    printf("\n# --------------------- Remove --------------------- #\n");
    printf("1 on success, 0 on failure\n");
    printf("Remove Trench:\t\t%d\n", treeRemove(tree, "Trench"));
    printf("Contains Trench:\t%d\n", treeContains(tree, "Trench"));
    printf("Contains Zrrrrr:\t%d\n", treeContains(tree, "Zrrrrr"));
    printf("Right Right:\t\tKey-> %s\tValue(struct[int])-> %d\n", tree->root->right->right->key, panda.x);
    printf("After removing \"Trench\" which has one child, Right child \"Zrrrrr\" still in tree and becomes its successor\n\n");
    
    printf("Remove Duck:\t\t%d\n", treeRemove(tree, "Duck"));
    printf("Contains Duck:\t\t%d\n", treeContains(tree, "Duck"));
    printf("Left:\t\t\tKey-> %s\tValue(char)-> %c\n", tree->root->left->key, *(char*)treeGet(tree, "Forget"));
    printf("Left Left:\t\tKey-> %s\tValue(char*)-> %s\n", tree->root->left->left->key, (char*)treeGet(tree, "Bat"));
    printf("After removing \"Duck\" which has two children;\nRight child \"Forget\" becomes its successor\nLeft child \"Bat\" becomes left child of \"Forget\"\n");
    
    printf("\n# --------------------- Configuration After Change --------------------- #\n");
    // Since these are hardcoded, if something didn't work correctly, you would get seg fault
    printf("Root:\t\tKey-> %s\tValue(int)-> %d\n", tree->root->key, *(int*)treeGet(tree, "Gang"));
    printf("Left:\t\tKey-> %s\tValue(char)-> %c\n", tree->root->left->key, *(char*)treeGet(tree, "Forget"));
    printf("Right:\t\tKey-> %s\tValue(float)-> %.2f\n", tree->root->right->key, *(float*)treeGet(tree, "Shuber"));
    printf("Right Left:\tKey-> %s\tValue(char)-> %c\n", tree->root->right->left->key, *(char*)treeGet(tree, "Man"));
    printf("Right Right:\tKey-> %s\tValue(struct[int])-> %d\n", tree->root->right->right->key, panda.x);
    printf("Left Left:\tKey-> %s\tValue(char*)-> %s\n", tree->root->left->left->key, (char*)treeGet(tree, "Bat"));
    
    printf("\n\n                   Gang              \n");
    printf("                /        \\              \n");
    printf("             Forget       Shuber         \n");
    printf("           /             /     \\        \n");
    printf("         Bat            Man    Zrrrrr  \n\n");
    
    // FREE
    treeFree(tree);
    
    return 0;
}

