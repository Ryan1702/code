#include<stdio.h>
#include<math.h>
int calculate(int a,int b,char c)
{
    int ans;
    switch(c)
    {
        case 'A':
            ans=a+b;
            break;
        case 'B':
            ans=a*b;
            break;
        case 'C':
            ans=a-b;
            break;
        case 'D':
            ans=a%b;
        case 'E':
            ans=pow(a,b);
    }
    return ans;
}
char get_choice()
{
    char op=' ';
    printf(" A. Add numbers\n");
    printf(" B. Multiply numbers\n");
    printf(" C. Subtract numbers\n");
    printf(" D. Remainder of numbers\n");
    printf(" E. Power of numbers\n");
    puts("");
    while(((op-'A')<0)||((op-'A')>4))
    {
        if(op!=' ') printf("Your choice is invalid. ");
        printf("What is your choice? : ");
        scanf(" %c",&op);
        puts("");
    }
    return op;
}
int main()
{
    char c;
    c=get_choice();
    printf("Enter 2 numbers : ");
    int a,b;
    scanf("%d%d",&a,&b);
    printf("Answer : %d\n",calculate(a,b,c));
    return 0;
}
