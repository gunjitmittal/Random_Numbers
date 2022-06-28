#include<stdio.h>
int main()
{
    FILE *fp;
    fp=fopen("gau.dat", "r");
    float data[1000000];
    float sum = 0;
    for(int i =0;i<1000000; i++)
    {
        fscanf(fp, "%f",&data[i]);
        sum += data[i];
    }
    float sum2 = 0;
    float exp = sum/1000000;
    for(int i =0;i<1000000; i++)
    {
        sum2 += (data[i] - exp)*(data[i] - exp);
    }
    float var = sum2/1000000;
    printf("Mean: %f\n",exp);
    printf("Variance: %f\n",var);
}