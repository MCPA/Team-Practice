#include <stdio.h>
#include <stdlib.h>

int readline(char * buf, int maxsize) {
  int i = 0;
  char c;
  while (c = getchar()) {
    if (c == EOF) {
      return 0;
    }
    if (c == '\n' || c == maxsize) {
      buf[i++] = '\0';
      return i;
    }
    buf[i++] = c;
  }
}

int main(int argc, char ** argv) {
  char msg[20];
  char cmd[20];
  while(readline(msg, sizeof(msg))) {
    sprintf(cmd, "echo %s", msg);
    system(cmd);
    fflush(stdout);
  }
  exit(0);
}
