#include <stdio.h>
#include <stdlib.h>
#include "head.h"

linkedList* listCreate(){
    linkedList* list = malloc(sizeof(linkedList));
    list->head = malloc(sizeof(Node));
    list->tail = malloc(sizeof(Node));
    
    list->head->data = False;
    list->head->next = list->tail;
    list->head->prev = NULL;
    
    list->tail->data = False;
    list->tail->next = NULL;
    list->tail->prev = list->head;
    
    return list;
}

void listInsertLast(linkedList* list, int num){
    if (list->head->data == False){
        list->head->data = num;
    }
    else if (list->tail->data == False){
        list->tail->data = num;
    }
    else{
        Node* new = malloc(sizeof(Node));
        new->data = num;
        new->prev = list->tail;
        new->next = NULL;
        
        list->tail->next = new;
        list->tail = new;
    }
}

void listPrint(linkedList* list){
    int i = 1;
    Node* curr = list->head;
    
    while (curr != NULL){
        printf("Item No. %d: %d\n", i, curr->data);
        curr = curr->next;
        i++;
    }
}

void listFree(linkedList* list){
    Node* curr = list->head;
    Node* new;
    
    while (curr != NULL){
        new = curr->next;
        free(curr);
        curr = new;
    }
    free(list);
}
