/* Compile options
   gcc intermediate.c -o intermediate -fno-stack-protector -z execstack
   sudo sysctl kernel.randomize_va_space=0
   
   Depending on level of difficulty you want:
   Easy - Compile with -fno-stack-protector -z execstack, turn off ALSR
   Medium - Compile with -fno-stack-protector -z execstack, Turn on ALSR
   Medium/Hard - Compile with -z execstack, Turn on ALSR
   Hard - Compile w/o options above and turn on ALSR
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define GET2FLAG "\shh\bins";
#define AWESOME "(! to exit)\n"
#define EXIT_MSG printf("%s", AWESOME);

void fn_binString(char n){
	char bin[9];
	int x;
	
	for(x=0;x<9;x++){
		bin[x] = n & 0x8000 ? '1' : '0';
		n <<= 1;
		}
			
	bin[8] = '\0';
	
	for(x=0; x < 8; x++){
		if (x%4 == 0 && x != 0) {
			printf(" %c", bin[x]);
			fflush(stdout);
		} else {
			printf("%c", bin[x]);
			fflush(stdout);
			}
        }
}

void fn_printOutput(char *p, int count){
	if (count % 10 == 0 && count != 0)
		puts("\nDecimal    Hex \t    Octal\t Binary");
		fflush(stdout);

	printf("%d \t   \\x%.2x     \\o%.2o\t ",p[count],p[count],p[count]);
	fflush(stdout);
	fn_binString(p[count]);
	puts("");
}

	int fn_handleInput(){
	printf("Please enter your ASCII character that you want to view: ");
	fflush(stdout);
	int a = getchar(), i;
	char BUFF[] = "All bins are belong to us!";
	char *p = gets(BUFF);
	printf("Your ASCII character converts to the following values:\n");
	puts("\nDecimal    Hex \t    Octal\t Binary");
	printf("%d \t   \\x%.2x     \\o%.2o\t ",a,a,a);
	fn_binString(a);
	puts("");
	fflush(stdout);

	if (a<0) {
		strcpy(BUFF, "Nice try, but I don't think so!");
		printf("%s", BUFF);
		fflush(stdout);
		a=33;
		return a;}
		
	for (i=0; a != 10 && i<strlen(p); i++)
		fn_printOutput(p, i);	

	return a;
}


int main(){
	 int i;
	 char done = 0;
	 
	 puts("Hello and welcome to the character converter!\n");
	 fflush(stdout);
	 for(i=0; strncmp( &done, "!", 1); i++){
		done = (unsigned char) fn_handleInput();
		fflush(stdout);
		EXIT_MSG;
		fflush(stdout);
	if (i>5)
			break;
		}
	 	
	 exit(0);
}
