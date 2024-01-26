#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

void sort(int *arr, int length){
    int n=length;
    int i,j,k,l;
    // all indices run from 0 to length-1
    for (k = 2; k <= n; k *= 2){ // k is doubled every iteration
        for (j = k/2; j > 0; j /= 2){ // j is halved at every iteration, with truncation of fractional parts
            for (i = 0; i < n; i++){
                l = i^j; // in C-like languages this is "i ^ j"
                if (l > i){
                    if ((i & k) == 0 && (arr[i] > arr[l]) || ((i & k) != 0 && (arr[i] < arr[l]))) {
                        //swap arr[i],arr[l]
                        int shelter=arr[i];
                        arr[i]=arr[l];
                        arr[l]=shelter;
                    }
                }
            }
        }
    }                            
}


double get_elapsed_time(struct timeval *begin, struct timeval *end)
{
    return (end->tv_sec - begin->tv_sec) * 1000000
        + (end->tv_usec - begin->tv_usec);
}

//test whether the sorting was successful
//0 for false, 1 for true
int test(int *arr,int length){
    int i=0;
    while(i<length-1){
        if (arr[i]>arr[i+1]) {
            return 0;
        }
        i++;
    }
    return 1;
}

int main(int argc, char* argv[]){
    struct timeval t1, t2;
    //set length as 2**power
    int power=3;//default
    if (argc>=2) {
        power=atoi(argv[1]);
    }
    int length=1<<power;
    
    //generating an array of integers with input length
    int *arr=(int *)malloc(length*sizeof(int));
    int i;
    for(i=0;i<length;i++){
        arr[i]=rand();
    }
    
    gettimeofday(&t1, NULL);
    sort(arr,length);
    gettimeofday(&t2, NULL);
    
    
    {
        double us;
        us = get_elapsed_time(&t1, &t2);
        printf("\nElapsed time: %.3lf sec\n", us/1000000.0);
        int sorted=test(arr,length);
        if(sorted){
            printf("\nSorting successful.\n");
        }
        else{
            printf("\nSorting failed.\n");
        }
        return 0;
    }
}