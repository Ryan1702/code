#include<stdio.h>
#include<string.h>
#include<math.h>
#define Maxn 100
double trans(char s[])
{
    int len=strlen(s),i;
    double ans=0;
    for(i=0;i<len;i++)
    {
        if(s[i]=='.') break;
        if(s[i]-'0'>=0&&s[i]-'0'<=9)
        {
            ans=ans*10+(s[i]-'0');
        }
    }
    double cnt=1;
    for(;i<len;i++)
    {
        if(s[i]-'0'>=0&&s[i]-'0'<=9)
        {
            cnt/=10;
            ans+=cnt*(s[i]-'0');
        }
    }
    return ans;
}
int main()
{
    int cnt=3;
    double ans=0;
    while(cnt--)
    {
        char name[Maxn+5],pri[Maxn+5],end;
        printf("Enter product's name : ");
        scanf("%[^\n]%c",name,&end);
        printf("Enter the price      : ");
        scanf("%[^\n]%c",pri,&end);
        puts("");
        printf("%s : %s\n",name,pri);
        puts("");
        ans+=trans(pri);
    }
    printf("Total amount         : RM %.2f",ans);
    return 0;
}
