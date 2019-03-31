#include<stdio.h>
#include<time.h>
#include<stdlib.h>
#define max 256
void Trans(double a[][max]);
int main(void)
{
    clock_t start,end;
    int i,j;
    double a[max][max];
    for (i = 0; i< max; i++){
        for(j = 0; j < max; j++){
            a[i][j] = (double)(i+j);
        }
    }

    start = clock();
    printf("start time %lu2\n",start);

    Trans(a);

    end = clock();

    printf("end time %lu\n",end);
    printf("execution time %lu\n",end-start);

    return 0;
}
void Trans(double a[][max]){
    //printf("test");
    int B=15;
    int i,j,ii,jj;
    double b[max][max];
    for(i = 0;i<max;i+=B){
        for(j = 0;j<max;j+=B){
            for(ii=i;ii<(i+B)&&ii<max;ii++){
                for(jj=j;jj<(j+B)&&jj<max;jj++){
                    b[jj][ii] = a[ii][jj];
                }
            }
        }
    }
}