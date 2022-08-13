//
// Author - Shuber Ali Mirza
// ID ----- 20027047
// extra.c -- Contains immitation of strcmp function
//

#include "extra.h"

// Function based on: https://www.javatpoint.com/c-program-to-compare-the-two-strings
// Immitates the strcmp library function
int strComp(const char* str1,const char* str2){
    int diff = 0;
    int flag = 0;
    while(*str1 != '\0' && *str2 != '\0' && flag == 0){
        if(*str1 != *str2){
            if(*str1 < *str2){
                diff = -1;
                flag = 1;
            } else{
                diff = 1;
                flag = 1;
            }
        }
        str1++;
        str2++;
    }
    return diff;
}