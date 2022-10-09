#include<stdio.h>

int main()
{
    int age = 18;
    double marks = 99.99;
    // for single character we use ''
    char grade = 'A';
    // to type a string we use []
    char name[] = "Dishambha Awasthi";
    printf("%s",name);
    // format specifier %d , %s, %f 
    printf("I am %s and marks are %f and I got a grade %s",name,marks,grade);
    return 0;
}
