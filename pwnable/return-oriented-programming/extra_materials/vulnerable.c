// gcc test.c -m32 -o test -z execstack -fno-stack-protector
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

void hidden(){
	asm ("pop %eax\n\t"
		"call *%esp \n\t"
		 "nop\n\t"
		 "nop\n\t"
		 "jmp *%esp");
}

void foo(){
	char buf[50];
	printf("Please enter a string: ");
	scanf("%s", buf);
	printf("Your string was: %s\n", buf);
}

int main(int argc, char **argv) {
	setvbuf(stdout, NULL, _IONBF, 0);
	foo();

    return 0;
}