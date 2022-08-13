//
// Author - Shuber Ali Mirza
// ID ----- 20027047
// extra.h -- Contains declaration of immitation of strcmp function from extra.c and "example" struct for testing
//

#ifndef EXTRA
#define EXTRA

typedef struct {
    int x;
    char* y;
} example;

int strComp(const char* str1,const char* str2);

#endif // EXTRA