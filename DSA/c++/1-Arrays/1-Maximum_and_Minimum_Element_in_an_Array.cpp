#include <iostream>
#include <limits>

void get_min_max(int array[] , int size ,int &min, int &max ){

    min = std::numeric_limits<int>::max();
    max = std::numeric_limits<int>::min();

    for (int i=0; i < size; i++){
        if(array[i]< min){
            min = array[i];
        }
        if(array[i]> max){
            max = array[i];
        }
    }
}

int main(){
    int array1[] = {3, 5, 4, 1, 9};
    int array2[] = {22, 14, 8, 17, 35, 3};
    int min , max;

    get_min_max(array1,5,min , max);
    printf("Array 1: Min = %d, Max = %d\n", min, max);

    get_min_max(array2, 6, min, max);
    printf("Array 2: Min = %d, Max = %d\n", min, max);
    
}