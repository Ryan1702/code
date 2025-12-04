#include<stdio.h>
#define Maxn 100
int main()
{
    char name[Maxn+5],id[Maxn+5];
    double fee;
    int dur;
    printf("Enter name                     : ");
    scanf("%s",name);
    printf("Enter ID                       : ");
    scanf("%s",id);
    printf("Enter fee (RM)                 : ");
    scanf("%lf",&fee);
    printf("Enter duration of study (years): ");
    scanf("%d",&dur);
    puts("");
    printf("-----------------------------------\n");
    printf("    XIAMEN UNIVERSITY MALAYSIA\n");
    printf("-----------------------------------\n");
    printf("Student name      : %s\n",name);
    printf("Student ID        : %s\n",id);
    printf("Duration of study : %d\n",dur);
    puts("");
    printf("Year     Course Fee\n");
    int cnt=1;
    do
    {
        printf(" %d       RM %.2f\n",cnt,fee);
        fee*=1.05;
    }while(++cnt<=dur);
    printf("-----------------------------------\n");
    return 0;
}
