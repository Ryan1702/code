#include<stdio.h>
double cm_to_inches(double c)
{
    return c*0.394;
}
double get_input()
{
    printf("Enter centimeter : ");
    double a;
    scanf("%lf",&a);
    printf("%.2f cm is equals to ",a);
    return cm_to_inches(a);
}
int main()
{
    char op='Y';
    while(op=='Y')
    {
        printf("%.2f inches\n",get_input());
        puts("");
        printf("Continue <Y - Yes   N - No>: ");
        scanf(" %c",&op);
        puts("");
    }
    printf("Program ends.\n");
    return 0;
}
