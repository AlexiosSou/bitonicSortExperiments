#include "api.h"
#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <limits.h>

#define N UINT_MAX
int arr[N];

void seq_sort(int *arr, int length){
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

void acc_sort(int *arr, int length){
    int n=length;
    int i,j,k;
    //all indices run from 0 to length-1
    #pragma acc data copy(arr[0:length])
    for (k = 2; k <= n; k *= 2){ // k is doubled every iteration
        for (j = k/2; j > 0; j /= 2){ // j is halved at every iteration, with truncation of fractional parts
            #pragma acc kernels
            #pragma acc loop independent
            for (i = 0; i < n; i++){
                int l;
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

double seq_time(int size){
    struct timeval t1, t2;
    int length=1<<size;
    
    //generating an array of integers with input length
    int i;
    for(i=0;i<length;i++){
        arr[i]=rand();
    }
    
    gettimeofday(&t1, NULL);
    seq_sort(arr,length);
    gettimeofday(&t2, NULL);
    
    

    double us;
    us = get_elapsed_time(&t1, &t2);
    return us;
}

double acc_time(int size){
    struct timeval t1, t2;
    int length=1<<size;
    
    //generating an array of integers with input length
    int i;
    for(i=0;i<length;i++){
        arr[i]=rand();
    }
    
    gettimeofday(&t1, NULL);
    acc_sort(arr,length);
    gettimeofday(&t2, NULL);
    
    

    double us;
    us = get_elapsed_time(&t1, &t2);
    return us;

}