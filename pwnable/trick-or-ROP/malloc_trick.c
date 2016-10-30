#include <stdlib.h>
#include <stdio.h>

int main(){
    long long i;
    long long *a;

    for (i = 0; i < 0x90; i += 2) {
        a = malloc(i);
        printf("0x%llx => 0x%llx\n", i, *(a-1)-1);
        free(a);
        a = NULL;
    }
    return 0;
}
