#include<stdio.h>
double calculateCharges(int bh,int bm,int eh,int em)
{
    int op=0;
    if(bh>eh||(bh==eh&&bm>em))
    {
        int m=bh;
        bh=eh;eh=m;
        m=bm;
        bm=em;em=m;
        op=1;
    }
    int ans=(eh*60+em)-(bh*60+bm);
    if(op) ans=24*60-ans;
    if(ans>=60) printf("You have parked for %d hour(s) and %d minute(s)\n",ans/60,ans%60);
    else printf("You have parked for %d minute(s)\n",ans);
    if(ans>3*60) return 2.5;
    else return 1.5;
}
int main()
{
    int a,b,c,d;
    printf("Time in (HH) : ");
    scanf("%d",&a);
    printf("Time in (MM) : ");
    scanf("%d",&b);
    printf("Time out (HH) : ");
    scanf("%d",&c);
    printf("Time out (MM) : ");
    scanf("%d",&d);
    printf("Total charges = $ %.2f\n",calculateCharges(a,b,c,d));
    return 0;
}
