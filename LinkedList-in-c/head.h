#ifndef LIST
#define LIST

#define False 0
#define True !False

typedef struct Node{
    int data;
    struct Node* next;
    struct Node* prev;
} Node;

typedef struct{
    Node* head;
    Node* tail;
} linkedList;

linkedList* listCreate();
void listInsertLast(linkedList* list, int num);
void listPrint(linkedList* list);
void listFree(linkedList* list);

#endif /* LIST */