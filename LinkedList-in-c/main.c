#include "head.h"

int main(){
    linkedList* list = listCreate();
    
    listInsertLast(list, 10);
    listInsertLast(list, 20);
    listInsertLast(list, 30);
    listInsertLast(list, 40);
    
    listPrint(list);
    listFree(list);
    
    return 0;
}
