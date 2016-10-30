#include <stdlib.h>
#include <stdio.h>

int main(void){
    long long n,i,j;
    char s[16];
    while (1) {
        if (!fgets(s, 16, stdin)){
            break;
        }
        n=strtoll(s, 0, 10);
        i = 1 << n;
        // prints 1 hex value padded with 16 bytes represented as a long long
        printf("1 << %lld = 0x%016llx\n", n,i);
        j = i >> n;
        printf("0x%016llx >> %lld = %lld\n", i,n,j);
    }
    return 0;
}
